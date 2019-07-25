from flask import Flask, jsonify

app = Flask(__name__)

# @app.route('/<name>')
# def index(name):
#     return '<h1>Hello there {}! </h1>'. format(name)
@app.route('/home')
def home():
    return '<h1>You are at home man</h1>'
@app.route('/json')
def json():
    return jsonify({"key1":"value1","key2":[1,2,3,4,5,6,7,8,9,0]})

if __name__ == '__main__':
    app.debug=True
    app.run()