"""Start one hosted search and read its Dataset."""
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://api.apify.com/v2"
ACTOR = "datascraperes~landsearch-us-land-scraper"
ROOT = Path(__file__).resolve().parents[2]


def api(path, payload=None):
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN.")
    body = json.dumps(payload).encode() if payload is not None else None
    request = Request(BASE + path, data=body,
                      headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def rows(dataset_id):
    offset = 0
    while True:
        options = urlencode({"offset": offset, "limit": 100})
        page = api(f"/datasets/{dataset_id}/items?{options}")
        if not page:
            return
        yield from page
        offset += len(page)


def run(input_payload):
    # A failed POST response can still represent a created run. Never replay a start automatically.
    started = api(f"/acts/{ACTOR}/runs?timeout=120&maxTotalChargeUsd=0.01", input_payload)["data"]
    run_id = started["id"]
    print(f"Run ID: {run_id}", file=sys.stderr)
    deadline = time.monotonic() + 180
    while time.monotonic() < deadline:
        current = api(f"/actor-runs/{run_id}")["data"]
        if current["status"] == "SUCCEEDED":
            kvs = current["defaultKeyValueStoreId"]
            summary = api(f"/key-value-stores/{kvs}/records/SUMMARY")
            if summary["status"] != "completed":
                raise RuntimeError(f"Inspect run {run_id}: {summary['stopReason']}")
            return current["defaultDatasetId"]
        if current["status"] in {"FAILED", "TIMED-OUT", "ABORTED"}:
            raise RuntimeError(f"Inspect run {run_id}: {current['status']}")
        time.sleep(2)
    raise RuntimeError(f"Polling expired. Inspect run {run_id} before submitting another start.")


if __name__ == "__main__":
    sample = json.loads((ROOT / "data/sample-input.json").read_text(encoding="utf-8"))
    print(json.dumps(list(rows(run(sample))), ensure_ascii=False, indent=2))
