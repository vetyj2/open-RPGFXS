# Contributing

Corrections to paths, search terms, frame timing, audio metadata, and documentation are welcome. Identify the relevant `ORFX`/`ORFXS` code or pairing, the file and a clear description of the evidence. For listening observations include the approximate time and distinguish a personal observation from existing review or automated signal analysis.

Keep published asset IDs and package-relative paths stable where possible. Do not overwrite historical review decisions with a newly proposed pairing; mark new recommendations as such. If packaged files change, update the relevant sidecars, indexes and integrity records, then run `python3 tools/build-asset-index.py` and `python3 tools/validate.py` from the repository root. Structural validation does not replace listening to a changed mix or checking a sprite animation.

Contributions submitted for inclusion are intended to be made available under this project's [CC0 1.0 dedication](LICENSE). Only submit material you can contribute under those terms.
