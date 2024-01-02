def longest_common_prefix(strs):
    if not strs:
        return ""

    # Iterate through characters of the first string
    for i in range(len(strs[0])):
        char_to_compare = strs[0][i]

        # Compare with corresponding characters in other strings
        for string in strs[1:]:
            if i >= len(string) or string[i] != char_to_compare:
                # If a mismatch is found or the end of a string is reached, return the prefix
                return strs[0][:i]

    # If no mismatch is found, the entire first string is the common prefix
    return strs[0]

# Example usage:
string_list = ["flower", "flow", "flight"]
result = longest_common_prefix(string_list)

print("Longest Common Prefix:", result)