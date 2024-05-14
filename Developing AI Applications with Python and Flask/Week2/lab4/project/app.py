# Import libraries
from flask import Flask, request, url_for, redirect, render_template 

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template('transactions.html', transactions = transactions)


# Create operation
@app.route("/add", methods=['POST', 'GET'])
def add_transaction():
    if request.method == "GET":
        return render_template('form.html')
    
    elif request.method == "POST":
        transation = {
          'id': len(transactions)+1,
          'date': request.form['date'],
          'amount': float(request.form['amount'])
         }
        
        transactions.append(transation)


# Update operation
@app.route("", methods=['POST'])
def update():
    pass

# Delete operation
@app.route("", methods=['DELETE'])
def delete():
    pass

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
