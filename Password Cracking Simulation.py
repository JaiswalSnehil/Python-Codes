import hashlib

def simulate_password_cracking(hashed_password, password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            return f"Passsword cracker: {password}"
    return "Password not found"

# Example 
hashed_password_to_crack = "2c9a8d02fc17ae77e926d38fe83cbfbf"
common_passwords = ["password", "123456", "qwerty", "admin"]

result = simulate_password_cracking(hashed_password_to_crack, common_passwords)
print(result)