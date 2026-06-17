# My Toolkit- Building a toolkit of reusable functions
def calculate_average(numbers):
    """Calculate the average of a list of numbers, and return 0 if the list is empty."""

    if not numbers:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)  
def find_max_and_min(numbers):
    """Find both the maximum and minimum values without using max() or min()."""

    if not numbers:
        return 0, 0

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    return largest, smallest
def count_occurrences(items, target):
    """Count occurrences without using .count()."""

    count = 0

    for item in items:
        if item == target:
            count += 1

    return count
def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and non-alphanumeric characters)."""

    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False
def create_report(title, scores):
    """Create and return a formatted report."""

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
    # Test each function
        test_scores = [85, 92, 78, 95, 88, 70, 93]
    
print(f"Average: {calculate_average(test_scores)}")
print(f"Max/Min: {find_max_and_min(test_scores)}")
print(f"Count of 85: {count_occurrences(test_scores, 85)}")
print(f"'racecar' palindrome: {is_palindrome('racecar')}")
print(f"'hello' palindrome: {is_palindrome('hello')}")
print()
print(create_report("Class Scores", test_scores))