"""Export listing columns from an existing Dataset to CSV."""
import argparse
import csv

from request import rows

FIELDS = ("id", "title", "priceUsd", "acres", "city", "county", "stateCode", "url")


def export(dataset_id, output):
    with open(output, "w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows(dataset_id))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("output")
    args = parser.parse_args()
    export(args.dataset_id, args.output)
