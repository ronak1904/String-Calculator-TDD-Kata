# String Calculator TDD Kata

This is a TDD (Test-Driven Development) implementation of the String Calculator kata.

## Requirements

The `add` method accepts a string of numbers and returns their sum:

1. **Empty string**: Returns 0
   - Input: `""` → Output: `0`

2. **Single number**: Returns the number
   - Input: `"1"` → Output: `1`

3. **Two numbers**: Returns the sum
   - Input: `"1,5"` → Output: `6`

4. **Multiple numbers**: Handles any amount of numbers
   - Input: `"1,2,3,4,5"` → Output: `15`

5. **Newlines**: Handles newlines between numbers (instead of commas)
   - Input: `"1\n2,3"` → Output: `6`

6. **Custom delimiters**: Supports custom delimiters via format `//[delimiter]\n[numbers...]`
   - Input: `"//;\n1;2"` → Output: `3`

7. **Negative numbers**: Throws exception with message "negative numbers not allowed <negative_number>"
   - Input: `"-1"` → Raises `ValueError: negative numbers not allowed -1`

8. **Multiple negatives**: Shows all negative numbers in exception message
   - Input: `"-1,-2,3"` → Raises `ValueError: negative numbers not allowed -1,-2`

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest test_string_calculator.py -v
```

Run with coverage:
```bash
pytest test_string_calculator.py --cov=string_calculator --cov-report=term-missing
```

## Implementation

The implementation follows TDD principles:
- Start with the simplest test case (empty string)
- Implement minimal code to pass
- Add next test case
- Refactor after each passing test
- Continue until all requirements are met
