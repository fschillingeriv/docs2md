#!/usr/bin/env python3
"""
Splits llms-full.txt into individual .md files, one per URL section.
Output mirrors the URL path structure under `docs/`.
e.g. https://bitwarden.com/help/import-data -> docs/help/import-data.md
"""

import re
import os
from pathlib import Path
from urllib.parse import urlparse

INPUT_FILE = "llms-full.txt"
OUTPUT_DIR = Path("docs")

SECTION_PATTERN = re.compile(
    r"^---\s*\nURL:\s*(\S+)\s*\n---\s*\n",
    re.MULTILINE
)

def url_to_path(url: str) -> Path:
    """Convert a URL to a flat path under OUTPUT_DIR using only the last path segment."""
    parsed = urlparse(url)
    # e.g. /help/import-data/ -> "import-data"
    slug = [p for p in parsed.path.strip("/").split("/") if p]
    name = slug[-1] if slug else "index"
    return OUTPUT_DIR / f"{name}.md"

def split(input_path: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    text = Path(input_path).read_text(encoding="utf-8")
    matches = list(SECTION_PATTERN.finditer(text))

    if not matches:
        print("No sections found — check the file format.")
        return

    written = 0
    for i, match in enumerate(matches):
        url = match.group(1)
        content_start = match.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[content_start:content_end].strip()

        md_content = f"---\nURL: {url}\n---\n\n{body}\n"

        out_path = url_to_path(url)
        out_path.write_text(md_content, encoding="utf-8")
        written += 1
        print(f"  wrote: {out_path}  ({url})")

    print(f"\nDone — {written} files written to '{output_dir}/'")

if __name__ == "__main__":
    split(INPUT_FILE, OUTPUT_DIR)
