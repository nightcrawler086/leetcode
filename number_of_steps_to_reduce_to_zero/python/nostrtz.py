class Solution1:
    def num_of_steps(self, num: int):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1

            steps += 1

        return (steps)


class Solution2:
    def num_of_steps(self, num: int):
        steps = 0
        while num > 0:
            if num & 1 == 0:
                num = num >> 1
            else:
                num = num - 1

            steps += 1

        return (steps)
