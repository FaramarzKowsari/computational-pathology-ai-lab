# Data Card

## Included data
Only procedurally generated synthetic 96 x 96 RGB patches and a generated label manifest are committed. They contain no patient data and are used solely for tests and smoke demonstrations.

## External data
The original educational project used the Kaggle Histopathologic Cancer Detection dataset. Users must obtain external datasets from their official source, accept their terms, and document the exact version and checksum.

## Split policy
The provided splitter supports stratification and optional group-aware splitting. For real slides, split by patient or slide before extracting patches to prevent leakage.

## Prohibited content
Do not commit protected health information, private slides, restricted annotations, or data without redistribution permission.
