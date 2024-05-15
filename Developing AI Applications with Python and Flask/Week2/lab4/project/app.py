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
    
    else:
        transation = {
          'id': len(transactions)+1,
          'date': request.form['date'],
          'amount': float(request.form['amount'])
         }
        
        transactions.append(transation)
        
        return redirect(url_for("get_transactions")) # `url_for(get_transactions)` `get_transactions` needs to be within quotation makrs.

# Update operation
@app.route("/edit/<int:transaction_id>", methods=['POST', 'GET'])
def edit_transaction(transaction_id):
    # if transaction_id in [transaction["id"] for transaction in transactions]: this method does not work since it only checks if true or false
    if request.method == "GET":
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template("edit.html", transaction=transaction)
        
    else:
        date = request.form['date']
        amount = request.form['amount']
        
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break # add break so it stops when it finds the value after updated.

        return redirect(url_for("get_transactions"))
    
# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))

            
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
