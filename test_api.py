import requests
import json


def test_upload():
    url = "http://localhost:8080/api/v1.0/posts"\
        "/upload?tags=test_image+test_tag+highres&rating=safe"
    with open("wl-logo.png", "rb") as f:
        image = f.read()
    payload = image
    headers = {
        'Content-Type': 'image/jpeg'
    }
    response = requests.request("POST", url, headers=headers,
                                data=payload)
    data = json.loads(response.text)
    assert data['height'] == 512
    assert data['md5_hash'] == "43e4986442fc97d495e9759fdadc4231"
    assert data['rating'] == "safe"
    assert data['tags'] == ["test_image", "test_tag", "highres"]
    assert data['width'] == 512


def test_get_image():
    url = "http://localhost:8080/api/v1.0/images/1"
    response = requests.request("GET", url)
    assert response.status_code == 200


def test_delete_image():
    url = "http://localhost:8080/api/v1.0/posts/delete/1"
    response = requests.request("DELETE", url)
    data = json.loads(response.text)
    assert data['success']


def test_delete_all_posts():
    url = "http://localhost:8080/api/v1.0/posts/deleteall"
    response = requests.request("DELETE", url)
    data = json.loads(response.text)
    assert data['success']


def test_search_by_tags():
    url = "http://localhost:8080/api/v1.0/posts"\
        "/upload?tags=test_image+test_tag+highres&rating=safe"
    with open("wl-logo.png", "rb") as f:
        image = f.read()
    payload = image
    headers = {
        'Content-Type': 'image/jpeg'
    }
    requests.request("POST", url, headers=headers, data=payload)

    url = "http://localhost:8080/api/v1.0/posts/search?tags=highres+test_image"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data[0]['height'] == 512
    assert data[0]['md5_hash'] == "43e4986442fc97d495e9759fdadc4231"
    assert data[0]['rating'] == "safe"
    assert data[0]['tags'] == ["test_image", "test_tag", "highres"]
    assert data[0]['width'] == 512


def test_search_by_id():
    url = "http://localhost:8080/api/v1.0/posts/1"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data['height'] == 512
    assert data['md5_hash'] == "43e4986442fc97d495e9759fdadc4231"
    assert data['rating'] == "safe"
    assert data['tags'] == ["test_image", "test_tag", "highres"]
    assert data['width'] == 512


def test_get_all_posts():
    url = "http://localhost:8080/api/v1.0/posts"\
        "/upload?tags=test_image+test_tag+highres&rating=safe"
    with open("wl-logo.png", "rb") as f:
        image = f.read()
    payload = image
    headers = {
        'Content-Type': 'image/jpeg'
    }
    requests.request("POST", url, headers=headers, data=payload)

    url = "http://localhost:8080/api/v1.0/posts/search?tags=highres+test_image"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data[0]['height'] == 512
    assert data[0]['md5_hash'] == "43e4986442fc97d495e9759fdadc4231"
    assert data[0]['rating'] == "safe"
    assert data[0]['tags'] == ["test_image", "test_tag", "highres"]
    assert data[0]['width'] == 512
    assert data[1]['height'] == 512
    assert data[1]['md5_hash'] == "43e4986442fc97d495e9759fdadc4231"
    assert data[1]['rating'] == "safe"
    assert data[1]['tags'] == ["test_image", "test_tag", "highres"]
    assert data[1]['width'] == 512


def test_reset_all_settings():
    url = "http://localhost:8080/api/v1.0/settings/reset"
    response = requests.request("DELETE", url)
    data = json.loads(response.text)
    assert data['success']


def test_feature_post():
    url = "http://localhost:8080/api/v1.0/settings/feature_post/1"
    response = requests.request("POST", url)
    data = json.loads(response.text)
    assert data['featured_post'] == 1


def test_get_featured_post():
    url = "http://localhost:8080/api/v1.0/settings/featured_post"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data['featured_post'] == 1


def test_set_tag_description():
    url = "http://localhost:8080/api/v1.0/tags/setdesc/"\
          "test_tag?description=Tag used for testing"
    response = requests.request("POST", url)
    data = json.loads(response.text)
    assert data['success']


def test_get_tag():
    url = "http://localhost:8080/api/v1.0/tags/test_tag"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data['name'] == "test_tag"
    assert data['description'] == "Tag used for testing"


def test_get_all_tags():
    url = "http://localhost:8080/api/v1.0/tags/all"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    assert data["tags"] == ["test_image", "test_tag", "highres"]


def test_get_thumbnail():
    url = "http://localhost:8080/api/v1.0/thumbs/1"
    response = requests.request("GET", url)
    assert response.status_code == 200


def test_delete_all_thumbnail():
    url = "http://localhost:8080/api/v1.0/thumbs/deleteall"
    response = requests.request("DELETE", url)
    data = json.loads(response.text)
    assert data['success']


def test_import_danbooru():
    url = "http://localhost:8080/api/v1.0/import/gelbooru/5373026"
    response = requests.request("POST", url)
    data = json.loads(response.text)
    assert data['height'] == 4272
    assert data['md5_hash'] == "0dc9ed721c9690e9f16e28a0b48e0f25"
    assert data['rating'] == "safe"
    assert data['tags'] == ["1girl", "absurdres", "bangs", "bikini",
                            "black_hair", "blunt_bangs", "blush",
                            "breasts", "chitanda_eru", "cleavage",
                            "collarbone", "eyebrows_visible_through_hair",
                            "frilled_bikini", "frills", "highres", "hyouka",
                            "jacket", "medium_breasts", "navel", "parted_lips",
                            "pink_jacket", "ponytail", "pool", "poolside",
                            "purple_eyes", "sak_(lemondisk)", "solo",
                            "swimsuit", "upper_body", "water", "wet",
                            "white_bikini"]
    assert data['width'] == 2802
