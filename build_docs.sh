# build api docs
sphinx-apidoc -f -o api-docs devcontainer_python_template
sphinx-build api-docs api-docs/_build

docker compose run --rm mkdocs mkdocs build
