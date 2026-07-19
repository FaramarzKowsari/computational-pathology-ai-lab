# Release Guide — v1.0.1

## Before creating the release

1. Copy this update package into the repository root and replace the matching files.
2. Open GitHub Desktop and verify the changed files.
3. Commit with:

   `Prepare metadata and citations for v1.0.1`

4. Push to `main`.
5. Wait until CI, Docker Build, and GitHub Pages are green.
6. Confirm the repository version is `1.0.1` in:
   - `pyproject.toml`
   - `src/cpathlab/__init__.py`
   - `CITATION.cff`
   - `.zenodo.json`
   - `codemeta.json`
   - `CHANGELOG.md`

## Create the GitHub release

1. Open the repository's **Releases** page.
2. Select **Draft a new release**.
3. Choose **Create new tag**.
4. Enter: `v1.0.1`
5. Target: `main`
6. Release title: `Computational Pathology AI Lab v1.0.1`
7. Copy the contents of `docs/RELEASE_NOTES_v1.0.1.md` into the release description.
8. Do not mark it as a pre-release.
9. Keep **Set as the latest release** enabled.
10. Publish the release.

## After publication

Zenodo should automatically archive the release because the repository integration is enabled.

The project Concept DOI remains:

`10.5281/zenodo.21445854`

Zenodo will assign a new version-specific DOI to `v1.0.1`. The earlier `v1.0.0` DOI remains:

`10.5281/zenodo.21445855`

It is normal for the exact `v1.0.1` DOI not to be present inside the source archive that created it. Use the Concept DOI in repository badges and project-level citation metadata; use the Zenodo-generated version DOI when citing that exact archive.
