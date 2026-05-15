# ============================================================
# CSF101 - Programming Methodology
# Assignment 2: Personal Pattern Toolkit Using Python
# File: personal_pattern_toolkit.py
# Student ID: 02250326
# Full Name: Lhawang Jigme Tobgye
# ============================================================


# -------------------------------------------------------
# Task 1: Input Validation
# Keeps asking until user enters a valid number (3–9)
# -------------------------------------------------------

def get_valid_number():
    while True:
        try:
            number = int(input("Enter a number between 3 and 9: "))
            if 3 <= number <= 9:
                return number
            else:
                print("This is an Invalid input. Please enter a number between 3 and 9.")
        except ValueError:
            print("This is an Invalid input. Please enter a valid integer or number.")


# -------------------------------------------------------
# Task 2: Generate Personal Code
# Format: FirstLetter-StudentID-LastLetter (uppercase)
# -------------------------------------------------------

def generate_personal_code(student_id, keyword):
    first_letter = keyword[0].upper()
    last_letter = keyword[-1].upper()
    personal_code = f"{first_letter}-{student_id}-{last_letter}"
    return personal_code


# -------------------------------------------------------
# Task 3: Character Frequency Using Dictionary
# Counts each character in the name (case-insensitive, no spaces)
# Time Complexity: O(n), Space Complexity: O(k) where k = unique chars
# This is to count the frequency of each character in the given name. Ignores spaces. 
# Treats upper and lowercase as the same.
# Returns a dictionary with characters as keys and counts as values.
# -------------------------------------------------------

def count_character_frequency(name):
    frequency = {}
    for char in name.lower():
        if char == ' ':
            continue  # Skip spaces
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# -------------------------------------------------------
# Task 4: Unique Vowels and Consonants
# From the full name + keyword combined
# Time Complexity: O(n), Space Complexity: O(1) – alphabet is fixed size
# This will Find unique vowels and unique consonants from the given text.
# It will also return two sorted lists: (unique_vowels, unique_consonants).
# -------------------------------------------------------

def find_unique_vowels_consonants(text):
    vowels_set = set()
    consonants_set = set()
    defined_vowels = set('aeiou')

    for char in text.lower():
        if char.isalpha():
            if char in defined_vowels:
                vowels_set.add(char)
            else:
                consonants_set.add(char)

    return sorted(vowels_set), sorted(consonants_set)


# -------------------------------------------------------
# Task 5: Stack-Based Bracket Checker
# Uses a Python list as a stack (LIFO)
# Time Complexity: O(n), Space Complexity: O(n)
# This is to Check whether the bracket expression is balanced.
# Supports: () [] {}
# Uses a list as a stack.
# Returns True if balanced, False otherwise.
# -------------------------------------------------------

def check_balanced_brackets(expression):
    stack = []
    opening = set('([{')
    closing = set(')]}')
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.append(char)  # Push onto stack
        elif char in closing:
            if not stack:
                return False  # No matching opening bracket
            top = stack.pop()  # Pop from stack
            if top != matching[char]:
                return False  # Mismatched brackets
    return len(stack) == 0  # Stack must be empty at the end


# -------------------------------------------------------
# Task 6: Queue-Based Task Simulation
# Uses a Python list as a queue (FIFO)
# Time Complexity: O(n), Space Complexity: O(n)
# This is to build a queue of tasks from the keyword characters.
# Each task is in the format: 'Analyse <char>'
# Process and print tasks in FIFO order.
# -------------------------------------------------------

def process_keyword_queue(keyword):
    queue = []

    # Enqueue: Add tasks for each character in the keyword
    for char in keyword:
        task = f"Analyse {char}"
        queue.append(task)

    # Dequeue: Process tasks in FIFO order
    print("\nQueue Processing:")
    while queue:
        task = queue.pop(0)  # Remove from the front (FIFO)
        print(f"  Processing: {task}")


# -------------------------------------------------------
# Task 7: Number Pattern Using Loops
# Prints a number triangle for a given number k
# Time Complexity: O(k²), Space Complexity: O(1)
# This is to print a number triangle pattern up to the given number. Example for number=5:
# -------------------------------------------------------

def print_number_pattern(number):
    print("\nNumber Pattern:")
    for row in range(1, number + 1):          # Outer loop: each row
        for col in range(1, row + 1):          # Inner loop: columns per row
            print(col, end=" ")
        print()  # Move to next line after each row


# -------------------------------------------------------
# Task 8: Recursive Digit Sum
# Recursively sums all digits in the Student ID
# Time Complexity: O(d) where d = number of digits, Space: O(d) call stack
# Recursively calculate the sum of digits of the student ID. Base case: single digit number returns itself. 
# Recursive case: last digit + recursive_digit_sum of remaining digits.
# -------------------------------------------------------

def recursive_digit_sum(student_id):
    n = int(student_id)  # Ensure it's an integer
    if n < 10:
        return n  # Base case: single digit
    else:
        return (n % 10) + recursive_digit_sum(str(n // 10))  # Recursive call


# -------------------------------------------------------
# Summary Display Function
# Collect all inputs and display the full program output by calling all the task functions. #
# -------------------------------------------------------

def display_summary(student_id, full_name, keyword, number, bracket_expr):
    print("\n" + "=" * 40)
    print("       MY PERSONAL PATTERN TOOLKIT")
    print("=" * 40)

    # ---- Task 2: Personal Code ----
    code = generate_personal_code(student_id, keyword)
    print(f"\nPersonal Code: {code}")

    # ---- Task 3: Character Frequency ----
    freq = count_character_frequency(full_name)
    print("\nCharacter Frequency:")
    for char, count in freq.items():
        print(f"  {char} : {count}")

    # ---- Task 4: Unique Vowels and Consonants ----
    combined_text = full_name + keyword
    vowels, consonants = find_unique_vowels_consonants(combined_text)
    print(f"\nUnique Vowels: {', '.join(vowels)}")
    print(f"Unique Consonants: {', '.join(consonants)}")

    # ---- Task 5: Bracket Checker ----
    balanced = check_balanced_brackets(bracket_expr)
    result = "Yes" if balanced else "No"
    print(f"\nBalanced Brackets: {result}")

    # ---- Task 6: Queue Processing ----
    process_keyword_queue(keyword)

    # ---- Task 7: Number Pattern ----
    print_number_pattern(number)

    # ---- Task 8: Recursive Digit Sum ----
    digit_sum = recursive_digit_sum(student_id)
    print(f"\nRecursive Digit Sum of Student ID: {digit_sum}")

    print("\n" + "=" * 40)
    print("         END OF TOOLKIT OUTPUT")
    print("=" * 40 + "\n")


# -------------------------------------------------------
# Main Program Entry Point
# The Main function: collects all user inputs and runs the toolkit. #
# -------------------------------------------------------

def main():
    print("===== Personal Pattern Toolkit =====\n")

    # Collect the inputs #
    student_id = input("Enter Your Student ID: ").strip()
    full_name = input("Enter Full Name: ").strip()
    keyword = input("Enter Unique Keyword: ").strip()

    # Task 1: Validated number input
    number = get_valid_number()

    bracket_expr = input("Enter The bracket expression: ").strip()

    # Display all results #
    display_summary(student_id, full_name, keyword, number, bracket_expr)


# Then, finallt run the program #
if __name__ == "__main__":
    main()
