## EngLDiary-bot
このEngLDiary-botは英語学習を目的として、日々の英語日記を管理するbotです。<br>日々の体験を英語で振り返り、体験と紐づいた英語学習体験を届けます。<br>現在の機能としては登録、検索、表示のみです。

## コマンド説明

### /add 日記をデータベースに保存する
```
/add <input sentence>
```
### /showme_all_contents データベースのすべての日記エントリを表示する
```
/showme_all_contents
```
### /fl 入力文字列を含む日記エントリを見つける
```
/fl <input letters>
```
### /fw 入力単語を含む日記エントリを見つける
```
/fw <input word>
```
### /fd 入力日付からの日記エントリを見つける
```
/fd <YYYY-MM-DD>
```
### /ft 入力時間範囲内の日記エントリを見つける
```
/ft <HH:MM-HH:MM>
```

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