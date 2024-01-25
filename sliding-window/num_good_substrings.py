'''
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Time Complexity: O(n) - where n is the length of the string s, 
                        we go through each letter of the s only once
Space Complexity: O(1) - we store at most 3 characters in the char_freq_map and it does not increase
                         with respect to the input size
'''


def count_good_substrings(s: str) -> int:
    if len(s) < 3:
        # The given string has a length less than 3
        return 0
    num_good_substrings = 0

    window_start = 0
    char_freq_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_freq_map:
            char_freq_map[right_char] = 0
        char_freq_map[right_char] += 1

        # At index 2, we have our first substring of length 3
        if (window_end >= 2):
            # determine if this is a good sub_string
            if len(char_freq_map) == 3:
                num_good_substrings += 1
            left_char = s[window_start]

            char_freq_map[left_char] -= 1
            if char_freq_map[left_char] == 0:
                del char_freq_map[left_char]

            window_start += 1

    return num_good_substrings


if __name__ == "__main__":
    assert count_good_substrings(
        "abcba") == 2, "Failed on count_good_substrings('abcba')"
    assert count_good_substrings(
        "xyzzazxyz") == 4, "Failed on count_good_substrings('xyzzazxyz')"
    assert count_good_substrings(
        "xy") == 0, "Failed on count_good_substrings('xy')"
    assert count_good_substrings(
        "xxx") == 0, "Failed on count_good_substrings('xxx')"
    print("All tests passed!")
