from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return 'Team User-Microservice'


@app.route('/user/register', methods=['POST'])
def user_register():
    return 'some register shit here'


@app.route('/user/verify', methods=['PATCH'])
def user_verify():
    return 'and some verify stuff here'


@app.route('/user/login', methods=['POST'])
def user_login():
    return 'some login magic here'


@app.route('/user/info', methods=['POST'])
def user_info():
    return 'info responses here'


@app.route('/user/update', methods=['PUT'])
def user_update():
    return 'and update responses here'


if __name__ == '__main__':
    app.run(port=4450, threaded=True)
