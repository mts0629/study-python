# python-study

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

## 参考

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [mypy documentation](https://mypy.readthedocs.io/en/stable/index.html)
