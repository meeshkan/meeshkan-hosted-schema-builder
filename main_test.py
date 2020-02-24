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
