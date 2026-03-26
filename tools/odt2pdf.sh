#!/usr/bin/env bash
# Convert ODT files to PDF using LibreOffice.
# Output PDFs are placed alongside the source files.
#
# Usage:
#   tools/odt2pdf.sh file1.odt [file2.odt ...]
#   tools/odt2pdf.sh content/docs/*.odt

set -euo pipefail

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 file1.odt [file2.odt ...]" >&2
    exit 1
fi

for file in "$@"; do
    if [[ ! -f "$file" ]]; then
        echo "Error: file not found: $file" >&2
        exit 1
    fi
    if [[ "${file##*.}" != "odt" ]]; then
        echo "Error: not an ODT file: $file" >&2
        exit 1
    fi
done

libreoffice --headless --convert-to pdf "$@" --outdir "$(dirname "${1}")"
