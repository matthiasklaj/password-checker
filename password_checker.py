import re
import sys

def check_password_strength(password):
    """Check the strength of a given password and provide detailed feedback."""
    # Define password strength criteria
    criteria = {
        'length': len(password) >= 12,  # Increased minimum length
        'upper': re.search(r'[A-Z]', password) is not None,
        'lower': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }

    # Evaluate the password strength
    strength_score = sum(criteria.values())
    
    # Calculate a complexity score
    complexity_score = (len(password) * 0.2) + (sum(criteria.values()) * 10)
    
    # Determine password strength
    if strength_score == 5:
        strength = 'Very Strong'
    elif strength_score == 4:
        strength = 'Strong'
    elif strength_score == 3:
        strength = 'Moderate'
    elif strength_score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    
    return criteria, strength, complexity_score

def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password to check its strength: ")
    
    criteria, strength, complexity_score = check_password_strength(password)

    print("\nPassword Strength Criteria:")
    print(f"Length (>= 12 characters): {'Pass' if criteria['length'] else 'Fail'}")
    print(f"Uppercase letter: {'Pass' if criteria['upper'] else 'Fail'}")
    print(f"Lowercase letter: {'Pass' if criteria['lower'] else 'Fail'}")
    print(f"Digit: {'Pass' if criteria['digit'] else 'Fail'}")
    print(f"Special character: {'Pass' if criteria['special'] else 'Fail'}")
    
    print(f"\nPassword Strength: {strength}")
    print(f"Complexity Score: {complexity_score:.2f}")

if __name__ == "__main__":
    main()
