#!/usr/bin/env python3
"""
Convert a Jupyter notebook (.ipynb) to a Python script (.py).

- Code cells are written as normal Python code.
- Markdown/raw text cells are written as Python comments.

Usage:
    python ipynb_to_py.py notebook.ipynb
    python ipynb_to_py.py notebook.ipynb -o output.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def comment_block(text: str) -> str:
    """Convert plain text into Python comment lines."""
    lines = text.splitlines()
    if not lines:
        return "#"
    return "\n".join("# " + line if line.strip() else "#" for line in lines)


def normalize_source(source: Any) -> str:
    """Notebook cell source may be a string or list of strings."""
    if isinstance(source, list):
        return "".join(source)
    if isinstance(source, str):
        return source
    return ""


def convert_notebook(notebook_path: Path, output_path: Path) -> None:
    with notebook_path.open("r", encoding="utf-8") as f:
        notebook = json.load(f)

    cells = notebook.get("cells", [])

    output_parts: list[str] = [
        "#!/usr/bin/env python3",
        f"# Converted from {notebook_path.name}",
        "",
    ]

    for i, cell in enumerate(cells, start=1):
        cell_type = cell.get("cell_type", "")
        source = normalize_source(cell.get("source", ""))

        if cell_type == "markdown":
            output_parts.append(f"# --- Markdown cell {i} ---")
            output_parts.append(comment_block(source))
            output_parts.append("")

        elif cell_type == "raw":
            output_parts.append(f"# --- Raw cell {i} ---")
            output_parts.append(comment_block(source))
            output_parts.append("")

        elif cell_type == "code":
            output_parts.append(f"# --- Code cell {i} ---")
            if source.strip():
                output_parts.append(source.rstrip())
            else:
                output_parts.append("pass")
            output_parts.append("")

        else:
            output_parts.append(f"# --- Unknown cell type '{cell_type}' in cell {i} ---")
            output_parts.append(comment_block(source))
            output_parts.append("")

    output_path.write_text("\n".join(output_parts).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a Jupyter notebook (.ipynb) to a Python script (.py)."
    )
    parser.add_argument("input", type=Path, help="Path to the input .ipynb file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Path to the output .py file (default: same name as input)",
    )
    args = parser.parse_args()

    input_path = args.input
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if input_path.suffix.lower() != ".ipynb":
        raise ValueError("Input file must have a .ipynb extension")

    output_path = args.output or input_path.with_suffix(".py")
    convert_notebook(input_path, output_path)
    print(f"Wrote: {output_path}")


if __name__ == "__main__":
    main()
