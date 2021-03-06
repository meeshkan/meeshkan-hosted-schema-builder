[![Build Status](https://github.com/meeshkan/meeshkan-hosted-schema-builder/workflows/CI/badge.svg)](https://github.com/meeshkan/meeshkan-hosted-schema-builder/actions?query=workflow%3ACI)
[![MIT licensed](http://img.shields.io/:license-MIT-blue.svg)](LICENSE)

# meeshkan-hosted-schema-builder
The [meeshkan schema builder](https://github.com/meeshkan/meeshkan) exposed as a HTTP API.

To use the hosted service, visit [meeshkan.io/schema-builder](https://meeshkan.io/schema-builder). Commits on the master branch are automatically deployed there.

Read on for how to develop and run locally.

# Setup
Create an isolated Python environment and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt -r requirements-dev.txt
```

# Running locally
Run the application with `python main.py`.

- Access it in a browser: http://localhost:8080/schema-builder
- Post data to it with curl: `curl -X POST --data-binary @recordings.jsonl http://localhost:8080/schema-builder`

# Running tests
Run `./check.sh`.
