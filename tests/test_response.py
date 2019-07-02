import pytest
import json
import utils_tests as u
import api.hugo_api as api


@pytest.fixture
def client(request):
    test_client = api.app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def test_path_not_found(client):
    req = u.get_request(10, 20)
    error = {"error": "The requested URL was not found on the server"}
    urls = ['/calculator/other', '/api/division']
    for url in urls:
        response = client.post(url, data=req, content_type='application/json')
        u.assert_err_response(error, 404, response)


def test_invalid_number_of_variables(client):
    message = {
        'number_1': 10,
        'number_2': 20,
        'number_3': 10
    }
    error = {"error": "Request cannot have more than two variables"}
    request = json.dumps(message)
    response = client.post('/calculator/addition', data=request, content_type='application/json')
    u.assert_err_response(error, 400, response)


def test_variables_not_numeric(client):
    req = u.get_request(10, "20")
    error = {"error": "Variables are not numeric"}
    response = client.post('/calculator/division', data=req, content_type='application/json')
    u.assert_err_response(error, 400, response)


def test_name_of_variables_incorrect(client):
    message = {
        'number_1': 10,
        'number_10': 20
    }
    error = {"error": "Variable number_2 missing in the request"}
    request = json.dumps(message)
    response = client.post('/calculator/multiplication', data=request, content_type='application/json')
    u.assert_err_response(error, 400, response)


def test_invalid_json(client):
    error = {"error": "Invalid JSON request"}
    response = client.post('/calculator/multiplication', content_type='application/json')
    u.assert_err_response(error, 400, response)


def test_division_error(client):
    req = u.get_request(10, 0)
    error = {"error": "Zero division error"}
    response = client.post('/calculator/division', data=req, content_type='application/json')
    u.assert_err_response(error, 500, response)


def test_method_not_allowed(client):
    req = u.get_request(10, 2)
    error = {"error": "Method not allowed"}
    response = client.put('/calculator/division', data=req, content_type='application/json')
    u.assert_err_response(error, 405, response)


@pytest.mark.parametrize("n1,n2,exp,func", [
    (5, 20, 25, "addition"),
    (5.5, 10, -4.5, "subtraction"),
    (10, 0.5, 5, "multiplication"),
    (100, 82, 1.22, "division")
])
def test_success_response(client, n1, n2, exp, func):
    req = u.get_request(n1, n2)
    success = {"result": exp}
    url = "/calculator/" + func
    response = client.post(url, data=req, content_type='application/json')
    u.assert_success_resp(success, response)
