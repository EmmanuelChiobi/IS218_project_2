"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/pylint">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/oop">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    # assert b"Index Page" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    # assert b"About Page" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    # assert b"Page 1" in response.data

def test_request_python(client):
    """This makes the index page"""
    response = client.get("/python")
    assert response.status_code == 200
    # assert b"Page 2" in response.data

def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    # assert b"Page 3" in response.data

def test_request_pylint(client):
    """This makes the index page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    # assert b"Page 3" in response.data

def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    # assert b"Page 3" in response.data

def test_request_oop(client):
    """This makes the index page"""
    response = client.get("/oop")
    assert response.status_code == 200
    # assert b"Page 3" in response.data

def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    # assert b"Page 3" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
