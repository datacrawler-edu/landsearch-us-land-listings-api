# LandSearch API for U.S. Land Listings

Search U.S. land listings by location, price, and acreage, then use the results in Python, JavaScript, or a spreadsheet. [Open LandSearch Scraper on Apify](https://apify.com/datascraperes/landsearch-us-land-scraper?fpr=edudata)

## What this repository helps you do

- Compare land for sale across counties with the same price and acreage bounds.
- Fetch details for individual property URLs.
- Export saved listing results as CSV without starting another run.

## Example result

See the [example Dataset](data/sample-output.json) and its [CSV export](data/sample-output.csv). Each row represents a unique listing and includes its LandSearch URL.

## Run without code

Open the [hosted Actor](https://apify.com/datascraperes/landsearch-us-land-scraper?fpr=edudata), enter a location, and select **Start**. Open **Dataset** to inspect or export the results. [Web guide](docs/no-code-guide.md)

## Try it with Apify's free plan

Apify's Free plan includes $5 in monthly prepaid usage that can be used in its Store and requires no credit card. Check available credit and [current plan terms](https://apify.com/pricing?fpr=edudata) before running a larger search.

## Quick start for developers

Set `APIFY_API_TOKEN` in your environment and run from the repository root:

```bash
python examples/python/request.py
```

The Python examples use the standard library. The JavaScript example uses native fetch in Node.js 20 or later.

## Input example

```json
{"location":"Texas","maxItems":3,"listingFormat":"sale","minAcres":1,"maxAcres":100}
```

[Complete request](data/sample-input.json) · [Input reference](docs/input-reference.md)

## Request examples

- [cURL](examples/curl-request.md)
- [Python single run](examples/python/request.py)
- [Python county batch](examples/python/batch_locations.py)
- [Python export from an existing Dataset](examples/python/export_csv.py)
- [JavaScript](examples/javascript/request.mjs)

## Output fields

Use `id` to identify a listing, `url` to open it, `acres` to compare area, and `priceUsd` for the advertised price when available. See the [output reference](docs/output-reference.md).

## Common use cases

[Compare counties, fetch known properties, and export a shortlist](docs/use-cases.md).

## Filter land listings by acres and price

Supply `minAcres`, `maxAcres`, `minPrice`, or `maxPrice` for a location search. Keep a small `maxItems` while checking the result set.

## Export LandSearch listings to CSV

Pass an existing default Dataset ID to `python examples/python/export_csv.py DATASET_ID listings.csv`. The export reads the saved rows and does not launch a run.

## FAQ

[Inputs, listing details, prices on request, and partial collections](docs/faq.md).

## Limits and pricing

The Actor bills one listing event per unique listing confirmed in the Dataset. Optional listing details use the same event. Check the [Pricing tab](https://apify.com/datascraperes/landsearch-us-land-scraper?fpr=edudata) for current tier rates. Check the run summary before treating an export as complete.

## Hosted version

[Run LandSearch Scraper on Apify](https://apify.com/datascraperes/landsearch-us-land-scraper?fpr=edudata).

## Responsible use

Respect the terms and privacy obligations that apply to your use of listing data. Keep API tokens out of logs and commits.

## Support

[Open a GitHub issue](https://github.com/datacrawler-edu/landsearch-us-land-listings-api/issues) for example problems. Include a sanitized input and run ID when available.

## License

[MIT](LICENSE)
