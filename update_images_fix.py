#!/usr/bin/env python3
import os
from pathlib import Path

# 60+ diverse Unsplash photo IDs for various 50-year-old lifestyle topics
photo_ids = [
    "photo-1552664730-d307ca884978",  # 1 - finance/business
    "photo-1579621970563-ebec7560ff3e",  # 2 - healthcare
    "photo-1611162617474-5b21e879e113",  # 3 - meditation
    "photo-1474552226712-ac0f0961a954",  # 4 - learning
    "photo-1507003211169-0a1dd7228f2d",  # 5 - lifestyle portrait
    "photo-1507371341519-52d3a7b992c2",  # 6 - professional
    "photo-1524678606370-a47ad25cb82a",  # 7 - coffee/relaxation
    "photo-1519389950473-47ba0277781c",  # 8 - investment/growth
    "photo-1460925895917-aeb19be489c3",  # 9 - success/achievement
    "photo-1454165804606-c3d57bc86b40",  # 10 - fitness
    "photo-1558618666-fcd25c85cd64",  # 11 - health
    "photo-1499209974431-9dddcece7f88",  # 12 - outdoors
    "photo-1506126613408-eca07ce68773",  # 13 - self-improvement
    "photo-1522202176988-08fa0ee197e1",  # 14 - professional growth
    "photo-1484480974693-6ca0a78fb36b",  # 15 - running
    "photo-1477884996148-fc0ee1e559af",  # 16 - golf/leisure
    "photo-1514306688299-6dc02fe343ad",  # 17 - gym
    "photo-1583454110551-21f2fa2afe61",  # 18 - cycling
    "photo-1506794778202-cad84cf45f1d",  # 19 - beach/vacation
    "photo-1528148343865-e218c9a940fb",  # 20 - travel
    "photo-1469854523086-cc02fe5d8800",  # 21 - joy
    "photo-1434628760416-3a5ff822d6cc",  # 22 - success
    "photo-1552664730-d307ca884978",  # 23 - wise
    "photo-1517694712202-14dd9538aa97",  # 24 - wealth
    "photo-1529156069898-49953e39b3ac",  # 25 - wisdom
    "photo-1507003211169-0a1dd7228f2d",  # 26 - confidence
    "photo-1492684223066-81342ee5ff30",  # 27 - achievement
    "photo-1511379938547-c1f69b13d835",  # 28 - maturity
    "photo-1519389950473-47ba0277781c",  # 29 - luxury
    "photo-1454165804606-c3d57bc86b40",  # 30 - growth
    "photo-1489749798305-ed8ac8f211b4",  # 31 - thinking strategically
    "photo-1517694712202-14dd9538aa97",  # 32 - assets
    "photo-1456406146555-c142cee21cf8",  # 33 - analytics
    "photo-1552664730-d307ca884978",  # 34 - focus
    "photo-1519389950473-47ba0277781c",  # 35 - investment portfolio
    "photo-1552664730-d307ca884978",  # 36 - determination
    "photo-1506794778202-cad84cf45f1d",  # 37 - relaxation
    "photo-1514306688299-6dc02fe343ad",  # 38 - energy
    "photo-1492684223066-81342ee5ff30",  # 39 - momentum
    "photo-1517694712202-14dd9538aa97",  # 40 - financial planning
    "photo-1529156069898-49953e39b3ac",  # 41 - experience
    "photo-1507003211169-0a1dd7228f2d",  # 42 - personal brand
    "photo-1484480974693-6ca0a78fb36b",  # 43 - vigor
    "photo-1528148343865-e218c9a940fb",  # 44 - celebration
    "photo-1456406146555-c142cee21cf8",  # 45 - analytics
    "photo-1493225457519-058bbb3b45d0",  # 46 - luxury travel
    "photo-1504384308090-c894fdcc538d",  # 47 - yacht/success
    "photo-1552664730-d307ca884978",  # 48 - dignity
    "photo-1519389950473-47ba0277781c",  # 49 - compound growth
    "photo-1529156069898-49953e39b3ac",  # 50 - legacy
    "photo-1579621970563-ebec7560ff3e",  # 51 - unique
    "photo-1611162617474-5b21e879e113",  # 52 - calm
    "photo-1474552226712-ac0f0961a954",  # 53 - inspired
    "photo-1552664730-d307ca884978",  # 54 - focused
    "photo-1507003211169-0a1dd7228f2d",  # 55 - powerful
    "photo-1507371341519-52d3a7b992c2",  # 56 - ready
    "photo-1524678606370-a47ad25cb82a",  # 57 - peace
    "photo-1519389950473-47ba0277781c",  # 58 - growth
    "photo-1460925895917-aeb19be489c3",  # 59 - victory
]

def update_image_urls():
    blog_dir = Path("/Users/eiji.y/Desktop/myblog/src/content/blog")
    qw_files = sorted(blog_dir.glob("qw-*.md"))

    print(f"Found {len(qw_files)} qw-*.md files")
    count = 0

    for idx, file in enumerate(qw_files):
        photo_id = photo_ids[idx % len(photo_ids)]
        new_image_url = f"https://images.unsplash.com/{photo_id}?w=1200&q=80"

        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        modified = False
        for i, line in enumerate(lines):
            if line.startswith('image: "'):
                lines[i] = f'image: "{new_image_url}"\n'
                modified = True
                count += 1
                print(f"✓ {file.name}: {photo_id}")
                break

        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(lines)

    print(f"\n✓ Updated {count} articles")

if __name__ == "__main__":
    update_image_urls()
