from flask import Blueprint, request, jsonify
from service.usecases import *
from service.error import *
from service.transfer import *

routes = Blueprint('routes', __name__)


# Create User
@routes.route('/user', methods=['POST'])
def user_register():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    if not content["email"]:
        response = ErrorResponse("email field is missing", 400)
    elif not content["first_name"]:
        response = ErrorResponse("first_name field is missing", 400)
    elif not content["last_name"]:
        response = ErrorResponse("last_name field is missing", 400)
    elif not content["password"]:
        response = ErrorResponse("password field is missing", 400)
    else:
        signup_out = signup(SignupIn(content))
        if signup_out is SignupErrorInvalidTeacherToken:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is SignupErrorInvalidEmail:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is SignupErrorInvalidFirstName:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is SignupErrorInvalidLastName:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is SignupErrorInvalidWeakPassword:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is SignupError:
            response = ErrorResponse(signup_out.message, 500)
        elif signup_out is Error:
            response = ErrorResponse(signup_out.message, 500)
        else:
            response = Response(signup_out, 200)

    return response.get_json_value(), response.get_code()


# Login User
@routes.route('/user/login', methods=['POST'])
def user_login():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    if not content["email"]:
        response = ErrorResponse("email field is missing", 400)
    elif not content["password"]:
        response = ErrorResponse("password field is missing", 400)
    else:
        login_out = login(LoginIn(content))
        if login_out is LoginErrorWrongUsernameOrPassword:
            response = ErrorResponse(login_out.message, 400)
        elif login_out is LoginErrorUserNotFound:
            response = ErrorResponse(login_out.message, 400)
        elif login_out is LoginError:
            response = ErrorResponse(login_out.message, 500)
        elif login_out is Error:
            response = ErrorResponse(login_out.message, 500)
        else:
            response = Response(login_out, 200)

    return response.get_json_value(), response.get_code()


# Get User Info
@routes.route('/user/<uuid>/info', methods=['GET'])  # TODO not REST compliant
def user_info(uuid):
    info_out = info(InfoIn(uuid))
    if info_out is InfoErrorUserNotFound:
        response = ErrorResponse(info_out.message, 400)
    elif info_out is InfoError:
        response = ErrorResponse(info_out.message, 500)
    elif info_out is Error:
        response = ErrorResponse(info_out.message, 500)
    else:
        response = Response(info_out, 200)

    return response.get_json_value(), response.get_code()


# Set User Info
@routes.route('/user', methods=['PUT'])  # TODO not REST compliant
def user_update():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    if not content["session"]:  # TODO check other fields
        response = ErrorResponse("session field is missing", 400)
    else:
        signup_out = modify(ModifyIn(content))
        if signup_out is ModifyErrorUserNotFound:
            response = ErrorResponse(signup_out.message, 400)
        elif signup_out is ModifyError:
            response = ErrorResponse(signup_out.message, 500)
        elif signup_out is Error:
            response = ErrorResponse(signup_out.message, 500)
        else:
            response = Response(signup_out, 200)

    return response.get_json_value(), response.get_code()


# Verify Email
@routes.route('/user/verify', methods=['PATCH'])
def user_verify_email():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse('JSON expected', 400)
        return error.get_json_value(), error.get_code()

    if not content["token"]:
        response = ErrorResponse("token field is missing", 400)
    else:
        verify_email_out = verify_email(VerifyEmailIn(content))
        if verify_email_out is VerifyEmailErrorTokenNotFound:
            response = ErrorResponse(verify_email_out.message, 400)
        elif verify_email_out is VerifyEmailErrorUserNotFound:
            response = ErrorResponse(verify_email_out.message, 400)
        elif verify_email_out is VerifyEmailError:
            response = ErrorResponse(verify_email_out.message, 500)
        elif verify_email_out is Error:
            response = ErrorResponse(verify_email_out.message, 500)
        else:
            response = Response(verify_email_out, 200)

    return response.get_json_value(), response.get_code()


# Check User Session
@routes.route('/user/session', methods=['POST'])
def user_session():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse('JSON expected', 400)
        return error.get_json_value(), error.get_code()

    if not content["session"]:
        response = ErrorResponse("session field is missing", 400)
    else:
        verify_session_out = verify_session(VerifySessionIn(content))
        if verify_session_out is VerifySessionErrorInvalidSession:
            response = ErrorResponse(verify_session_out.message, 400)
        elif verify_session_out is VerifySessionError:
            response = ErrorResponse(verify_session_out.message, 500)
        elif verify_session_out is Error:
            response = ErrorResponse(verify_session_out.message, 500)
        else:
            response = Response(verify_session_out, 200)

    return response.get_json_value(), response.get_code()
