#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: v * 2 for k, v in a_dictionary.items()}


# Test cases (à retirer ou commenter avant push si l'école ne les autorise pas)
if __name__ == "__main__":
    test_cases = [
        { 'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16 },
        { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 },
        { 'John': 12 },
        {}
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print("Original:", case)
        print("Multiplied:", multiply_by_2(case))
        print("-" * 40)
