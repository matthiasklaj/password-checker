import re
import sys

def check_password_strength(password):
    """Check the strength of a given password and provide detailed feedback."""
    # Define password strength criteria
    criteria = {
        'length': len(password) >= 12,
        'upper': re.search(r'[A-Z]', password) is not None,
        'lower': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }

    # Evaluate the password strength
    strength_score = sum(criteria.values())
    
    # Calculate a complexity score
    length_score = min(len(password), 20) * 0.5  # Score for length, with max 10 points
    criteria_score = strength_score * 10  # Each met criteria contributes 10 points
    complexity_score = length_score + criteria_score
    
    # Define the target complexity score
    target_score = 100
    score_needed = max(0, target_score - complexity_score)
    
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
    
    # Calculate missing criteria and suggestions
    missing_criteria = {key: not value for key, value in criteria.items() if not value}
    suggestions = []
    
    if 'length' in missing_criteria:
        suggestions.append("- Increase password length to at least 12 characters.")
    if 'upper' in missing_criteria:
        suggestions.append("- Add at least one uppercase letter.")
    if 'lower' in missing_criteria:
        suggestions.append("- Add at least one lowercase letter.")
    if 'digit' in missing_criteria:
        suggestions.append("- Add at least one digit.")
    if 'special' in missing_criteria:
        suggestions.append("- Add at least one special character.")
    
    return criteria, strength, complexity_score, suggestions, score_needed

def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password to check its strength: ")
    
    criteria, strength, complexity_score, suggestions, score_needed = check_password_strength(password)

    print("\nPassword Strength Criteria:")
    print(f"Length (>= 12 characters): {'Pass' if criteria['length'] else 'Fail'}")
    print(f"Uppercase letter: {'Pass' if criteria['upper'] else 'Fail'}")
    print(f"Lowercase letter: {'Pass' if criteria['lower'] else 'Fail'}")
    print(f"Digit: {'Pass' if criteria['digit'] else 'Fail'}")
    print(f"Special character: {'Pass' if criteria['special'] else 'Fail'}")
    
    print(f"\nPassword Strength: {strength}")
    print(f"Complexity Score: {complexity_score:.2f}")
    
    if score_needed > 0:
        print("\nSuggestions to reach a perfect score (100):")
        for suggestion in suggestions:
            print(suggestion)
        print(f"\nAdditional score needed to reach 100: {score_needed:.2f}")
    else:
        print("\nYour password is already at maximum complexity score!")

if __name__ == "__main__":
    main()
