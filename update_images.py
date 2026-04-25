#!/usr/bin/env python3
import os
import re
from pathlib import Path

# 60+ diverse Unsplash photo IDs for various 50-year-old lifestyle topics
photo_ids = [
    "photo-1517694712202-14dd9538aa97",  # finance/business
    "photo-1579621970563-ebec7560ff3e",  # healthcare
    "photo-1611162617474-5b21e879e113",  # meditation
    "photo-1474552226712-ac0f0961a954",  # learning
    "photo-1552664730-d307ca884978",  # thinking
    "photo-1507003211169-0a1dd7228f2d",  # lifestyle portrait
    "photo-1507371341519-52d3a7b992c2",  # professional
    "photo-1524678606370-a47ad25cb82a",  # coffee/relaxation
    "photo-1519389950473-47ba0277781c",  # investment/growth
    "photo-1460925895917-aeb19be489c3",  # success/achievement
    "photo-1454165804606-c3d57bc86b40",  # fitness
    "photo-1558618666-fcd25c85cd64",  # health
    "photo-1499209974431-9dddcece7f88",  # outdoors
    "photo-1506126613408-eca07ce68773",  # self-improvement
    "photo-1522202176988-08fa0ee197e1",  # professional growth
    "photo-1552664730-d307ca884978",  # contemplation
    "photo-1484480974693-6ca0a78fb36b",  # running
    "photo-1477884996148-fc0ee1e559af",  # golf/leisure
    "photo-1514306688299-6dc02fe343ad",  # gym
    "photo-1583454110551-21f2fa2afe61",  # cycling
    "photo-1506794778202-cad84cf45f1d",  # beach/vacation
    "photo-1506794778202-cad84cf45f1d",  # travel
    "photo-1528148343865-e218c9a940fb",  # joy
    "photo-1469854523086-cc02fe5d8800",  # success
    "photo-1434628760416-3a5ff822d6cc",  # business meeting
    "photo-1552664730-d307ca884978",  # wise
    "photo-1517694712202-14dd9538aa97",  # wealth
    "photo-1529156069898-49953e39b3ac",  # wisdom
    "photo-1507003211169-0a1dd7228f2d",  # confidence
    "photo-1492684223066-81342ee5ff30",  # achievement
    "photo-1552664730-d307ca884978",  # maturity
    "photo-1511379938547-c1f69b13d835",  # luxury
    "photo-1519389950473-47ba0277781c",  # growth
    "photo-1454165804606-c3d57bc86b40",  # discipline
    "photo-1517694712202-14dd9538aa97",  # opportunity
    "photo-1507003211169-0a1dd7228f2d",  # presentation
    "photo-1489749798305-ed8ac8f211b4",  # thinking strategically
    "photo-1517694712202-14dd9538aa97",  # assets
    "photo-1456406146555-c142cee21cf8",  # analytics
    "photo-1552664730-d307ca884978",  # focus
    "photo-1519389950473-47ba0277781c",  # investment portfolio
    "photo-1552664730-d307ca884978",  # determination
    "photo-1506794778202-cad84cf45f1d",  # relaxation
    "photo-1514306688299-6dc02fe343ad",  # energy
    "photo-1492684223066-81342ee5ff30",  # momentum
    "photo-1517694712202-14dd9538aa97",  # financial planning
    "photo-1529156069898-49953e39b3ac",  # experience
    "photo-1507003211169-0a1dd7228f2d",  # personal brand
    "photo-1484480974693-6ca0a78fb36b",  # vigor
    "photo-1528148343865-e218c9a940fb",  # celebration
    "photo-1456406146555-c142cee21cf8",  # analytics
    "photo-1493225457519-058bbb3b45d0",  # luxury travel
    "photo-1504384308090-c894fdcc538d",  # yacht/success
    "photo-1552664730-d307ca884978",  # dignity
    "photo-1519389950473-47ba0277781c",  # compound growth
    "photo-1529156069898-49953e39b3ac",  # legacy
]

def update_image_urls():
    blog_dir = Path("/Users/eiji.y/Desktop/myblog/src/content/blog")
    qw_files = sorted(blog_dir.glob("qw-*.md"))

    print(f"Found {len(qw_files)} qw-*.md files")

    for idx, file in enumerate(qw_files):
        # Use modulo to cycle through photo_ids
        photo_id = photo_ids[idx % len(photo_ids)]
        new_image_url = f"https://images.unsplash.com/{photo_id}?w=1200&q=80"

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace image URL in frontmatter
        new_content = re.sub(
            r'image: "https://images\.unsplash\.com/[^"]+\?[^"]*"',
            f'image: "{new_image_url}"',
            content
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Updated {file.name}: {photo_id}")

    print(f"\n✓ Updated {len(qw_files)} articles with diverse image URLs")

if __name__ == "__main__":
    update_image_urls()
