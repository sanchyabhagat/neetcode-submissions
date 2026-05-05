class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digit2char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i, s):
            if i == len(digits):
                res.append(s)
                return

            for c in digit2char.get(digits[i]):
                backtrack(i+1, s + c)

        if digits == "": return []
        backtrack(0, "")
        return res
        