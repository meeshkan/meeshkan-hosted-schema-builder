from io import TextIOWrapper
from json.decoder import JSONDecodeError

import meeshkan
import yaml
from flask import Flask, request
from flask_talisman import Talisman
from http_types import HttpExchangeReader
from openapi_typed_2.converters import convert_from_openapi

app = Flask(__name__)
Talisman(app)
INDEX_HTML = open("index.html").read()


@app.route("/schema-builder", strict_slashes=False)
def get():
    """Return a description of how to use the API."""
    return INDEX_HTML


@app.route("/schema-builder", methods=["POST"], strict_slashes=False)
def generate_schema():
    """Return a generated schema built from posted HTTP recordings."""
    if request.headers["content-type"].startswith("multipart/form-data"):
        uploaded_file = request.files["file"]
        uploaded_file.seek(0)
        file_content = TextIOWrapper(uploaded_file)
    else:
        file_content = request.stream

    try:
        http_exchanges = HttpExchangeReader.from_jsonl(file_content)
        openapi_schema = meeshkan.build_schema_batch(http_exchanges)
        response_text = yaml.safe_dump(convert_from_openapi(openapi_schema))
        return (
            response_text,
            200,
            {
                "content-type": "application/vnd.oai.openapi",
                "content-disposition": 'attachment; filename="openapi-schema.yml"',
            },
        )
    except JSONDecodeError:
        response_text = "Content is not JSON\r\n"
        return response_text, 400, {"content-type": "text/plain"}


@app.route("/_ah/warmup")
def warmup():
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9093, debug=True, extra_files=["index.html"])
