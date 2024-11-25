import re

def assess_password_strength(password):
    """
    Assess the strength of a given password based on criteria.
    
    :param password: Password to be assessed (string)
    :return: A tuple containing the password strength (string) and feedback (list of issues)
    """
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should include at least one special character (e.g., @, #, $).")

    # Determine password strength
    if len(feedback) == 0:
        strength = "Strong"
    elif len(feedback) <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


if __name__ == "__main__":
    print("Password Strength Checker")
    password = input("Enter a password to check its strength: ")
    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for issue in feedback:
            print(f"- {issue}")
    else:
        print("Your password is strong. Great job!")
