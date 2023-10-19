# study-python

Pythonの学習

## 環境

- OS：Ubuntu 20.04 LTS (native/WSL2)
- Python 3.11.4
    - [Release](https://www.python.org/downloads/release/python-3114/)
    - インストール
        ```sh
        $ ./configure
        $ make
        $ make test
        $ sudo make install
        ```
        - pipがSSL moduleのエラーで失敗していたが、Requirementsを見直して再度ビルドすることにより解消した
            [pyenv/Troubleshooting/FAQ/Suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
            ```sh
            $ sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
            libbz2-dev libreadline-dev libsqlite3-dev curl \
            libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
            ```
- 仮想環境：venv
    - `$ python -m venv .venv && source .venv/bin/activate`
- mypy 1.4.1
- pytest 7.4.0

## ソースコード・著作権

本リポジトリに含まれるソースコードは、下記で公開されている内容を元に改変を加えたものです。

未改変部の著作権は、原著作者様に帰属します。

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [mypy documentation](https://mypy.readthedocs.io/en/stable/index.html)
- [pytest documentation](https://docs.pytest.org/en/7.4.x/index.html)

### 改変点

- コーディングスタイルの調整
- コメントの追加
- ファイル構成
