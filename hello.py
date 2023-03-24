from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
    return "Hello world"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


if __name__ == '__main__':
    app.run(debug=True)
