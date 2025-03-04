<p align="center">
    <img src="https://github.com/VisActor/.github/raw/main/profile/logo_500_200_dark.svg" alt="pyvchart logo" width=200 height=200 />
</p>
<h1 align="center">pyvchart</h1>
<p align="center">
    <em>Python ❤️ VChart = pyvchart</em>
</p>
<p align="center">
    <a href="https://github.com/pyvchart/pyvchart/actions">
        <img src="https://github.com/pyvchart/pyvchart/actions/workflows/python-app.yml/badge.svg" alt="Github Actions Status">
    </a>
    <a href="https://codecov.io/gh/pyvchart/pyvchart" >
        <img src="https://codecov.io/gh/pyvchart/pyvchart/branch/main/graph/badge.svg?token=q4Op7n64fK" alt="Codecov"/>
    </a>
</p>
<p align="center">
    <a href="https://github.com/pyvchart/pyvchart/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

[日本語 README](README.md) | [英語 README](README.en.md) | [日本語（にほんご）README](README.jp.md)

## 📣 はじめに

[VisActor/VChart](https://github.com/VisActor/VChart) は、字節ジャンプトがオープンソース化したビジュアル化ソリューション VisActor のコアチャートコンポーネントライブラリです。これはビジュアル化文法ライブラリ VGrammar とレンダリングエンジン VRender を基に構築されており、データの表示だけでなく、ナレーシナリオ向けのアニメーション編成、豊富なインタラクティブ機能、カスタマイズ可能なチャートスタイルもサポートしています。シンプルで使いやすい設定により、ユーザーの学習コストが大幅に削減されます。一方、Python は表現力豊かな言語であり、データ処理やAIなどの分野で非常に適しています。データ分析やモデリングがデータビジュアライゼーションと組み合わさったときに、[pyecharts](https://github.com/pyecharts/pyecharts) と [pyvchart](https://github.com/pyvchart/pyvchart) が生まれました。

## ✨ 特徴

* [pyecharts](https://github.com/pyecharts/pyecharts) に似た API 設計、スムーズでフローリングした使用感、メソッドチェーンのサポート
* VChart のすべてのチャートを含む、必要なものが揃っている
* Jupyter Notebook、JupyterLab (**近日公開予定**) などの主流の Notebook 環境をサポート
* Flask、Sanic、Django (**近日公開予定**) などの主流の Web フレームワークへの容易な統合
* 高度に柔軟な設定オプション、美しいチャートを簡単に作成できる
* 開発者を手助けするための詳細なドキュメントと例

## 🔰 インストール

**pip インストール**
```shell
# インストール
# 【❕注意❕】現在、PyPI に長期間メンテナンスされていない同名のプロジェクトが存在するため、wheel を PyPI にアップロードすることができません。
$ pip install pyvchart -U

# 一時的な解決策
$ pip install git+https://github.com/pyvchart/pyvchart@v0.1.0
```


**ソースコードインストール**
```shell
# バージョン v1 以上をインストール
$ git clone https://github.com/pyvchart/pyvchart.git
$ cd pyvchart
$ pip install -r requirements.txt
$ python setup.py install
```


## 📝 使用方法

使用例はここにあります：[Examples](https://github.com/pyvchart/chart-examples)

## ⛏ コード品質

### ユニットテスト

```shell
$ pip install -r test/requirements.txt
$ make
```


### 統合テスト

GitHub Actions を使用して継続的インテグレーション環境を構築しています。

### コードスタイル

[flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/), [pylint](https://www.pylint.org/) を使用してコード品質を向上させています。

## 😉 作者

pyvchart は以下の開発者が開発およびメンテナンスを行っています

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

他の貢献者の情報は [pyvchart/graphs/contributors](https://github.com/pyvchart/pyvchart/graphs/contributors) で確認できます

## 💡 貢献

より多くの開発者が pyvchart の開発に参加することを期待しています。PR のレビューを迅速に行い、タイムリーな返信を提供しますが、PR を送信する際には以下の点に注意してください

1. すべてのユニットテストがパスし、新しい機能の場合はユニットテストを追加してください
2. 開発ガイドラインに従い、コードを black および isort でフォーマットしてください（`$ pip install -r requirements-dev.txt` を実行してください）
3. 必要に応じて関連ドキュメントを更新してください

また、pyvchart に多くの例を提供してドキュメントを充実させることも歓迎します。ドキュメントプロジェクトは [pyvchart/website](https://github.com/pyvchart/website) にあります

## 📃 ライセンス

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)