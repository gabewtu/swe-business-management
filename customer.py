# from hash_utilities import HashUtilities (commenting out for potential implemenatation later)


class Customer:
    class SearchCriteria:
        def __init__(self, customerID=-1, firstName="", lastName="", email="",
                     address="", phoneNumber=""):#, userName=""):
            self.customerID = customerID
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.address = address
            self.phoneNumber = phoneNumber
            #self.userName = userName

    # Constructors
    def __init__(self, fN="", lN="", pN="", addr="", email="", custID=-1):
                 #uName="", passwordHash="", salt="", custID=-1):
        self.firstName = fN
        self.lastName = lN
        self.phoneNumber = pN
        self.address = addr
        self.email = email
        self.customerID = custID
        #self.userName = uName
        #self.passwordHash = passwordHash
        #self.salt = salt
        

    # Getters
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPhoneNumber(self):
        return self.phoneNumber

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    #def getUsername(self):
        #return self.userName

    def getCustomerID(self):
        return self.customerID

    # Setters
    def setFirstName(self, fN):
        self.firstName = fN

    def setLastName(self, lN):
        self.lastName = lN

    def setPhoneNumber(self, pN):
        self.phoneNumber = pN

    def setAddress(self, addr):
        self.address = addr

    def setEmail(self, em):
        self.email = em

    #def setUsername(self, uName):
        #self.userName = uName

    #def setPassword(self, plainPassword):
        #Generates a salt and stores the hashed password.
        #self.passwordHash, self.salt = HashUtilities.hash_password(plainPassword)

    # Helper methods
    @staticmethod
    def findCustomerID(criteria):
        # TODO: Replace with SQLite query.
        #
        # Planned DB behavior:
        # 1. Search the customers table
        # 2. Match fields based on non-empty criteria
        # 3. Return the matching customerID if found
        # 4. Return -1 if no match exists
        return -1

    #Commenting out for potential implementation later
    #@staticmethod
    #def authenticateCustomer(userName, password):
        # TODO: Replace with SQLite query.
        #
        # Planned DB behavior:
        # 1. Search the customers table for the given username
        # 2. Retrieve the stored password hash and salt
        # 3. Hash the entered password using the stored salt
        # 4. Compare hashes
        # 5. Return customerID if login is successful
        # 6. Return -1 otherwise

        # Temporary test login
        #test_salt = "TestSalt123!"
        #stored_hash = HashUtilities.hash_with_salt("1234", test_salt)

        #if userName == "test@test.com":
            #entered_hash = HashUtilities.hash_with_salt(password, test_salt)
            #if entered_hash == stored_hash:
                #return 1

        #return -1

    def createCustomerInDB(self):
        # Validate required fields are provided
        if not self.firstName or not self.lastName or not self.email or not self.address: #or not self.userName or not self.passwordHash:
            return False

        # TODO: Replace with SQLite insertion query.
        #
        # Planned DB behavior:
        # 1. Check whether the username or email already exists in the database
        # 2. Insert the new customer record into the customers table
        # 3. Store the customer's passwordHash and salt in the database
        # 4. Assign the generated customerID from the database to this object
        # 5. Return True if insertion is successful
        # 6. Return False if creation fails

        return True

    def updateCustomerInDB(self):
        if self.customerID == -1:
            return False

        # TODO: Replace with SQLite update query.
        #
        # Planned DB behavior:
        # 1. Use the current object's customerID to locate the record
        # 2. Update the customer's fields
        # 3. Return True if update is successful
        # 4. Return False if the update fails

        return True

    def deleteCustomerInDB(self):
        if self.customerID == -1:
            return False

        # TODO: Replace with SQLite deletion query.
        #
        # Planned DB behavior:
        # 1. Use the current object's customerID to locate the record
        # 2. Delete the customer from the database
        # 3. Return True if deletion is successful
        # 4. Return False if deletion fails

        return True
