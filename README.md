# calc-api-hands-on

簡単な掛け算 / 割り算 API のサンプル (Azure Functions, Python 3.11)

- エンドポイント: `/multiply`, `/divide` (GET/POST)
- レスポンス: JSON（API）および簡易 HTML（ブラウザ）

ローカル実行:
1. Python 3.11 の仮想環境を作成
2. `pip install -r requirements.txt`
3. Azure Functions Core Tools を使用して `func start` で実行

*注意*: `local.settings.json` はコミットせず、必要な値を `local.settings.json` に追加してください。