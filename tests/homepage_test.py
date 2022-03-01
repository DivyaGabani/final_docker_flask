"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Some quick example" in response.data
    assert b'<a class="nav-link" href="/about">About</a>' in response.data


    def test_request_index(client):
        """This makes the index page"""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Homepage" in response.data

    def test_request_index(client):
        """This makes the about page"""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent semper ultricies erat vitae volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed aliquet posuere porta. Nulla sem metus, pharetra vitae ante id, feugiat lobortis velit. Donec mollis eros maximus est viverra venenatis. Donec sed lorem sem. Mauris sit amet pulvinar neque. Nulla facilisi. Vestibulum sit amet maximus eros." in response.data
