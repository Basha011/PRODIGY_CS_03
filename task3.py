def check_password_complexity(password):
    # Criteria flags
    length_criteria = False
    uppercase_criteria = False
    lowercase_criteria = False
    number_criteria = False
    special_char_criteria = False

    # Check each criteria
    if len(password) >= 8:
        length_criteria = True
    for char in password:
        if char.isupper():
            uppercase_criteria = True
        elif char.islower():
            lowercase_criteria = True
        elif char.isdigit():
            number_criteria = True
        elif char in '@$!%*?&#':
            special_char_criteria = True

    # Determine strength
    criteria_met = sum(
        [length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (@, $, !, %, *, ?, &, #).")

    return strength, feedback


# Example usage
password = input('Enter the password: ')
strength, feedback = check_password_complexity(password)

print("Password Strength:", strength)
for comment in feedback:
    print(f"- {comment}")
