# 非機能要件 (nonrequirements)

## デプロイ対象リージョン
- Azure 東日本（Japan East）をターゲットにデプロイする。

## ホスティング
- Azure Functions の Consumption Plan を使用する。

## ランタイム
- Python 3.11 を使用する。

## 性能目標（SLO 候補）
- 例: p95 < 200ms を目安とする（合意が必要）。

## タイムアウト
- Consumption Plan の既定値を参照し、必要に応じに短縮を検討する。

## スケーリング
- Consumption Plan の自動スケールに依存する。

## 監視・ロギング
- Application Insights によりリクエスト、例外、カスタムイベントを収集する。

## CORS / セキュリティ
- 初期は認証不要で運用するが、HTTPS を必須とする。
- 将来的に API キーや認証を導入可能とする。

## CI/CD / デプロイワークフロー
- GitHub Actions を推奨し、ビルド・テスト・デプロイを自動化する。

## IaC（Infrastructure as Code）
- Bicep または Terraform を推奨する。

## 運用観点
- ログ保持期間、エラー率・遅延のアラート設定、インシデント対応手順を定義する。

## 未決事項・選択肢
- p95 の目標値（200ms vs 500ms 等）。
- タイムアウトの具体値。
- CORS の許可リスト（ドメイン指定）。
- レート制限の閾値と方式（IP ベース/キー ベース）。
- ログ保持期間（30/90/365日）とコスト要件。
- IaC の最終選定（Bicep vs Terraform）。