from typing import List


def is_near_match(s: str, substring: str) -> bool:
    len_s = len(s)
    len_substring = len(substring)

    # Exact match
    if s == substring:
        return True

    # Check for character substitution
    if len_s == len_substring:
        differences = sum(1 for a, b in zip(s, substring) if a != b)
        if differences == 1:
            return True

    # Check for single character deletion or addition
    if abs(len_s - len_substring) == 1:
        if len_s > len_substring:
            # Check for single character deletion in s
            for i in range(len_s):
                if s[:i] + s[i + 1:] == substring:
                    return True
        else:
            # Check for single character addition in s
            for i in range(len_substring):
                if substring[:i] + substring[i + 1:] == s:
                    return True

    return False


def search_substring_with_error(strings: List[str], substring: str) -> List[str]:
    result = []
    for s in strings:
        if substring in s or is_near_match(s, substring):
            result.append(s)
    return result


# example for test
# strings = [
#     "hello world",
#     "helo world",   # One character deletion ('l')
#     "helloo world", # One character addition ('o')
#     "hella world",  # One character substitution ('a' for 'o')
#     "searching for substrings",
#     "this is a test",
#     "substring search",
#     "example string"
# ]
#
# def main():
#     result = search_substring_with_error(strings, "hello world")
#     print(result)
#
# if __name__ == "__main__":
#     main()