from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>hello world</h1>'

@app.route('/user/<string:name>')
def get_user(name):
    return '<h1>hello %s</h1>' % name

    if __name__ == "__main__":
        app.run(debug=True);
