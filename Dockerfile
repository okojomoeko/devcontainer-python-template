FROM python:3-buster

WORKDIR /app

RUN pip install -U \
        pip \
        mkdocs \
        mkdocs-autorefs \
        mkdocs-material \
        mkdocs-markmap \
        mkdocs-material-extensions \
        mkdocstrings \
        mkdocstrings-python \
        plantuml-markdown \
        fontawesome-markdown \
        mdx_unimoji \
        python-markdown-math \
        pymdown-extensions
