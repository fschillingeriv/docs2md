# docs2md

Automatically mirrors the [Bitwarden Help Center](https://bitwarden.com/help/) as a collection of Markdown files, one per help article. The repository also stores OpenAPI spec files for Bitwarden's APIs, which are not included in the Help Center's machine-readable export.

## How it works

Bitwarden publishes a machine-readable snapshot of their help content at `https://bitwarden.com/help/llms-full.txt`. This file contains the full text of every help article in a structured format, with each article delimited by a front matter block:

```
---
URL: https://bitwarden.com/help/some-article/
---

Article content here...
```

A GitHub Actions workflow runs daily, fetches the latest `llms-full.txt`, and uses a Python script to split it into individual `.md` files under `docs/`. Each file is named after the last path segment of its source URL (e.g. `import-data.md`) and preserves the URL front matter for traceability.

## Repository structure

```
docs/                   Individual Markdown files, one per help article (~359 files)
specs/                  OpenAPI JSON specs for Bitwarden's APIs (manually maintained)
  api.json              Bitwarden Public API spec
  vault-management-api.json  Vault Management API spec
scripts/
  split_llms.py         Splits llms-full.txt into per-page .md files
llms-full.txt           Latest snapshot from bitwarden.com/help/llms-full.txt
.github/workflows/
  sync-llms.yml         Daily workflow that fetches and splits llms-full.txt
```

## Automated sync

The workflow in `.github/workflows/sync-llms.yml` runs automatically every day at midnight UTC and can also be triggered manually from the Actions tab.

On each run it:

1. Fetches the latest `llms-full.txt` from `https://bitwarden.com/help/llms-full.txt`
2. Clears the existing `docs/` directory
3. Runs `scripts/split_llms.py` to regenerate all `.md` files
4. Commits and pushes any changes

## API specs

Two Bitwarden API pages — `bitwarden.com/help/api/` and `bitwarden.com/help/vault-management-api/` — are not included in `llms-full.txt`. Their OpenAPI specs are stored manually in `specs/`.

To update them, download the latest JSON from the "Download Swagger JSON file" button on each page and commit the updated files to `specs/`.

## Drafts

The `drafts/` directory is used for work-in-progress document revisions and is not affected by the automated sync.
