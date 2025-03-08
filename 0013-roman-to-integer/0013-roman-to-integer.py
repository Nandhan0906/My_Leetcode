class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s) - 1):
            current_val = roman[s[i]]
            next_val = roman[s[i + 1]]
            if current_val < next_val:
                total -= current_val
            else:
                total += current_val
        total += roman[s[-1]]
        return total