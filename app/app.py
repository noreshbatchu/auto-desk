# app/main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Autodesk Project!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
