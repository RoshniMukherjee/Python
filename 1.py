def get_grade(score):
    if score >= 0 and score < 50:
        return "NTI"
    elif score >= 50 and score < 60:
        return "PI"
    elif score >= 60 and score < 70:
        return "I"
    elif score >= 70 and score < 80:
        return "EM"
    elif score >= 80 and score <= 100:
        return "HO"
    else:
        return "Invalid score"

# Example usage:
score = 75
grade = get_grade(score)
print("Grade:", grade)
