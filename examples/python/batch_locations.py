"""Compare two Texas counties with one bounded run per location."""
import json

from request import rows, run


if __name__ == "__main__":
    for location in ("Grayson County, TX", "Parker County, TX"):
        dataset = run({"location": location, "listingFormat": "sale", "minAcres": 1, "maxItems": 3})
        print(json.dumps({"location": location, "listings": list(rows(dataset))}, ensure_ascii=False))
