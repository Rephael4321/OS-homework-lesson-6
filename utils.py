def isDigit(value: str, name: str) -> bool:
    if value.isnumeric():
        return True
    else:
        print(f"Error: {value} is not a number. {name} has to be a number.")
        return False


def isInDict(value: int, dictionary: dict) -> bool:
    if value in dictionary:
        return True
    else:
        print(f"Error: {value} does not exist")
        return False
