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

    if not "teacher_token" in content:
        content["teacher_token"] = None

    if not "email" in content:
        response = ErrorResponse("email field is missing", 400)
    elif not "first_name" in content:
        response = ErrorResponse("first_name field is missing", 400)
    elif not "last_name" in content:
        response = ErrorResponse("last_name field is missing", 400)
    elif not "password" in content:
        response = ErrorResponse("password field is missing", 400)
    else:
        signup_out = signup(SignupIn(content))
        if isinstance(signup_out, SignupErrorInvalidTeacherToken):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, SignupErrorInvalidEmail):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, SignupErrorInvalidFirstName):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, SignupErrorInvalidLastName):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, SignupErrorInvalidWeakPassword):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, SignupError):
            response = ErrorResponse(signup_out.message, 500)
        elif isinstance(signup_out, Error):
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

    if not "email" in content:
        response = ErrorResponse("email field is missing", 400)
    elif not "password" is content:
        response = ErrorResponse("password field is missing", 400)
    else:
        login_out = login(LoginIn(content))
        if isinstance(login_out, LoginErrorWrongUsernameOrPassword):
            response = ErrorResponse(login_out.message, 400)
        elif isinstance(login_out, LoginErrorUserNotFound):
            response = ErrorResponse(login_out.message, 400)
        elif isinstance(login_out, LoginError):
            response = ErrorResponse(login_out.message, 500)
        elif isinstance(login_out, Error):
            response = ErrorResponse(login_out.message, 500)
        else:
            response = Response(login_out, 200)

    return response.get_json_value(), response.get_code()


# Get User Info
@routes.route('/user/<uuid>', methods=['GET'])  # TODO not REST compliant
def user_info(uuid):
    info_out = info(InfoIn(uuid))
    if isinstance(info_out, InfoErrorUserNotFound):
        response = ErrorResponse(info_out.message, 400)
    elif isinstance(info_out, InfoError):
        response = ErrorResponse(info_out.message, 500)
    elif isinstance(info_out, Error):
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

    if not "session" in content:  # TODO check other fields
        response = ErrorResponse("session field is missing", 400)
    else:
        signup_out = modify(ModifyIn(content))
        if isinstance(signup_out, ModifyErrorUserNotFound):
            response = ErrorResponse(signup_out.message, 400)
        elif isinstance(signup_out, ModifyError):
            response = ErrorResponse(signup_out.message, 500)
        elif isinstance(signup_out, Error):
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

    if not "token" in content:
        response = ErrorResponse("token field is missing", 400)
    else:
        verify_email_out = verify_email(VerifyEmailIn(content))
        if isinstance(verify_email_out, VerifyEmailErrorTokenNotFound):
            response = ErrorResponse(verify_email_out.message, 400)
        elif isinstance(verify_email_out, VerifyEmailErrorUserNotFound):
            response = ErrorResponse(verify_email_out.message, 400)
        elif isinstance(verify_email_out, VerifyEmailError):
            response = ErrorResponse(verify_email_out.message, 500)
        elif isinstance(verify_email_out, Error):
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

    if not "session" in content:
        response = ErrorResponse("session field is missing", 400)
    else:
        verify_session_out = verify_session(VerifySessionIn(content))
        if isinstance(verify_session_out, VerifySessionErrorInvalidSession):
            response = ErrorResponse(verify_session_out.message, 400)
        elif isinstance(verify_session_out, VerifySessionError):
            response = ErrorResponse(verify_session_out.message, 500)
        elif isinstance(verify_session_out, Error):
            response = ErrorResponse(verify_session_out.message, 500)
        else:
            response = Response(verify_session_out, 200)

    return response.get_json_value(), response.get_code()


# Ban User
@routes.route('/user/<uuid>/ban', methods=['POST'])
def user_ban(uuid):
    ban_out = ban(BanIn(uuid))
    if isinstance(ban_out, VerifySessionErrorInvalidSession):
        response = ErrorResponse(ban_out.message, 400)
    elif isinstance(ban_out, VerifySessionError):
        response = ErrorResponse(ban_out.message, 500)
    elif isinstance(ban_out, Error):
        response = ErrorResponse(ban_out.message, 500)
    else:
        response = Response(ban_out, 200)

    return response.get_json_value(), response.get_code()
