import getpass
import hashlib
import requests

def hash_password(password):
    password_bytes = password.encode()
    hash_object = hashlib.sha1(password_bytes)
    hash_hex = hash_object.hexdigest().upper()
    return hash_hex

def get_leak_count(prefix, suffix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)
    
    return 0

def main():
    password = getpass.getpass("Type inn password")
    result = hash_password(password)
    prefix = result[:5]
    suffix = result[5:]
    count = get_leak_count(prefix, suffix)

    if count > 0:
        print (f'Password has been leaked {count} amount of times!')
    else:
        print("Password has not been leaked")


if __name__ == "__main__":
    main()
    input("Press enter to exit")

