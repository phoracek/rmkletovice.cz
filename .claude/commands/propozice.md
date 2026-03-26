Create a new `letove-akce` article for a propozice ODT file.

## Usage

```
/propozice content/docs/<filename>.odt
```

## Steps

1. **Convert ODT to PDF** using `tools/odt2pdf.sh <odt-path>`.

2. **Extract event date** from the ODT using `tools/odt2text.py <odt-path>`. Parse the plain text to find the event date (e.g. "11. 4. 2026").

3. **Find the most recent matching article** in `content/letove-akce/` that shares the same slug pattern (e.g. for `oblastni-prebor-zaku-2026-*` look for `oblastni-prebor-zaku-2025-*`, etc.). Read that file as a reference for structure and metadata.

4. **Determine the new article filename**: `YYYYMMDD-<slug>.rst` where the date comes from the event date extracted in step 2 and the slug is derived from the ODT filename (strip the year prefix from the directory part, e.g. `oblastni-prebor-zaku-2026-letovice-propozice.odt` → slug `oblastni-prebor-zaku-2026-letovice`).

5. **Write the new `.rst` article** in `content/letove-akce/`, following the reference file's structure:
   - Title and underline
   - `:category: Letové akce`
   - `:action:` dict with `date`, `place`, `map` (copy from reference), and `documents` listing only the Propozice entry (with `odt` and `pdf` formats). Do **not** include a `Výsledková listina` entry — it does not exist yet.

6. **Commit** both the new `.rst` file and the generated PDF (and the source ODT if not yet tracked) with `git commit -s`.
