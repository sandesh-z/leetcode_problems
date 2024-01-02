import timeit

start = timeit.default_timer()
class Solution(object):
    def char_to_int(self, char):
        """
        Convert a Roman numeral character to an integer.
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return roman_dict[char] if char in roman_dict else 0

    def roman_to_int(self, s):
        """
        Convert a Roman numeral string to an integer.
        """
        total_sum = 0

        for index, char in enumerate(s):
            if index < len(s) - 1 and self.char_to_int(s[index]) < self.char_to_int(s[index + 1]):
                total_sum -= self.char_to_int(char)
            else:
                total_sum += self.char_to_int(char)

        return total_sum


solution = Solution()
with open("text.txt", "r") as file:
    for line in file:
        print(solution.roman_to_int(line.strip()))

stop = timeit.default_timer()

print('Time: ', stop - start) 