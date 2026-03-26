#!/usr/bin/env python3
# Extract plain text from an ODT file.
#
# Usage:
#   tools/odt2text.py file.odt

import re
import sys
import zipfile

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} file.odt", file=sys.stderr)
    sys.exit(1)

path = sys.argv[1]

with zipfile.ZipFile(path) as z:
    content = z.read("content.xml").decode()

text = re.sub(r"<[^>]+>", " ", content)
text = re.sub(r" +", " ", text)
print(text.strip())
