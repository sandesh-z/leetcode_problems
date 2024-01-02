def longest_common_prefix(strs):
    if not strs:
        return ""

    # Sort the strings to ensure that the shortest and longest strings are at the extremes
    strs.sort()

    # Take the first and last strings in the sorted list
    first_str = strs[0]
    last_str = strs[-1]

    # Compare the characters of the first and last strings
    common_prefix = ""
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix += first_str[i]
        else:
            break

    return common_prefix

# Example usage:
string_list = ["flower", "flow", "flight"]
result = longest_common_prefix(string_list)

print("Longest Common Prefix:", result)