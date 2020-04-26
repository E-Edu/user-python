import datetime

def response(code, status, path, msg=None):
    time = datetime.datetime.utcnow().isoformat()
    return {
        "code": code,
        "status": status,
        "timestamp": time,
        "path": path,
        "msg": msg
    }, code

class Status():
    c_200 = "OK"
    c_201 = "Created"

    c_400 = "Bad Request"
    c_401 = "Unauthorized"
    c_403 = "Forbidden"

    c_500 = "Internal Server Error"
    c_501 = "Not Implemented"

    cm_1 = "invalid credentials"
    cm_2 = "missing keys"
"""
Code Status
200  OK
201  Created

400  Bad Request
401  Unauthorized
403  Forbidden

500  Internal Server Error
501  Not Implemented
"""