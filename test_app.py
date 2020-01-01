import app

@pytest.fixture
def client():
    """ Start a fake server of the flask app """
    with app.test_client() as client:
        yield client


def test_main_page(client):
    """ pytest uses 'client' to find the fixture """
    response = client.get('/')
    assert 'Movie' in response.data
