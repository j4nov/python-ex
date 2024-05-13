from ex1 import letters_with_even_index


def test_letters_with_even_index():
    # Test case 1
    input_string1 = "May the Force be with you."
    expected_output1 = "Mayeoceewiyou"
    assert letters_with_even_index(input_string1) == expected_output1

    # Test case 2
    input_string2 = "Hello World!"
    expected_output2 = "eoWo"
    print(letters_with_even_index(input_string2))
    assert letters_with_even_index(input_string2) == expected_output2

    # Test case 3
    input_string3 = "At least java is simple!"
    expected_output3 = "Aeasaaissime"
    assert letters_with_even_index(input_string3) == expected_output3

    # Test case 4: Input with only odd indexed letters
    input_string4 = "bdfhjlnprtvxz"
    expected_output4 = ""
    print(letters_with_even_index(input_string4))
    assert letters_with_even_index(input_string4) == expected_output4

    # Test case 5: Input with only even indexed letters
    input_string5 = "acegikmoqsuwy"
    expected_output5 = "acegikmoqsuwy"
    print(letters_with_even_index(input_string5))
    assert letters_with_even_index(input_string5) == expected_output5


# Run the tests
test_letters_with_even_index()
