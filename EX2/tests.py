from ex2 import check_if_pattern


def test_check_if_pattern():
    # Test case 1
    input_string1 = "hellohellohello"
    expected_output1 = True
    assert check_if_pattern(input_string1) == expected_output1

    # Test case 2
    input_string2 = "xyzxyzxyzxyzxxzxyzxyz"
    expected_output2 = False
    assert check_if_pattern(input_string2) == expected_output2

    # Test case 3
    input_string3 = "oopoopoopoopoopoopoop"
    expected_output3 = True
    assert check_if_pattern(input_string3) == expected_output3

    # Test case 4: Input with single character
    input_string4 = "a"
    expected_output4 = False  # Single character cannot form a pattern
    assert check_if_pattern(input_string4) == expected_output4

    # Test case 5: Input with repeating characters but not forming a pattern
    input_string5 = "aaaa"
    expected_output5 = True  # Repeating characters but not a pattern
    assert check_if_pattern(input_string5) == expected_output5

    # Test case 6: Input with non-repeating characters
    input_string6 = "abcdefghi"
    expected_output6 = False  # No repeating pattern
    assert check_if_pattern(input_string6) == expected_output6

    # Test case 6: Input with no pattern
    input_string7 = "Hello world"
    expected_output7 = False  # No repeating pattern
    assert check_if_pattern(input_string7) == expected_output7


# Run the tests
test_check_if_pattern()
