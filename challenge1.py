def reverseMyString(s):
    """Reverses a string while keeping non-letter 
    characters in their original positions.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string with non-letter 
        characters in their original positions.

    Examples:
        >>> reverse_letters_in_string("ab-cd")
        "dc-ba"
        >>> reverse_letters_in_string("a-bC")
        "c-ba"

    Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string!!")
    
    s = list(s)
    fromLeft = 0
    fromRight = len(s) - 1


    while fromLeft < fromRight:

        if not s[fromLeft].isalpha():
            fromLeft += 1

        elif not s[fromRight].isalpha():
            fromRight -= 1

        else:
            s[fromLeft], s[fromRight] = s[fromRight], s[fromLeft]
            fromLeft += 1
            fromRight -= 1

    return "".join(s)


