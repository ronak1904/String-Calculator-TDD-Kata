def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = numbers.split(",")
    return sum(int(part) for part in parts)
