///////////////////////////////////////////////////////////////////////////////
// Author: Katie Garner
// Description: This is the implementation file for password hashing utilities
//              for the COSC412 Project.
///////////////////////////////////////////////////////////////////////////////
#include "HashUtilities.h"
#include <iomanip>
#include <sstream>
#include <ctime>
#include <cstdlib>

const string HashUtilities::pepper = "Sp1c3y!";

// Description: Generates a random salt, stores it in outSalt, and returns
//              the hashed password string.
string HashUtilities::hashPassword(const string& password, string& outSalt) {
    // Seed the random number generator once
    static bool seeded = false;
    if (!seeded) {
        srand(static_cast<unsigned int>(time(0)));
        seeded = true;
    }

    outSalt = generateSalt(SALT_LENGTH);
    return doHash(outSalt, password);
}

// Description: Hashes a password using a provided salt. Used for login
//              verification when the stored salt is already known.
string HashUtilities::hashWithSalt(const string& password, const string& salt) {
    return doHash(salt, password);
}

// Description: Core DJB2 hash function.
unsigned long HashUtilities::djb2(const string& input) {
    unsigned long hash = 5381;

    for (char c : input) {
        hash = ((hash << 5) + hash) + c;   // hash * 33 + c
    }

    return hash;
}

// Description: Generates a random salt string.
string HashUtilities::generateSalt(int length) {
    const string charSet =
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789!@#$%^&*()";

    string salt = "";

    for (int i = 0; i < length; i++) {
        salt += charSet[rand() % charSet.length()];
    }

    return salt;
}

// Description: Converts an unsigned long hash value to hexadecimal.
string HashUtilities::toHex(unsigned long hash, int width) {
    stringstream hashCode;
    hashCode << hex << setw(width) << setfill('0') << hash;
    return hashCode.str();
}

// Description: Performs the actual salted + peppered hash calculation.
string HashUtilities::doHash(const string& salt, const string& password) {
    return toHex(djb2(salt + password + pepper));
}