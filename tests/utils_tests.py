import json


def get_request(n1, n2):
    message = {
        'number_1': n1,
        'number_2': n2
    }
    return json.dumps(message)


def assert_err_response(exp_response, exp_status, response):
    err = json.loads(response.data.decode('utf8'))
    assert response.status_code == exp_status
    assert err == exp_response


def assert_success_resp(exp_response, response):
    res = json.loads(response.data.decode('utf8'))
    assert response.status_code == 200
    assert res == exp_response
