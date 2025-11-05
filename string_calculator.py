def add(numbers: str) -> int:
    if not numbers:
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        # Extract delimiter from format "//[delimiter]\n[numbers...]"
        end_delimiter = numbers.find("\n")
        if end_delimiter != -1:
            delimiter = numbers[2:end_delimiter]
            numbers = numbers[end_delimiter + 1:]
    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    number_list = [int(part) for part in parts]
    negatives = [num for num in number_list if num <0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {negatives[0]}")
    return sum(number_list  )
