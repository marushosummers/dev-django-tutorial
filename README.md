python-dev
===

Prototype を作る時に毎回するセットアップをまとめておく。

# 開発
## 準備
依存関係の解決なども pipenv によって行っているのでインストールする。
また、必要なバージョンをインストールできるように pyenv もインストールしておく。

```shell
pip install --upgrade pip && pip install pipenv
```

## Dockerを使わない場合の環境構築
以下のコマンドで依存関係を解消する。

```shell
pipenv install --dev
```

## Docker (*正直 prototyping で Docker が必要とは思わない。pipenv で事足りそう*)
### 前提となる環境
- Dockerクライアントがホストマシンにインストールされていること

### macOS での Docker セットアップ
以下のコマンドを実行後、 Docker.app を起動し、`docker ps` 等にてインストールの確認。

```bash
# docker-compose も導入されるはず
brew cask install docker
```
### コンテナの立ち上げ
以下のコマンドで Docker コンテナが立ち上がる。

```shell
make run
```
成功すれば、 `docker ps` でコンテナが起動していることが確認できるはず。


## 実行方法
以下で jupyter lab を起動できる。

```shell
./run_notebook.sh
```

pipenv で取得したライブラリは kernel を作ることで jupyter（[`run_notebook.sh`](./run_notebook.sh) でカーネル `python_proto` を作っているのでそれを指定する）。

参考: [pipenv環境でjupyterを使う際のkernel設定 - Qiita](https://qiita.com/mzn/items/99d769d0ad9d03a5d73e)


## Linter
```shell
make lint

# or 

pipenv run lint
```

自動で修正する場合は以下のコマンドを実行する。

```shell
make format

# or 

pipenv run format
```

## Debug
以下のコマンドが利用可能。詳細は[Makefile](./Makefile)を参照のこと。

```
make enter      # コンテナに入る
make log        # ログを見始める
```

# CI
Circle CI の config を [`.circleci/config.yml`](./.circleci/config.yml) に記述している。現在は以下の設定になっている。

* すべての commit に対して test が走る。
* release への commit に対して、 `release/{date}_{number}` タグが切られる。

このため、基本的には `dev` ブランチを切って、それを default ブランチに設定し、`release` への commit は `dev` ブランチのマージによって行うと良い。このリポジトリ自体は release の概念はないので、 `release` のみを用意している。
