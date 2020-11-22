class Solution:
    s = ""
    def romanToInt(self, s: str) -> int:
        slov = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        length = len(self.s)
        count = 0
        while i < length:
            if i != length - 1:
                if slov[self.s[i + 1]] > slov[self.s[i]]:
                    count += slov[self.s[i + 1]] - slov[self.s[i]]
                    i += 2
                else:
                    count += slov[self.s[i]]
                    i += 1
            else:
                count += slov[self.s[i]]
                break
        return count

roman = input()
if 1 > len(roman) or len(roman) > 15:
    print("Вы ввели недопустимое количество римских цифр")
else:
    sas = Solution()
    sas.s = roman
    print(sas.romanToInt(sas.s))