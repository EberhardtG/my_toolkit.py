"""
my_toolkit.py

A collection of reusable utility functions for common calculations
and string processing tasks.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Returns:
        float: The average value of the list.
        int: Returns 0 if the list is empty.
    """
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def find_max_and_min(numbers):
    """
    Find the maximum and minimum values in a list without using
    the built-in max() or min() functions.

    Returns:
        tuple: (max_value, min_value)
        tuple: (None, None) if the list is empty.
    """
    if not numbers:
        return None, None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    return largest, smallest


def count_occurrences(items, target):
    """
    Count how many times a target value appears in a list.

    Args:
        items (list): The list to search.
        target: The value to count.

    Returns:
        int: Number of occurrences of the target.
    """
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """
    Determine whether a string is a palindrome.

    Comparison is case-insensitive and ignores spaces.

    Returns:
        bool: True if the text is a palindrome, otherwise False.
    """
    text = text.replace(" ", "").lower()

    return text == text[::-1]


def create_report(title, scores):
    """
    Create a formatted report containing statistics about a list of scores.

    Uses calculate_average() and find_max_and_min() internally.

    Returns:
        str: A formatted report string.
    """
    average = calculate_average(scores)
    largest, smallest = find_max_and_min(scores)

    report = (
        f"=== {title} ===\n"
        f"Average: {average:.1f}\n"
        f"Max: {largest}\n"
        f"Min: {smallest}\n"
        f"Count: {len(scores)}"
    )

    return report


if __name__ == "__main__":
    # Required tests
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()

    print(create_report("Class Scores", test_scores))

    print("\n--- Edge Case Tests ---")

    # Empty list tests
    print("Empty average:", calculate_average([]))
    print("Empty max/min:", find_max_and_min([]))

    # Multiple occurrences
    repeated_numbers = [1, 2, 2, 2, 3, 4, 2]
    print(
        "Count of 2 in [1, 2, 2, 2, 3, 4, 2]:",
        count_occurrences(repeated_numbers, 2)
    )

    # Target not found
    print(
        "Count of 99 in test_scores:",
        count_occurrences(test_scores, 99)
    )

    # Palindrome phrase from assignment
    print(
        "'A man a plan a canal Panama' palindrome:",
        is_palindrome("A man a plan a canal Panama")
    )

    # Mixed case palindrome
    print(
        "'RaceCar' palindrome:",
        is_palindrome("RaceCar")
    )

    # Single character palindrome
    print(
        "'a' palindrome:",
        is_palindrome("a")
    )

    # Empty string palindrome
    print(
        "Empty string palindrome:",
        is_palindrome("")
    )
