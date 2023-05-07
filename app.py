from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Тест!'
# just a comment

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
