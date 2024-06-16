## EngLDiary-bot
このEngLDiary-botは英語学習を目的として、日々の英語日記を管理するbotです。<br>日々の体験を英語で振り返り、体験と紐づいた英語学習体験を届けます。<br>現在の機能としては登録、検索、表示のみです。

## 使用方法
詳細は下記の参考資料「Discord Botを簡単お手軽開発する方法」をご参照ください。<br>
1. このリポジトリをGithub Codespacesで開く。
2. .envファイルをプロジェクトルートに作成し、中身のtoken情報をDiscordのアクセストークンに書き換える。
3. プロジェクトルートにいる状態で、「python main.py」を実行する。
4. discord サーバーで下記のコマンドを打ち込む。

このような手順でbotが利用可能になります。

## コマンド説明

### /add 日記をデータベースに保存する
```
/add <input sentence>
```
![add image](https://private-user-images.githubusercontent.com/117506621/340078858-019dfd88-de83-4474-b884-aaacf264e64a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1Mjg3ODksIm5iZiI6MTcxODUyODQ4OSwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODU4LTAxOWRmZDg4LWRlODMtNDQ3NC1iODg0LWFhYWNmMjY0ZTY0YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTAxMjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mOTlkZDhmNjUwNDlhNTYxNTgxNWE3YjQ5M2RkZGJkMTdkMTk3OGJlOWI2OWJlY2JlMzUwZTExYjc4YTY2YmQ1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9._ivQNTk2Mk3cuM3-hXi8RByIsZKRic9bb6NzH8qo7ZE)
### /showme_all_contents データベースのすべての日記エントリを表示する
```
/showme_all_contents
```
![showme_all_contents image](https://private-user-images.githubusercontent.com/117506621/340078871-e6663886-9e73-42ed-ae56-646b82f0c396.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MjkxNjIsIm5iZiI6MTcxODUyODg2MiwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODcxLWU2NjYzODg2LTllNzMtNDJlZC1hZTU2LTY0NmI4MmYwYzM5Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTA3NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNDRhNWI3MTJlNDEwY2U5MzM0MDdlZWY0ODQ3NDQ0NWM0ZmQwNDUzZmM2ODg2ZmQ2Yzg4ODMyMTAwY2Y3NTI5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.JpgNnks8r7K3RAO3rHZ1Pi5zOEtKLGcdLpgRc34gFI4)
### /fl 入力文字列を含む日記エントリを見つける
```
/fl <input letters>
```
![fl image](https://private-user-images.githubusercontent.com/117506621/340078877-fcf58e3e-0519-4db1-8c52-cc5a709cc786.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MjkxNjIsIm5iZiI6MTcxODUyODg2MiwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODc3LWZjZjU4ZTNlLTA1MTktNGRiMS04YzUyLWNjNWE3MDljYzc4Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTA3NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ODNjNjNjMTM3N2VlNWJkZDYyMGQ3YTJjMDg4ZDY0OTljZDRmOWQwYTA0NjhjNWI2ZTM2MTlhYzAwOTdmY2U0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.qEIJhHpcFatz_gvF943nlwznhaU8drK0Yuvpok-a2Lk)
### /fw 入力単語を含む日記エントリを見つける
```
/fw <input word>
```
![fw image](https://private-user-images.githubusercontent.com/117506621/340078883-38808b5a-0c51-468f-801f-a596648611bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MjkxNjIsIm5iZiI6MTcxODUyODg2MiwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODgzLTM4ODA4YjVhLTBjNTEtNDY4Zi04MDFmLWE1OTY2NDg2MTFiZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTA3NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hODU5ZTcyOWMwZTMwY2Y3MmZlODg0MzM0NzNhZjM2OGVlZmVmZmJmMDAyOTRlMWM1ZTliNGMxZDJlOTBkODBhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.kC6mrSSSaR9PoBQidlhPFx2k2BxP0fMTik-2cVXtcDA)
### /fd 入力日付からの日記エントリを見つける
```
/fd <YYYY-MM-DD>
```
![fd image](https://private-user-images.githubusercontent.com/117506621/340078891-0cff9007-b815-4580-b535-eeb6291bbb0b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MjkxNjIsIm5iZiI6MTcxODUyODg2MiwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODkxLTBjZmY5MDA3LWI4MTUtNDU4MC1iNTM1LWVlYjYyOTFiYmIwYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTA3NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYjhjZDk2ZDQyYjQ2YmI1ZDY2OWQxZGIxZWY1ZDI2N2NhZGQzZmUzMTA3ODU3MTY1ZDEyODdmNzBjMTNjNjhjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.C7eDEIH7wibYY77WNwBIQeZ6FJJTDzUwFy0dW-Rq1xs)
### /ft 入力時間範囲内の日記エントリを見つける
```
/ft <HH:MM-HH:MM>
```
![ft image](https://private-user-images.githubusercontent.com/117506621/340078895-bc3cde3b-66d9-4abe-b1d2-3225db9a944a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1Mjg3ODksIm5iZiI6MTcxODUyODQ4OSwicGF0aCI6Ii8xMTc1MDY2MjEvMzQwMDc4ODk1LWJjM2NkZTNiLTY2ZDktNGFiZS1iMWQyLTMyMjVkYjlhOTQ0YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNlQwOTAxMjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NmE3NzljNWZkYjQ3YzhjNTg0Y2YzYmY0YTBkYWY0YjI5NzgxYzZhNjlmMTZiODRjOWZkOGUzNThhYjYwM2VhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.jn8k8UAxbsezfF8C-DgFKgS-NHlQKGSvmR_kqzgPL5I)
## ファイル構成
```

├── README.md
├── main.py                 # 実行ファイル
├── diary_bot               # projectフォルダ
│   ├── diary.py            # diary_botコマンドの関数
│   ├── db_app.py           # SQLiteをpythonで操作する関数
│   └── env.py              # .envを読み込むファイル
├── config                  # 各種変数の管理
│   ├── config.py           # ヘルプメッセージやエラーメッセージを管理
│   └── sql_statements.py   # SQLのコマンドを管理
├── database                # SQLiteのデータベースを格納するフォルダ
├── .devcontainer           # CodeSpacesの環境を構築する
├── .vscode                 # VScodeの環境を構築する        
├── .env                    # ファイルを作成し、トークンを記載する
├── poetry.lock             # poetry依存関係
└── pyproject.toml          # pythonプロジェクトにおける開発設定ファイル

```

## データベース

```
+------------+-----------+
|  contents  | Data Type |
+------------+-----------+
| id (PK)    | INTEGER   |
| user       | TEXT      |
| message    | TEXT      |
| create_at  | DATETIME  |
| channel    | TEXT      |
| guild      | TEXT      |
| image_url  | TEXT      |
+------------+-----------+
```

## 使用言語
- python

## 使用ライブラリ
- discordpy
- python-dotenv
- isort
- black
- sqlite3
- logger

## 開発ツール
- vscode
- github codespace

## 参考資料
- 「Discord Botを簡単お手軽開発する方法」（ときうかぜのブログ）
    https://www.tokiukaze.com/blog/discord-bot-dev/
- 「DiscordJockey」（Adrian Steffan）
    https://github.com/adriansteffan/DiscordJockey
- 「diarycat_public」（hoangphuc05）
    https://github.com/hoangphuc05/diarycat_public
- 「ログ出力のための print と import logging はやめてほしい」（@amedama）
    https://qiita.com/amedama/items/b856b2f30c2f38665701
- 「SQLite Python」（SQLite TUTORIAL）
    https://www.sqlitetutorial.net/sqlite-python/
- 「discord.py」（Rapptz）
    https://discordpy.readthedocs.io/
