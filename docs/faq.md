# FAQ

**Can I search by ZIP code?** Yes. Pass it as a string in `location`.

**Can I pass a property URL and a state together?** Choose one mode per run.

**Does enrichment add a separate charge?** The Actor uses the same listing event when detail is included.

**Why is the price missing?** If the seller asks you to request the price, the output can have a null `priceUsd` and `priceOnRequest` set.

**Can a successful run return only some requested listings?** Yes. Inspect the persisted SUMMARY status and stop reason. Check the existing run before submitting another paid start.
