#!/usr/bin/env python3
from pathlib import Path
import re

# Map qw articles to mote-real articles by theme
qw_to_mote_real = {
    1: [25, 9, 10, 2],      # qw-01 (Side FIRE) → mote-real-25,09,10,02
    2: [4],                 # qw-02 (Fashion) → mote-real-04
    3: [22],                # qw-03 (IDECO) → mote-real-22
    5: [5],                 # qw-05 (Diet) → mote-real-05
    6: [6],                 # qw-06 (Side job) → mote-real-06
    10: [13],               # qw-10 (Hair) → mote-real-13
    14: [2, 18],            # qw-14 (Index) → mote-real-02,18
    15: [15],               # qw-15 (Training) → mote-real-15
    16: [16, 25],           # qw-16 (FIRE steps) → mote-real-16,25
    17: [2, 18],            # qw-17 (Stocks) → mote-real-02,18
    18: [3],                # qw-18 (Dividends) → mote-real-03
    20: [20],               # qw-20 (Job change) → mote-real-20
    23: [23],               # qw-23 (Tax) → mote-real-22
}

blog_dir = Path("/Users/eiji.y/Desktop/myblog/src/content/blog")

# Get mote-real file mapping
mote_real_files = {}
for f in blog_dir.glob("mote-real-*.md"):
    num = int(f.stem.split("-")[2])
    mote_real_files[num] = f.stem

# Add internal links to qw articles
for file in sorted(blog_dir.glob("qw-*.md")):
    stem = file.stem  # e.g., "qw-01-sidefire-50s"
    qw_num = int(stem.split("-")[1])  # Extract number

    if qw_num not in qw_to_mote_real:
        continue

    mote_real_nums = qw_to_mote_real[qw_num]

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if internal links already exist
    if '/blog/mote-real-' in content:
        print(f"✓ Already has mote-real links: qw-{qw_num:02d}")
        continue

    # Create internal links section
    links_html = "\n\n---\n\n## 関連記事\n\n"
    for mote_num in mote_real_nums:
        if mote_num in mote_real_files:
            mote_name = mote_real_files[mote_num]
            links_html += f"- [{mote_name.replace('mote-real-', '').replace('-', ' ')}](/blog/{mote_name}/)\n"

    # Insert before last --- if exists
    if content.rstrip().endswith('---'):
        content = content.rstrip()[:-3] + links_html
    else:
        content = content.rstrip() + links_html

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Added {len(mote_real_nums)} mote-real links: qw-{qw_num:02d}")

print("\n✓ Internal links added to qw articles")
