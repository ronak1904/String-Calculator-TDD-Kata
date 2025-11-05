def add(numbers: str) -> int:
    """
    Add numbers from a string.
    
    Args:
        numbers: A string containing comma-separated numbers (or custom delimiter)
        
    Returns:
        The sum of the numbers, or 0 if the string is empty
        
    Raises:
        ValueError: If any negative numbers are found
    """
    if not numbers:
        return 0
    
    # Handle custom delimiter
    delimiter = ","
    if numbers.startswith("//"):
        # Extract delimiter from format "//[delimiter]\n[numbers...]"
        end_delimiter = numbers.find("\n")
        if end_delimiter != -1:
            delimiter = numbers[2:end_delimiter]
            numbers = numbers[end_delimiter + 1:]
    
    # Replace newlines with delimiter for parsing
    numbers = numbers.replace("\n", delimiter)
    
    # Split by delimiter and convert to integers
    number_list = [int(num.strip()) for num in numbers.split(delimiter) if num.strip()]
    
    # Check for negative numbers
    negatives = [num for num in number_list if num < 0]
    if negatives:
        neg_str = ",".join(str(n) for n in negatives)
        raise ValueError(f"negative numbers not allowed {neg_str}")
    
    return sum(number_list)
