# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

* Documentation: <{{cookiecutter.docs_page_url}}>
* Repository: <{{cookiecutter.repo_url}}>
* Package: <{{cookiecutter.package_url}}>
* Author: <mailto:{{cookiecutter.author_email}}>
& License: [MIT](LICENSE)

## Requirements

This package requires CPython 3.8 or compatible. If you have other version already installed, you can switch using `pyenv`. It must be installed as described in the [manual](https://github.com/pyenv/pyenv).

```sh
pyenv install 3.8.2
pyenv local 3.8.2
```

## Installation

```sh
pip install {{cookiecutter.package_name}}
```

## Usage

```sh
poetry run python {{cookiecutter.module_name}}/hello.py
```

## Development

```sh
# Preparing environment
pip install --user poetry  # unless already installed
poetry install

# Rendering documentation
poetry run mkdocs serve

# Testing
poetry run pytest

# Checking coding style
poetry run flake8 {{cookiecutter.module_name}} tests

# Checking type annotations
poetry run mypy {{cookiecutter.module_name}} tests

# Building package
poetry build

# Releasing
poetry version minor  # increment selected component
git tag ${$(poetry version)[2]}
git push --tags
poetry build
poetry publish
poetry run mkdocs build
poetry run mkdocs gh-deploy -b gh-pages
```
