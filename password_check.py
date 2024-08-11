def password_checker(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check if the password contains both uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Password should contain both uppercase and lowercase letters."
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit."
    
    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>?,./"
    if not any(char in special_characters for char in password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

# Example usage:
password = input("Enter a password: ")
result = password_checker(password)
print(result)


