from flask import Flask, render_template, request, jsonify
from customer import Customer
from employee import Employee

app = Flask(__name__)

# -----------------------------
# HOME PAGE
# Customer login page
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')


# -----------------------------
# CUSTOMER LOGIN
# -----------------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('email')   # using email field as username for now
    password = data.get('password')

    customer_id = Customer.authenticateCustomer(username, password)

    if customer_id != -1:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


# -----------------------------
# EMPLOYEE LOGIN PAGE
# -----------------------------
@app.route('/employee')
def employee_page():
    return render_template('employee_login.html')


# -----------------------------
# EMPLOYEE LOGIN
# -----------------------------
@app.route('/employee-login', methods=['POST'])
def employee_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    employee_id = Employee.authenticateEmployee(username, password)

    if employee_id != -1:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)