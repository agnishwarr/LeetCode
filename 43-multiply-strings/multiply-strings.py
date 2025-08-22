class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle zero shortcut
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)            # lengths of inputs
        res = [0] * (m + n)                    # result array for digits

        # multiply from right to left
        for i in range(m - 1, -1, -1):         # i points into num1
            d1 = ord(num1[i]) - 48             # digit value of num1[i]
            for j in range(n - 1, -1, -1):     # j points into num2
                d2 = ord(num2[j]) - 48         # digit value of num2[j]
                mul = d1 * d2                  # product of digits
                p2 = i + j + 1                 # ones position for this pair
                p1 = i + j                     # carry position for this pair
                s = mul + res[p2]              # add existing carry at p2
                res[p2] = s % 10               # write ones digit
                res[p1] += s // 10             # add carry to p1

        # skip leading zeros
        i = 0                                  # start at the leftmost
        while i < len(res) and res[i] == 0:
            i += 1

        return "".join(str(d) for d in res[i:])  # join remaining digits