class Yatzy:
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(dice):
        counts = [dice.count(i) for i in range(1, 7)]
        if 5 in counts:
            return 50
        return 0

    @staticmethod
    def count_occurrences(dice, number):
        return dice.count(number) * number

    def ones(self):
        return self.count_occurrences(self.dice, 1)

    def twos(self):
        return self.count_occurrences(self.dice, 2)

    def threes(self):
        return self.count_occurrences(self.dice, 3)

    def fours(self):
        return self.count_occurrences(self.dice, 4)

    def fives(self):
        return self.count_occurrences(self.dice, 5)

    def sixes(self):
        return self.count_occurrences(self.dice, 6)

    @staticmethod
    def count_pairs(dice):
        counts = [dice.count(i) for i in range(1, 7)]
        for i in range(6, 0, -1):
            if counts[i - 1] >= 2:
                return i * 2
        return 0

    @staticmethod
    def score_pair(*dice):
        return Yatzy.count_pairs(dice)

    @staticmethod
    def two_pair(*dice):
        counts = [dice.count(i) for i in range(1, 7)]
        pairs = 0
        score = 0
        for i in range(6, 0, -1):
            if counts[i - 1] >= 2:
                pairs += 1
                score += i * 2
        if pairs == 2:
            return score
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        counts = [dice.count(i) for i in range(1, 7)]
        for i in range(6, 0, -1):
            if counts[i - 1] >= 4:
                return i * 4
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        counts = [dice.count(i) for i in range(1, 7)]
        for i in range(6, 0, -1):
            if counts[i - 1] >= 3:
                return i * 3
        return 0

    @staticmethod
    def small_straight(*dice):
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    @staticmethod
    def large_straight(*dice):
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    @staticmethod
    def full_house(*dice):
        counts = [dice.count(i) for i in range(1, 7)]
        if 2 in counts and 3 in counts:
            return sum(dice)
        return 0
