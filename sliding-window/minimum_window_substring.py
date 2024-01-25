'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string ""
'''


def find_substring(s: str, t: str) -> str:
    """Find the minimum substring in string s that contains all characters of string t"""
    if len(t) > len(s):
        return ""
    char_freq_map = {}

    # Build a frequency map for the string t
    for letter in t:
        if letter not in char_freq_map:
            char_freq_map[letter] = 0
        char_freq_map[letter] += 1

    matched = 0

    window_start = 0
    smallest_substr_start = 0
    min_length = len(s) + 1
    for window_end, right_char in enumerate(s):
        if right_char in char_freq_map:
            char_freq_map[right_char] -= 1

            if char_freq_map[right_char] >= 0:
                matched += 1
        while matched == len(t):
            if min_length > (window_end - window_start + 1):
                smallest_substr_start = window_start
                min_length = window_end - window_start + 1
            left_char = s[window_start]
            window_start += 1
            if left_char in char_freq_map:
                if char_freq_map[left_char] == 0:
                    matched -= 1
                char_freq_map[left_char] += 1

    if min_length > len(s):
        return ""
    return s[smallest_substr_start: smallest_substr_start + min_length]


if __name__ == "__main__":
    assert find_substring(
        'ab', 'a') == "a", "Failed on find_substring('ab', 'a')"
    assert find_substring(
        'abadc', 'abc') == "badc", "Failed on find_substring('abadc', 'abc')"
    assert find_substring(
        'ab', 'abc') == "", "Failed on find_substring('ab', 'abc')"
    assert find_substring(
        'abdbanc', 'abc') == 'banc', "Failed on find_substring('abdbanc', 'abc')"

    print("All tests passed!")
