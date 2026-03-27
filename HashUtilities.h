///////////////////////////////////////////////////////////////////////////////
// Author: Katie Garner
// Description: This is the specification file for password hashing utilities
//              for the COSC412 Project.
///////////////////////////////////////////////////////////////////////////////
#ifndef HASHUTILITIES_H
#define HASHUTILITIES_H

#include <string>

using namespace std;

class HashUtilities {
public:
    // Constants for readability
    static const int SALT_LENGTH = 16;

    // Description: Generates a random salt, stores it in outSalt, and returns
    //              the hashed password string.
    static string hashPassword(const string& password, string& outSalt);

    // Description: Hashes a password using a provided salt. Used for login
    //              verification when the stored salt is already known.
    static string hashWithSalt(const string& password, const string& salt);

private:
    // Description: Core DJB2 hash function.
    static unsigned long djb2(const string& input);

    // Description: Generates a random salt string.
    static string generateSalt(int length = SALT_LENGTH);

    // Description: Converts an unsigned long hash value to hexadecimal.
    static string toHex(unsigned long hash, int width = 8);

    // Description: Performs the actual salted + peppered hash calculation.
    static string doHash(const string& salt, const string& password);

    // Fixed pepper value used internally
    static const string pepper;
};

#endif