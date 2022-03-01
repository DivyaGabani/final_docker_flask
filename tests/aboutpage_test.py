"""This test the aboutpage"""


def test_request_index(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Aboutpage" in response.data
