def check_if_pattern(string: str) -> bool:
    """
    Your task is to implement a function named
    check_if_pattern(string) that determines whether
    a given string follows a pattern of repeating substrings.
    Note that a single character by itself is not considered a pattern,
    but repeating single characters are considered a pattern.

    Examples:
    1. check_if_pattern("hellohellohello") => True
    2. check_if_pattern("xyzxyzxyzxyzxxzxyzxyz") => False
    3. check_if_pattern("oopoopoopoopoopoopoop") => True

    :param string: The string to be analyzed for the presence of repeating patterns.
    :return: True if the string has a repeating pattern, otherwise False.
    """
