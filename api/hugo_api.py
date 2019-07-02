from flask import Flask, jsonify, request
import verify_payload as v
import calculator as calc

app = Flask(__name__)


@app.route('/calculator/<function>', methods=['POST'])
def calculator_service(function):
    try:
        req = request.get_json()
    except Exception, err:
        app.logger.error(err)
        return jsonify({'error': 'Invalid JSON request'}), 400

    err_message, status = v.verify(function, req)
    if status is not None:
        app.logger.error('And error occur while verifying the payload: %s', err_message["error"])
        return jsonify(err_message), status
    else:
        number1 = req["number_1"]
        number2 = req["number_2"]

        response = calc.Calculator(number1, number2, function)
        msg, status_code = response.call_calc()
        return jsonify(msg), status_code


@app.errorhandler(405)
def method_not_allowed(error):
    app.logger.error(error)
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(404)
def method_not_allowed(error):
    app.logger.error(error)
    return jsonify({'error': 'The requested URL was not found on the server'}), 404
