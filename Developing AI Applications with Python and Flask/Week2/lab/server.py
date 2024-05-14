import uuid as uuid_module  # Renaming the module to avoid conflicts with other variables
from flask import Flask, make_response, request
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

@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

@app.route("/name_search")
def name_search():
    q = request.args.get("q")
    
    if not q:
        resp = make_response({"422": "Invalid input parameter"})
        resp.status_code = 422
        return resp
    
    for i in data:
        if i['first_name'].lower() == q.lower():
            resp = make_response(i)
            resp.status_code = 200
            return resp
            
    resp = make_response({"404": "Person not found"})
    resp.status_code = 404
    return resp
        
        
@app.route("/count")
def count():
    return {"data count": len(data)}, 200

@app.route("/person/<uuid>")
def find_by_uuid(uuid):
    try:
        # Attempt to create a UUID object from the string
        uuid_obj = uuid_module.UUID(uuid)
        
    except ValueError:
        # If ValueError is raised, the string is not a valid UUID
        resp = make_response({"422": "Invalid input parameter: Not a valid UUID"})
        resp.status_code = 422
        return resp

    
    for i in data:
        if i['id'] == uuid:
            resp = make_response(i)
            resp.status_code = 200
            return resp
            
    resp = make_response({"404": "UUID not found"})
    resp.status_code = 404
    return resp


@app.route("/person/<uuid>", methods=['DELETE'])
def delete_by_uuid(uuid):
    for i in data:
        if i['id'] == uuid:
            resp = make_response({"Deleted": f"{uuid}"})
            resp.status_code = 200
            data.remove(i)
            return resp

@app.route("/person", methods=['POST'])
def add_by_uuid():
    if not request.json:
        resp = make_response({"422": "Invalid input parameter"})
        resp.status_code = 422
        return resp

    if request.json["id"] not in [d["id"] for d in data]:
        data.append(request.json)
        newaddid = request.json["id"]
        resp = make_response({"Add": f"{newaddid}"})
        resp.status_code = 200
        return resp
            
    resp = make_response({"404": "UUID already exists"})
    resp.status_code = 404
    return resp

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]