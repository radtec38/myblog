#!/usr/bin/env python3
import re
from pathlib import Path

# Map articles to affiliate links based on content
affiliate_links = {
    "mote-real-01": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEYL9W+1WP2+15QHIA" rel="nofollow">【PR】メンズコスメ - モテる男の必須アイテム</a>',
    "mote-real-02": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】証券口座を開く - インデックス投資を始める</a>',
    "mote-real-03": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】高配当株投資 - 月10万円の不労所得</a>',
    "mote-real-04": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEYL9W+1WP2+15QHIA" rel="nofollow">【PR】UNIQLOでメンズファッション - 可愛いと言われるコーデ</a>',
    "mote-real-05": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEAKZ6+1WP2+1HL85U" rel="nofollow">【PR】フィットネスアプリ - 5kg痩せるプログラム</a>',
    "mote-real-06": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】キャリアコーチング - 年収100万アップの秘訣</a>',
    "mote-real-07": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEYL9W+1WP2+15QHIA" rel="nofollow">【PR】結婚相談所 - 22年続く関係の作り方</a>',
    "mote-real-08": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEAKZ6+1WP2+1HL85U" rel="nofollow">【PR】ウイスキー・ハイボール - 大人の嗜好品</a>',
    "mote-real-09": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】ネット証券 - 両学長推奨の投資方法</a>',
    "mote-real-10": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】資産運用アプリ - 数千万の資産を築く</a>',
    "mote-real-11": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】AI投資ツール - 握力を鍛える</a>',
    "mote-real-12": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEYL9W+1WP2+15QHIA" rel="nofollow">【PR】買ってよかったもの - Amazon ベストセラー</a>',
    "mote-real-13": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEAKZ6+1WP2+1HL85U" rel="nofollow">【PR】育毛剤・薄毛対策 - フィンペシア体験</a>',
    "mote-real-14": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】AI活用ツール - 副業で月10万円</a>',
    "mote-real-15": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEAKZ6+1WP2+1HL85U" rel="nofollow">【PR】ロードバイク - 5年通勤の経験談</a>',
    "mote-real-16": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】格安SIM・通信費削減 - 月290円の秘訣</a>',
    "mote-real-17": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】医療保険 - 確率思考で無駄を削減</a>',
    "mote-real-18": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】資産管理アプリ - 5000万円の管理術</a>',
    "mote-real-19": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEYL9W+1WP2+15QHIA" rel="nofollow">【PR】恋愛心理学 - 自然体の関係を築く</a>',
    "mote-real-20": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】転職エージェント - 就職氷河期を突破</a>',
    "mote-real-21": '<a href="https://px.a8.net/svt/ejp?a8mat=4B1SPS+FEW0KY+1WP2+15QHIA" rel="nofollow">【PR】オンライン講座 - 最下位から首席へ</a>',
}

blog_dir = Path("/Users/eiji.y/Desktop/myblog/src/content/blog")

for file in sorted(blog_dir.glob("mote-real-*.md")):
    basename = file.stem  # e.g., "mote-real-01-why-i-get-liked"
    base_num = "-".join(basename.split("-")[:2])  # e.g., "mote-real-01"

    if base_num not in affiliate_links:
        print(f"⚠ No affiliate link for {basename}")
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if affiliate link already exists
    if '<a href="https://px.a8.net' in content:
        print(f"✓ Already has affiliate link: {basename}")
        continue

    # Add affiliate link before the last closing tag
    affiliate_html = f'\n\n---\n\n## 関連リンク\n\n{affiliate_links[base_num]}\n'

    # Insert before the last --- if it exists, otherwise at the end
    if content.rstrip().endswith('---'):
        content = content.rstrip()[:-3] + affiliate_html
    else:
        content = content.rstrip() + affiliate_html

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Added affiliate link: {basename}")

print("\n✓ Complete - Affiliate links added to mote-real articles")
