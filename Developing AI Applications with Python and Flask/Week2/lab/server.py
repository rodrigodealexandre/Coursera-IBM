from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/no_content")
def no_content():
    """return 'no content found' with a status of 204
    Returns:
        string: no content found with 204 status code
    """
    return({"204":"No content found"}, 204)

@app.route("/exp")
def index_explicit():
    """
    return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response({"200":"Hello World"})
    resp.status_code = 200
    return resp
