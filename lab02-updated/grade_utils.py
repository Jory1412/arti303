"""Utility module for computing letter grades based on a 5.00 GPA scale."""

def letter_grade(gpa):
    """Convert a numerical GPA (out of 5.00) to a letter grade."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
