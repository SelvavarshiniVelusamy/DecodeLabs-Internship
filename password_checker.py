def check_password_strength(password):
    length_ok = len(password) >= 8
    uppercase_ok = any(char.isupper() for char in password)
    number_ok = any(char.isdigit() for char in password)
    symbol_ok = any(not char.isalnum() for char in password)

    score = sum([length_ok, uppercase_ok, number_ok, symbol_ok])

    if score <= 1:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\n--- Password Strength Report ---")
    print("Password Length:", len(password))
    print("Contains uppercase letter:", uppercase_ok)
    print("Contains number:", number_ok)
    print("Contains symbol:", symbol_ok)
    print("Password Strength:", strength)


def main():
    print("=== Password Strength Checker ===")

    password = input("Enter your password: ")

    check_password_strength(password)


if __name__ == "__main__":
    main()
