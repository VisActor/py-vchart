まず、オープンソースへの貢献に参加するというあなたの行動に拍手を送ります 👍🏻。そして、VisActor コミュニティに参加し、このオープンソースプロジェクトに貢献してくれることに心から感謝します。

## py-vchart 貢献ガイド

py-vchart チームは通常、GitHub 上で開発と issue の管理を行っています。[GitHub サイト](https://github.com/)を開き、右上の `Sign up` ボタンをクリックして、自分のアカウントを登録し、オープンソースの旅の第一歩を踏み出しましょう。

[py-vchart リポジトリ](https://github.com/VisActor/py-vchart)には、すべてのオープンソース貢献者向けの[ガイド](https://github.com/VisActor/py-vchart/blob/develop/CONTRIBUTING.zh-CN.md)があり、バージョン管理、ブランチ管理などの内容が紹介されています。**数分間かけて読んで理解してください**。

## 最初の Pull Request

### Step0：Git のインストール

Git は、ソフトウェア開発プロジェクトのコード変更を追跡および管理するためのバージョン管理システムです。開発者は、コードの履歴を記録および管理し、チーム協力、コードのバージョン管理、コードのマージなどの操作を容易に行うことができます。Git を使用することで、各ファイルの各バージョンを追跡し、異なるバージョン間で簡単に切り替えたり比較したりすることができます。また、ブランチ管理機能を提供しており、複数の並行開発タスクを同時に行うことができます。

- Git 公式サイトにアクセスします：<https://git-scm.com/>
- 最新バージョンの Git インストーラーをダウンロードします。
- ダウンロードしたインストーラーを実行し、インストールウィザードの指示に従ってインストールします。
- インストールが完了したら、コマンドラインで `git version` コマンドを使用して、インストールが成功したことを確認できます。

### Step1：プロジェクトの Fork

- まず、このプロジェクトを fork する必要があります。[py-vchart プロジェクトページ](https://github.com/VisActor/py-vchart)にアクセスし、右上の Fork ボタンをクリックします。

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/fork.PNG)

- あなたの GitHub アカウントに、xxxx(あなたの GitHub ユーザー名)/py-vchart というプロジェクトが表示されます。
- ローカルコンピュータで以下のコマンドを使用して、py-vchart フォルダを取得します。

```
// ssh
git clone git@github.com:xxxx(你的github用户名)/py-vchart.git
// https
git clone https://github.com/xxxx(你的github用户名)/py-vchart.git
```

### Step2：プロジェクトコードの取得

- py-vchart フォルダに移動し、py-vchart のリモートアドレスを追加します。

```
git remote add upstream https://github.com/VisActor/py-vchart.git
```

- py-vchart の最新ソースコードを取得します。

```
git pull upstream develop
```


### Step3：ブランチの作成

- さて、これでコードの貢献を始めることができます。py-vchart のデフォルトブランチは develop ブランチです。機能開発、バグ修正、ドキュメント作成のいずれの場合も、新しいブランチを作成してから develop ブランチにマージしてください。以下のコードを使用してブランチを作成します。

```
// 機能開発ブランチの作成
git checkout -b feat/xxxx

// 問題修正開発ブランチの作成
git checkout -b fix/xxxx

// ドキュメント、デモブランチの作成 
git checkout -b docs/add-funnel-demo
```


ここでは、ドキュメント修正ブランチ `docs/add-funnel-demo` を作成したと仮定します。

- これで、ブランチ上でコードを変更することができます。
- コードを追加したと仮定し、コードをコミットします。
- `git commit -a -m "docs: add custom funnel demo and related docs"` 。VisActor のコミットメッセージは [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 規範に従っています。

  - `<type>[optional scope]: <description>`
  - 一般的に使用される `type` には、docs（ドキュメント、ログの修正）、feat（新機能）、fix（問題修正）、refactor（コードリファクタリング）などがあります。実際の状況に応じて選択してください。
  - `description` は、簡潔で正確な英語で記述してください。

### Step4：変更のマージ

- 一般的な問題として、リモートの upstream (@visactor/py-vchart) に新しい更新があると、Pull Request を送信する際に衝突が発生することがあります。そのため、送信する前に、リモートの他の開発者のコミットと自分のコミットをマージすることができます。以下のコードを使用して develop ブランチに切り替えます。

```
git checkout develop
```

- 以下のコードを使用して、リモートの最新コードを取得します。

```
git pull upstream develop
```

- 自分の開発ブランチに切り替えます。

```
git checkout docs/add-funnel-demo
```

- develop のコミットを自分のブランチにマージします。

```
git rebase develop
```

- 更新されたコードを自分のブランチにプッシュします。

```
git push origin docs/add-funnel-demo
```


### Step5：Pull Request の送信

あなたの GitHub コードリポジトリページで `Compare & pull request` ボタンをクリックすることができます。

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR.png)

または、`contribute` ボタンを使用して作成することもできます。

<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR-2.png">
</div>

テンプレートに従って、今回の送信内容を記入します。

- この修正のタイプを選択します。
<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-checklist.png">
</div>

- 関連する issue を記入します。
<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/related-issue.png">
</div>

- 複雑な変更がある場合は、背景と解決策を説明してください。
<div align='center'>
<img style="height:120px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-background.png">
</div>

関連情報を記入したら、Create pull request をクリックして送信します。

## **py-vchart オープンソース貢献の旅へようこそ**

"**good first issue**" は、オープンソースコミュニティで一般的に使用されるラベルで、新しい貢献者が入門するのに適した問題を見つけるのに役立ちます。

py-vchart の入門問題は、[issue リスト](https://github.com/VisActor/py-vchart/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) で確認できます。現在は以下の 2 種類があります。

- Demo ケースの作成
- 簡単な機能開発

もしあなたが現在**時間と意欲があり**、コミュニティへの貢献に参加したい場合は、issue の中から **good first issue** を探し、興味があり、自分に適したものを選んで引き受けてください。

あなたはきっと最後までやり遂げる人だと信じています。ですから、issue を理解して引き受けることを決めたら、issue の下にメッセージを残して、皆に知らせてください。

### Demo Task 開発ガイド

未記載...

## VisActor コミュニティへの参加

VisActor へのコード貢献の他に、コミュニティをさらに繁栄させるための他の活動にも参加することをおすすめします。たとえば、

1. プロジェクトの発展や機能計画などについて提案をする。
2. 記事やビデオを作成し、講演会を開催して VisActor を宣伝する。
3. プロモーション計画を作成し、チームと一緒に実行する。

VisActor も、コミュニティ建設に参加する学生たちの成長を支援するために努力しています。以下のような支援を提供する予定です（これに限定されず、皆さんからの更多の提案を期待しています）。

1. VisActor をベースにしたデータ可視化開発トレーニングを提供し、参加する学生がプログラミングスキル、可視化理論、アーキテクチャ設計などの複数の分野で迅速に成長するのを支援します。
2. 定期的に「コード貢献賞」と「コミュニティプロモーション賞」を選出します。
3. コミュニティメンバーをオープンソースイベントに参加させます。

## よくある質問

未記載...