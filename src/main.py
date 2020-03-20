from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return 'Team User-Microservice'


if __name__ == '__main__':
    app.run(port=4450, threaded=True)
