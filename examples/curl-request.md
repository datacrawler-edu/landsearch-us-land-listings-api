# cURL request

Run from the repository root with `APIFY_API_TOKEN` set in the environment.

```bash
curl --fail-with-body --request POST \
  'https://api.apify.com/v2/acts/datascraperes~landsearch-us-land-scraper/runs?timeout=120&maxTotalChargeUsd=0.01' \
  --header "Authorization: Bearer $APIFY_API_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

Retain `data.id` and read the existing run at `GET /v2/actor-runs/{runId}`. When it reaches a terminal state, use its Dataset and SUMMARY. If the start response is lost, inspect recent runs before retrying.
