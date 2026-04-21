import random

# Hash utility class for generating salts and hashing passwords
class HashUtilities:
    SALT_LENGTH = 16
    PEPPER = "Sp1c3y!"

    @staticmethod
    def hash_password(password: str):
        """
        Generates a random salt and returns:
        (hashed_password, generated_salt)
        """
        out_salt = HashUtilities.generate_salt(HashUtilities.SALT_LENGTH)
        hashed_password = HashUtilities.do_hash(out_salt, password)
        return hashed_password, out_salt

    @staticmethod
    def hash_with_salt(password: str, salt: str) -> str:
        """
        Hashes a password using an already-known salt.
        Used for login verification.
        """
        return HashUtilities.do_hash(salt, password)

    @staticmethod
    def djb2(input_string: str) -> int:
        """
        Core DJB2 hash function.
        """
        hash_value = 5381

        for char in input_string:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)

        return hash_value

    @staticmethod
    def generate_salt(length: int = SALT_LENGTH) -> str:
        """
        Generates a random salt string.
        """
        char_set = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789!@#$%^&*()"
        )

        salt = ""
        for _ in range(length):
            salt += random.choice(char_set)

        return salt

    @staticmethod
    def to_hex(hash_value: int, width: int = 8) -> str:
        """
        Converts a hash value to hexadecimal.
        """
        return format(hash_value, "x").zfill(width)

    @staticmethod
    def do_hash(salt: str, password: str) -> str:
        """
        Performs the actual salted + peppered hash calculation.
        """
        combined = salt + password + HashUtilities.PEPPER
        return HashUtilities.to_hex(HashUtilities.djb2(combined))
