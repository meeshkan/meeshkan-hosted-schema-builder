import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/")
    assert r.status_code == 200
    assert r.data.decode("utf-8").startswith("Meeshkan schema builder")


def test_post_non_json():
    main.app.testing = True
    client = main.app.test_client()

    r = client.post("/", data="not json")
    assert r.status_code == 400
    assert r.data.decode("utf-8") == "Content is not JSON\r\n"
