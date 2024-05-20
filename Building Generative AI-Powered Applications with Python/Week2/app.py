from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/bananas')
def bananas():
    return 'This page has bananas!'
    
@app.route('/bread')
def bread():
    return 'This page has bread!'

if __name__ == '__main__':
    app.run()
