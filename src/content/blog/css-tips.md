---
title: "知っておくべきモダンCSSテクニック10選"
description: "CSSの最新機能を活用して、より効率的でメンテナブルなスタイルシートを書くためのテクニックを紹介します。"
pubDate: 2026-04-10
tags: ["CSS", "フロントエンド", "デザイン"]
image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1200&q=80"
---

CSS は進化を続けており、以前はJavaScriptやSassが必要だった処理も、現代のCSSだけで実現できるようになっています。今回はすぐに使えるモダンCSSテクニックを10個ご紹介します。

## 1. カスタムプロパティ（CSS変数）

デザイントークンの管理に欠かせないのがCSS変数です。テーマの一元管理やダイナミックな値の変更が簡単になります。

```css
:root {
  --color-primary: #4f46e5;
  --spacing-base: 1rem;
}

.button {
  background: var(--color-primary);
  padding: var(--spacing-base);
}
```

## 2. CSS Grid でのレイアウト

Flexboxと並んでGridはモダンレイアウトの主役です。複雑な2次元レイアウトをシンプルに表現できます。

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}
```

`auto-fill`と`minmax`を組み合わせると、レスポンシブなグリッドをメディアクエリなしで実現できます。

## 3. clamp() による流体タイポグラフィ

`clamp()`を使えば、画面幅に応じてフォントサイズを滑らかに変化させられます。

```css
h1 {
  font-size: clamp(1.5rem, 4vw + 1rem, 3rem);
}
```

最小値・推奨値・最大値の3つを指定するだけで、どの画面サイズでも最適なテキストサイズになります。

## 4. :is() セレクター

複数のセレクターに同じスタイルを適用する際、`:is()`を使うとコードがすっきりします。

```css
/* 従来 */
h1 a, h2 a, h3 a { color: inherit; }

/* :is()を使用 */
:is(h1, h2, h3) a { color: inherit; }
```

## 5. コンテナクエリ

メディアクエリがビューポートサイズを基準にするのに対し、コンテナクエリはコンテナ要素のサイズを基準にスタイルを変更できます。コンポーネント指向の開発と非常に相性が良い機能です。

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

これらのテクニックを活用して、より保守しやすいCSSを書いていきましょう。
