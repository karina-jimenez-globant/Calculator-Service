
functions_available = ['addition', 'subtraction', 'division', 'multiplication']


def verify(function, r):
    message = dict({})

    if function not in functions_available:
        message["error"] = "The requested URL was not found on the server"
        return message, 404

    if len(r) > 2:
        message["error"] = "Request cannot have more than two variables"
        return message, 400

    try:
        n1 = r["number_1"]
        n2 = r["number_2"]
    except Exception, ex:
        message["error"] = "Variable "+ex.args[0]+" missing in the request"
        return message, 400

    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
        message["error"] = "Variables are not numeric"
        return message, 400

    return message, None



