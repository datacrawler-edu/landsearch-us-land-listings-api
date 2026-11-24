# Output reference

The default Dataset contains unique listings. Core fields include `id`, `title`, `url`, `format`, `status`, `priceUsd`, `acres`, location fields, coordinates, and a cover image URL when available. `priceOnRequest` marks listings advertised without a fixed price. `detailsIncluded` tells you whether enrichment was retrieved. Detail rows can include `description`, `imageUrls`, `parcelNumbers`, `taxes`, and `listingHistory`.

Inspect `SUMMARY` in the default key-value store for the collection status before treating a Dataset as complete. See the [example rows](../data/sample-output.json).
