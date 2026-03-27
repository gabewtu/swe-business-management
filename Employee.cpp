///////////////////////////////////////////////////////////////////////////////
// Author: Katie Garner
// Description: This is the implementation file for the Employee class for the
//				COSC412 Project.
///////////////////////////////////////////////////////////////////////////////

#include "Employee.h"
#include "HashUtilities.h"

// Constructors
Employee::Employee() {
    firstName = "";
    lastName = "";
    email = "";
    userName = "";
    passwordHash = "";
    salt = "";
    employeeID = -1;
    expenses = 0;
}

Employee::Employee(string fN, string lN, string email, string uName, int empID) {
    this->firstName = fN;
    this->lastName = lN;
    this->email = email;
    this->userName = uName;
    this->passwordHash = "";
    this->salt = "";
    this->employeeID = empID;
    expenses = 0;
}

Employee::Employee(string fN, string lN, string email, string uName, string pHash, string s, int empID) {
    this->firstName = fN;
    this->lastName = lN;
    this->employeeID = empID;
    this->email = email;
    this->userName = uName;
    this->passwordHash = pHash;
    this->salt = s;
    expenses = 0;
}


// Getters
string Employee::getFirstName() const {
    return firstName;
}

string Employee::getLastName() const {
    return lastName;
}

string Employee::getEmail() const {
    return email;
}

int Employee::getEmployeeID() const {
    return employeeID;
}

double Employee::getExpenses() const {
    return expenses;
}


// Setters
void Employee::setUserName(const string& uName) {
    userName = uName;
}

void Employee::setPassword(const string& plainPassword) {
    passwordHash = HashUtilities::hashPassword(plainPassword, salt);
}

bool Employee::verifyPassword(const string& plainPassword) const {
    return passwordHash == HashUtilities::hashWithSalt(plainPassword, salt);
}

bool Employee::addExpenseToDB(double exp) {
	expenses += exp; // keep object consistent

	// Database stuff

	return true;
}
