def letters_with_even_index(string: str) -> str:
    """
    Iterate through each character of the input string. If the character is an alphabetical letter and its index in the
    alphabet is even, include it in the output string. Output should contain letters with same case as in input.

    Args:
        string (str): The input string to process.

    Returns:
        str: A string containing only the alphabetical letters from the input string that have an even index in the alphabet.

    Note:
        The alphabet is defined as "abcdefghijklmnopqrstuvwxyz".
        Indexing of the alphabet starts from zero.

    Examples:
    1. some_string("May the Force be with you.") returns "Mayeoceewiyou"
    2. some_string("Hello World!") returns "eoWo"
    3. some_string("At least java is simple!") returns "Aeasaaissime"

    :param string: The input string to process
    :return: A string containing only the alphabetical letters from the input string that have an even index in the alphabet.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""

    for letter in string:
        if letter.lower() in alphabet:
            if alphabet.index(letter.lower()) % 2 == 0:
                output += letter
    return output
