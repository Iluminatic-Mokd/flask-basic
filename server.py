from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def index():
    return  f'Hello World'

@app.route('/name')
def name():
    return f'<h1>Thanapoom Rattanapakdee</h1>'


# if __name__ == '__main__':
#     app.run(debug=True)