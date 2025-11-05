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
    return sum(int(part) for part in parts)
