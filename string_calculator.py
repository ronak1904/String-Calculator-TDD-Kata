def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = numbers.split(",")
    if len(parts)>1:
        return int(parts[0]) + int(parts[1])
    return int(numbers)
