from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    n = int(request.form['num'])
    if n == 1:
        return f"Success{n}"
    else:
        return f"Failed{n}"


if __name__ == '__main__':
    app.run(debug=True)
