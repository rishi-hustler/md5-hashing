import hashlib
import os

def md5_hash_text(text):
    """
    Generate MD5 hash of a given string
    """
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


def md5_hash_file(file_path):
    """
    Generate MD5 hash of a file
    """
    md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

    except FileNotFoundError:
        return None


def verify_file_integrity(file_path, known_hash):
    """
    Verify if file hash matches a known MD5 hash
    """
    current_hash = md5_hash_file(file_path)

    if current_hash is None:
        return None

    return current_hash == known_hash


def compare_hashes(hash1, hash2):
    """
    Compare two MD5 hashes
    """
    return hash1 == hash2


def display_menu():
    print("\n================ MD5 HASH GENERATOR =================")
    print("1. Generate MD5 hash for text")
    print("2. Generate MD5 hash for a file")
    print("3. Verify file integrity using MD5")
    print("4. Compare two MD5 hashes")
    print("5. Exit")
    print("====================================================")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            text = input("\nEnter text to hash: ")
            hash_result = md5_hash_text(text)
            print("MD5 Hash:", hash_result)

        elif choice == "2":
            file_path = input("\nEnter file path: ")

            if not os.path.exists(file_path):
                print("File does not exist.")
            else:
                hash_result = md5_hash_file(file_path)
                print("MD5 Hash of file:", hash_result)

        elif choice == "3":
            file_path = input("\nEnter file path: ")
            known_hash = input("Enter known MD5 hash: ")

            result = verify_file_integrity(file_path, known_hash)

            if result is None:
                print("File not found.")
            elif result:
                print("File integrity verified. Hashes match.")
            else:
                print("File integrity compromised. Hashes do not match.")

        elif choice == "4":
            hash1 = input("\nEnter first MD5 hash: ")
            hash2 = input("Enter second MD5 hash: ")

            if compare_hashes(hash1, hash2):
                print("Hashes are identical.")
            else:
                print("Hashes are different.")

        elif choice == "5":
            print("\nExiting MD5 Hash Generator.")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
