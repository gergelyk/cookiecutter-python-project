# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

* Documentation: <{{cookiecutter.docs_page_url}}>
* Repository: <{{cookiecutter.repo_url}}>
* Package: <{{cookiecutter.package_url}}>
* Author: [{{cookiecutter.author_email}}](mailto:{{cookiecutter.author_email}})
* License: [MIT](LICENSE)

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

# Auto-formatting
poetry run docformatter -ri {{cookiecutter.module_name}} tests
poetry run isort -rc {{cookiecutter.module_name}} tests
poetry run yapf -r -i {{cookiecutter.module_name}} tests

# Checking coding style
poetry run flake8 {{cookiecutter.module_name}} tests

# Checking composition and quality
poetry run mypy {{cookiecutter.module_name}} tests
poetry run pylint {{cookiecutter.module_name}} tests
poetry run bandit {{cookiecutter.module_name}} tests
poetry run radon cc {{cookiecutter.module_name}} tests
poetry run radon mi {{cookiecutter.module_name}} tests

# Testing with coverage
poetry run pytest --cov indentedlogs --cov tests

# Rendering documentation
poetry run mkdocs serve

# Building package
poetry build

# Releasing
poetry version minor  # increment selected component
git commit -am "bump version"
git push
git tag ${$(poetry version)[2]}
git push --tags
poetry build
poetry publish
poetry run mkdocs build
poetry run mkdocs gh-deploy -b gh-pages
```

## Donations

If you find this software useful and you would like to repay author's efforts you are welcome to use following button:

[![Donate](https://www.paypalobjects.com/en_US/PL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=D9KUJD9LTKJY8&source=url)

