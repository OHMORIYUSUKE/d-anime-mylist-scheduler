# d-anime-mylist-scheduler

[d-anime-mylist-backend](https://github.com/OHMORIYUSUKE/d-anime-mylist-backend)の DB の情報を更新するためのツールです。

## 作業方法

1. .venv をルートディレクトリに作成
2. requirements.txt に記載されているライブラリをインストール
3. .env を.env.sample をコピーしてルートディレクトリに作成

## 利用方法

main.py を定期実行させる。

※ 定期実行させることで、ユーザーが登録した d アニメストアのマイリストの状態を定期的に DB に更新させることができます。
