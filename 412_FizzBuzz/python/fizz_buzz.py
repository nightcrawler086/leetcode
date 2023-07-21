class Solution1:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                answer.append(str(i))
            elif i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")

        return (answer)


class Solution2:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            mystr = ''
            if i % 3 != 0 and i % 5 != 0:
                mystr += str(i)
            if i % 3 == 0:
                mystr += "Fizz"
            if i % 5 == 0:
                mystr += "Buzz"

            answer.append(mystr)
        return (answer)


class Solution3:
    def fizzBuzz(self, n: int) -> list[str]:
        return [[str(i), 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + (i % 5 == 0) * 2] for i in range(1, n + 1)]
