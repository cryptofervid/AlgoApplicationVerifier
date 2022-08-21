import json
from app import app


def test_get_all_projects():

    response = app.test_client().get("/validationapi/projects")
    assert response.status_code == 200

    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is list


def test_get_all_commits_by_project():

    response = app.test_client().get("/validationapi/projects/1/commits")
    assert response.status_code == 200

    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is list


