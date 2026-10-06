# MCPとCLIを作業ごとに使い分ける

## 目次

1. 要点（一言と、根拠の段階と、使いどころ）
2. 仕組み（なぜ効くか）
3. 使い方（手順と例）
4. 試し方（最初の一歩と測り方）
5. 出典（公式・論文・元の記事までの道筋）
6. 試した記録（私が試した結果）
7. 関連（ほかの葉）

## 1. 要点（一言と、根拠の段階と、使いどころ）

MCPは、AIと外部の道具をつなぐ通信規格です。
CLIは、文字の命令で道具を操作する方式です。

同じ仕事の入力と出力を比べ、合う入口を選びます。

根拠の段階：公式で確認

賢いモデルは方式の比較に向きます。
軽いモデルは決まった読取り手順に向きます。
指示は、対象と必要な出力を具体的に書きます。
既存の道具を使う検索、集計、状態確認に向きます。

根拠は仕組みや提供機能の確認です。
この環境での効果と動作は、まだ測っていません。

## 2. 仕組み（なぜ効くか）

CLIは、既存の命令と出力の絞込みを利用できます。
MCPは、道具名と入力の形をAIへ渡せます。
同じ機能でも、設定の手間や返答量は異なります。
公式は、使えるCLIの併用を勧めています。
常にCLIが速い、安いという保証ではありません。

ファイル本文だけなら、直接読む方法も候補です。
Obsidianの本文読取と画面操作は別の仕事です。
接続を足す前に、追加で必要な機能を確かめます。

[公式のCLI併用の助言](https://code.claude.com/docs/en/costs#reduce-mcp-tool-overhead)は、CLIなら道具ごとの一覧を文脈へ追加せずに使えると説明しています。このため、既存CLIで必要な項目だけ返せる作業では、読ませる説明と結果を減らせます。これは文脈量に関する仕組みで、速度や料金の実測結果ではありません。

## 3. 使い方（手順と例）

以下は将来の試行手順です。今回は実行していません。

1. 一つの読取り作業と正解を決めます。
2. 直接読取、CLI、MCPの候補を並べます。
3. 使える操作、必要な入力、返る形を比べます。
4. 同じ項目だけを取得する手順を書きます。
5. 一つの方式を選び、選んだ理由を記録します。

指示や設計の例です。

```text
公開の試験資料について、題名と更新日だけが必要です。
直接読取、CLI、MCPの三案を比べてください。
今ある機能と、追加設定が必要な機能を分けてください。
比較表だけを作ってください。
```

## 4. 試し方（最初の一歩と測り方）

最初の一歩は、準備10分、比較20分、検算10分の計40分です。
手元で架空の資料を3件用意し、各件を題名・更新日・本文の3項目にします。
必要な答えは題名と更新日の計6値として、先に正解表を書きます。
全項目を返す案と、題名・更新日だけ返す案を紙上で比較します。
直接読取、CLI、MCPそれぞれについて、絞込みの位置と追加設定の有無を記します。

成功基準は、必要な値が6/6一致し、不要な本文の返却が0件であることです。
返答の文字数と、追加設定が必要な候補数も記録します。
既存環境で実行できない候補は「未実行」とし、速度や費用の優劣を付けません。
この初回は入出力の設計を検証します。実際の接続時間や削減率は測りません。

## 5. 出典（公式・論文・元の記事までの道筋）

- 根拠の段階：公式で確認
- 公式・論文など：
  - [投稿が紹介したAnthropicの記事](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)
  - [CLI併用を説明する公式文書](https://code.claude.com/docs/en/costs#reduce-mcp-tool-overhead)
  - [Claude Code本体の公式配布案内](https://code.claude.com/docs/en/overview)
  - [ObsidianのLocal REST API提供元](https://github.com/coddingtonbear/obsidian-local-rest-api)
  - [Obsidian用スキル提供元](https://github.com/kepano/obsidian-skills)
  - [ObsidianスキルのREADME本文](https://raw.githubusercontent.com/kepano/obsidian-skills/main/README.md)
  - [sem-aiの配布元](https://github.com/semaphoreio/sem-ai)
  - [Semaphoreによるsem-aiの説明](https://docs.semaphore.io/using-semaphore/ai/sem-ai)
  - [sem-aiのコマンド資料](https://docs.semaphore.io/reference/sem-ai-cli)
  - [Claude Codeの推奨手順](https://code.claude.com/docs/en/best-practices#use-cli-tools)
  - [権限の設定](https://code.claude.com/docs/en/permissions)
  - [Claude Code costs](https://code.claude.com/docs/en/costs)
  - [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
  - [Claude Code公式更新履歴](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md)
  - [Claude CodeのMCP接続](https://code.claude.com/docs/en/mcp)
- 確認の限界：
  - 記事と公式文書は同じ提供元の別資料として照合したもので、記事中の実リンクと断定しません。
  - 数値や個別製品の効果は、この投稿だけでは未確認。
  - 本体は調査時未確認です。
  - 文字列の存在は、接続成功や効果の実証ではありません。
  - 個別アプリの対応も、一般のMCP仕様だけでは保証しません。

## 6. 試した記録（私が試した結果）

まだ試していない

## 7. 関連（ほかの葉）

- [道具の説明を必要時に読む](../../03_文脈と記憶/10_拡張と読込み/道具の説明を必要時に読む.md)
- [接続の失敗を段階で切り分ける](接続の失敗を段階で切り分ける.md)
- [読む範囲を決めて原文を探す](../../03_文脈と記憶/07_必要な情報の検索/読む範囲を決めて原文を探す.md)
