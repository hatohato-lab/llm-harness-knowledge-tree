# 共通原本から各AI用の指示を作る

## 目次

1. 要点（一言と、根拠の段階と、使いどころ）
2. 仕組み（なぜ効くか）
3. 使い方（手順と例）
4. 試し方（最初の一歩と測り方）
5. 出典（公式・論文・元の記事までの道筋）
6. 試した記録（私が試した結果）
7. 関連（ほかの葉）

## 1. 要点（一言と、根拠の段階と、使いどころ）

一つの原本から、各AIが読む形式の指示を作る。

同期は、原本の変更を複数の出力へ反映する処理である。
Rulesyncは、各AI向けの設定を生成する外部ツールである。
dry-runは、変更予定だけを示す実行方法である。

根拠の段階：元の出典で確認。

対象は、推論を使って設計するモデルと、小型で高速な定型編集用モデルを併用する環境である。
両方へ渡す指示に、対象パス、行う操作、完了条件を一項目ずつ具体的に書く。
二つの開発ツールで同じリポジトリを直し、指示の保存形式が異なる場面に向く。
生成ツールを使うだけで、遵守率が上がるとは限らない。

## 2. 仕組み（なぜ効くか）

各AIの指示ファイルには、場所や書式の違いがある。
原本から生成すれば、手で何度も転記せずに済む。
生成先を別々に直すと、次の生成で差を失うことがある。
原本の編集と、生成結果の点検を一組にする。

[開発元README](https://raw.githubusercontent.com/dyoshikawa/rulesync/main/README.md)は、統一した規則から製品別設定を生成する処理を説明している。
そのため、変更の入力箇所を一つに固定できる、というのが更新漏れを減らす理由である。
これは運用上の見込みであり、モデルごとの品質改善を測った結果ではない。

Rulesyncの開発元は、変更予定と同期確認を用意している。
Claude Code標準の機能ではない。
異なるツールの指示の意味まで同一になる保証はない。

同じ生成方式は、スキルや接続設定にも応用される。
ただし、対応する機能と設定の意味は各AIで異なる。
この葉では、指示と手順の共有に対象を絞る。

## 3. 使い方（手順と例）

1. 指示ファイルだけを生成対象にする。
2. 原本と、各AI向けの出力先を決める。
3. 導入済みの版に合う説明を確認する。
4. dry-runで変更する場所を、原本で変更する本文を点検する。
5. 採用後は、原本だけを直して再生成する。
6. 同期確認と、各AIでの読込み確認を行う。

導入済みの試験場所で使う、変更予定の確認例を示す。

```text
rulesync generate --dry-run --targets claudecode,codexcli --features rules --json
```

--jsonは、出力を機械で読める形式にする指定である。
それだけでは書込みを止めない。
--checkは、原本と生成結果に差があるかを調べる指定である。
--dry-runと--checkは、別々に使う。
削除を伴う指定は、この例に含めない。

## 4. 試し方（最初の一歩と測り方）

後日の第一歩は、導入済みのRulesyncと、許可済みの独立した試験フォルダを使う45分の試行案である。
準備10分で、共通規則一件と出力先二つを用意する。[設定仕様](https://rulesync.dyoshikawa.com/guide/configuration)に従い、対象はrulesだけ、deleteはfalseとする。
次の15分で原本の規則を一度変更し、dry-runの予定を確認してから、試験フォルダだけへ生成する。
最後の20分で、生成された二つの本文を原本と照合し、別実行のcheckで残差を確かめる。
成功基準は原本の更新箇所1、変更の反映2/2、意味の食い違い0、checkの終了コード0である。
JSONの変更予定は対象パスの点検に使い、本文の一致は生成後のファイルで確かめる。AIの遵守率とは別の指標である。
未導入や設定の不一致で準備が10分を超えたら「前提未成立」で止め、紙上の転記だけを生成成功に数えない。
この調査では、この試行、導入、生成を実行していない。

## 5. 出典（公式・論文・元の記事までの道筋）

- 根拠の段階：元の出典で確認
- 公式・論文など：
  - [開発元README](https://raw.githubusercontent.com/dyoshikawa/rulesync/main/README.md)
  - [開発元のCLI仕様](https://rulesync.dyoshikawa.com/reference/cli-commands)
  - [本体の公開リポジトリ](https://github.com/dyoshikawa/rulesync)
  - [開発元が公開したREADME](https://github.com/dyoshikawa/rulesync#readme)
  - [generateコマンド実装](https://raw.githubusercontent.com/dyoshikawa/rulesync/main/src/cli/commands/generate.ts)
  - [生成処理の実装](https://raw.githubusercontent.com/dyoshikawa/rulesync/main/src/lib/generate.ts)
  - https://github.com/fcakyon/claude-codex-settings
  - https://github.com/contextmux/contextmux#getting-started
  - https://github.com/dyoshikawa/rulesync/releases/tag/v26.0.0
  - https://rulesync.dyoshikawa.com/guide/dry-run
  - https://github.com/affaan-m/ECC#whats-inside
  - [Claude Code側の読込み条件](https://code.claude.com/docs/en/memory#agentsmd)
  - [Rulesyncの命令一覧](https://rulesync.dyoshikawa.com/reference/cli-commands.html)
  - [Rulesyncの機能対応表](https://rulesync.dyoshikawa.com/reference/supported-tools.html)
  - [Rulesyncの設定項目](https://rulesync.dyoshikawa.com/guide/configuration.html)
  - [Claude Codeのプラグイン構成](https://code.claude.com/docs/en/plugins/create#plugin-layout)
- 確認の限界：
  - この調査では代表投稿のXページも取得を試みたが、本文を取得できなかった。
  - 保存箇所に「短縮先は未確認」とあるため、投稿からREADMEへ直接リンクされていたとは判定できない。
  - この欠落は残る。
  - 本体の導入・動作は未確認である。
  - 旧SNS投稿の短縮先未確認は残る。
  - ほかにも、確認できていない点が複数あります。

## 6. 試した記録（私が試した結果）

まだ試していない

## 7. 関連（ほかの葉）

- [共通指示を一つの原本に置く](共通指示を一つの原本に置く.md)
- [差分に絞って変更を監査する](../../05_評価と改善/04_失敗を調べる/差分に絞って変更を監査する.md)
