import yaml

import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/schema-builder", base_url="https://localhost")
    assert r.status_code == 200
    assert r.data.decode("utf-8") == open("index.html").read()


def test_post_non_json():
    main.app.testing = True
    client = main.app.test_client()

    r = client.post(
        "/schema-builder",
        data="not json",
        base_url="https://localhost",
        headers={"content-type": "application/x-www-form-urlencoded"},
    )
    assert r.status_code == 400
    assert r.data.decode("utf-8") == "Content is not JSON\r\n"


def test_post_recordings():
    main.app.testing = True
    client = main.app.test_client()

    recordings = open("recordings.jsonl").read()

    r = client.post(
        "/schema-builder",
        data=recordings,
        base_url="https://localhost",
        headers={"content-type": "application/x-www-form-urlencoded"},
    )
    result_yaml = yaml.safe_load(r.data.decode("utf-8"))

    assert r.status_code == 200
    assert result_yaml["servers"][0]["url"] == "http://api.github.com"
    assert result_yaml["paths"]["/user/repos"]["description"] == "Path description"
