from hash_utilities import HashUtilities


class Employee:
    class SearchCriteria:
        def __init__(self, employeeID=-1, firstName="", lastName="", email="", userName=""):
            self.employeeID = employeeID
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.userName = userName

    # Constructor
    def __init__(self, fN="", lN="", email="", uName="", passwordHash="", salt="", empID=-1):
        self.firstName = fN
        self.lastName = lN
        self.email = email
        self.userName = uName
        self.passwordHash = passwordHash
        self.salt = salt
        self.employeeID = empID
        self.expenses = 0.0

    # Getters
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getUserName(self):
        return self.userName

    def getEmployeeID(self):
        return self.employeeID

    def getExpenses(self):
        return self.expenses

    # Setters
    def setFirstName(self, fN):
        self.firstName = fN

    def setLastName(self, lN):
        self.lastName = lN

    def setEmail(self, em):
        self.email = em

    def setUserName(self, uName):
        self.userName = uName

    def setPassword(self, plainPassword):
        """
        Generates a salt and stores the hashed password.
        """
        self.passwordHash, self.salt = HashUtilities.hash_password(plainPassword)

    # Helper methods
    @staticmethod
    def findEmployeeID(criteria):
        # TODO: Replace with SQLite query.
        #
        # Planned DB behavior:
        # 1. Search the employees table
        # 2. Match fields based on non-empty criteria
        # 3. Return the matching employeeID if found
        # 4. Return -1 if no match exists
        return -1

    @staticmethod
    def authenticateEmployee(userName, plainPassword):
        # TODO: Replace with SQLite query.
        #
        # Planned DB behavior:
        # 1. Search the employees table for the given username
        # 2. Retrieve the stored password hash and salt
        # 3. Hash the entered password using the stored salt
        # 4. Compare hashes
        # 5. Return employeeID if login is successful
        # 6. Return -1 otherwise

        # Temporary test login
        test_salt = "AdminSalt456!"
        stored_hash = HashUtilities.hash_with_salt("admin123", test_salt)

        if userName == "admin":
            entered_hash = HashUtilities.hash_with_salt(plainPassword, test_salt)
            if entered_hash == stored_hash:
                return 1

        return -1

    # DB methods
    def createEmployeeInDB(self):
        if not self.firstName or not self.lastName or not self.email or not self.userName or not self.passwordHash:
            return False

        # TODO: Replace with SQLite insertion query.
        #
        # Planned DB behavior:
        # 1. Check whether username or email already exists
        # 2. Insert employee record into employees table
        # 3. Store passwordHash and salt
        # 4. Assign generated employeeID to this object
        # 5. Return True if insertion is successful

        return True

    def updateEmployeeInDB(self):
        if self.employeeID == -1:
            return False

        # TODO: Replace with SQLite update query.
        #
        # Planned DB behavior:
        # 1. Use employeeID to locate the record
        # 2. Update employee fields
        # 3. Return True if update succeeds

        return True

    def deleteEmployeeByID(self, employeeID):
        if employeeID == -1:
            return False

        # TODO: Replace with SQLite deletion query.
        #
        # Planned DB behavior:
        # 1. Use employeeID to locate the record
        # 2. Delete employee from database
        # 3. Return True if deletion succeeds

        return True

    def addExpenseToDB(self, amount, date, description):
        if amount < 0 or self.employeeID == -1 or not date or not description:
            return False

        self.expenses += amount

        # TODO: Replace with SQLite update query.
        #
        # Planned DB behavior:
        # 1. Insert a new expense record into the expenses table using employeeID,
        #    amount, date, and description
        # 2. Update the database's total expense value in table
        # 3. Return True if successful
        # 4. Return False if failed

        return True
