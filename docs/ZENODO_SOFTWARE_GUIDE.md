# Zenodo Software DOI Guide

## Current permanent identifiers

- Software Concept DOI — all versions: `10.5281/zenodo.21445854`
- Archived software version `v1.0.0`: `10.5281/zenodo.21445855`
- Companion book DOI: `10.5281/zenodo.21444837`
- Google Books key for the companion book: `GGKEY:8ZWNQ7NFGBL`

The Concept DOI is the stable identifier for the software project. Zenodo creates a new version-specific DOI whenever a new GitHub release is archived.

## GitHub–Zenodo connection

The repository is connected and enabled in the Zenodo GitHub integration:

`FaramarzKowsari/computational-pathology-ai-lab`

Do not turn this connection off before publishing a GitHub release.

## Publishing version 1.0.1

1. Confirm that CI, Docker Build, and GitHub Pages are green.
2. Confirm that `pyproject.toml`, `src/cpathlab/__init__.py`, `CITATION.cff`, `.zenodo.json`, and `codemeta.json` report version `1.0.1`.
3. Commit and push all metadata changes to `main`.
4. Create the GitHub tag and release `v1.0.1` from the current `main` commit.
5. Wait for Zenodo to archive the release.
6. Open the new Zenodo record and copy its version-specific DOI.
7. Keep `10.5281/zenodo.21445854` as the primary project badge and permanent all-versions identifier.
8. Use the new version DOI only when citing the exact `v1.0.1` archive.

## Metadata rules

- Do not reuse the book DOI for the software.
- Do not replace the Concept DOI when a new release is created.
- Preserve ORCID `0000-0003-1692-0453`.
- Preserve the relationship to the companion book DOI.
- Never claim clinical validation or diagnostic performance.
