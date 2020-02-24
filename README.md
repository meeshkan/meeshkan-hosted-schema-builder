# meeshkan-hosted-schema-builder
The [meeshkan schema builder](https://github.com/meeshkan/meeshkan) exposed as a HTTP API.

To use the hosted service, visit https://meeshkan.io/schema-builder.

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

- Access it in a browser at `http://localhost:8080`
- and post data to it with `curl -X POST --data-binary @resources/recordings.jsonl http://localhost:8080`.

# Running tests
Run `./check.sh`.
