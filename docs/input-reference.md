# Input reference

Choose one target. Set `location` to a U.S. state, county with state, city with state, ZIP code, or LandSearch location slug. Use `United States` for a national search. Alternatively, set `listingUrls` to an array of up to 1,000 HTTPS property URLs.

| Optional field | Meaning |
| --- | --- |
| `maxItems` | 1–50,000, default 100 when omitted |
| `listingFormat` | `all`, `sale`, `lease`, `auction` |
| `minPrice`, `maxPrice` | Advertised price bounds in USD |
| `minAcres`, `maxAcres` | Acreage bounds |
| `sort` | `newest`, `oldest`, `priceLow`, `priceHigh`, `acresLow`, `acresHigh` |
| `includeDetails` | Include available details, default false |

In URL mode omit location, price and acreage filters, or format/sort overrides. Details are included when available.
