"""
This is a sample file used to learn about pylint.
It contain a function of adding numbers and print the result.
"""

def add(number1, number2):
    """
    This is a sample add function.

    Returns:
        number1 + number2
    """
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
