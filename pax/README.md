# PAX — Demo Domain

A skeleton Praxis PAX (v4) wrapping the demo-dashboard's domain. Built as the **bonus arc** of the École des Mines lecture: showing how a one-off Streamlit app's underlying concepts can be packaged as portable, replicable, comparable knowledge.

## Structure

```
pax.yaml                              # manifest (v4)
knowledge/
  domain.json                         # the field
  constructs.json                     # the variables, with formal defs
  sources.json                        # the data's provenance
  findings.json                       # [] — populate after real analyses run
playbooks/
  quick_start.yaml                    # reproducible workflow
```

## Why this exists in the deck

A dashboard ships *an answer*. A PAX ships *a method*. The slide deck makes this contrast at minute 45.

## What's TBD

- Real findings, with effect sizes and structured statistics, once Elise's dataset replaces the synthetic placeholder
- Real `source_url` on the manifest's dataset entry
- A `construct_relationships.json` once the actual variables of interest are known
- Canonical-construct backbone (v3 backbone) — out of scope for the lecture demo

## References

- Full spec: `/Volumes/Muaddib/jelambert/Desktop/Dev/active/pax-market/docs/PAX_CREATION_GUIDE.md`
- Marketplace: [pax-market.com](https://pax-market.com)
- Validator: `python -m praxis_cli validate .`
