"""Övningar på iterators"""

from math import sqrt


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """

    def __init__(self):
        self.i = 0

    def __next__(self):
        self.i += 1
        return self.i ** 3

    def __iter__(self):
        return self


class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    def __init__(self):
        self.num = 1

    def _is_prime(self):
        for i in range(2, int(sqrt(self.num)) + 1):
            if self.num % i == 0:
                return False
        return True

    def __next__(self):
        self.num += 1
        while not self._is_prime():
            self.num += 1
        return self.num

    def __iter__(self):
        return self


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.lastnum = 0
        self.currnum = 1
        self.i = 0

    def __next__(self):

        if self. i == 0:
            self.i += 1
            return 0
        elif self.i == 1:
            self.i += 1
            return 1
        else:
            numberone = self.lastnum
            numbertwo = self.currnum

            self.currnum = numberone + numbertwo
            self.lastnum = numbertwo

            return self.currnum

    def __iter__(self):
        return self


class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """

    def __init__(self):
        self.i = -1
        self.letters = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het', 'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

    def __next__(self):
        try:
            self.i += 1
            return self.letters[self.i]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self

class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """

    def __init__(self, word):
        self.oword = list(word)
        self.nword = []
        self.i = -1

        self.perm(self.oword)

    def perm(self, a, b=0):
        if b != len(a):
            for x in range(b, len(a)):
                a[b], a[x] = a[x], a[b]
                self.perm(a, b+1)
                a[b], a[x] = a[x], a[b]
        else:
            self.nword.append(a[:])

    def __next__(self):
        self.i += 1
        try:
            return "".join(self.nword[self.i])
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """

    def __init__(self, seq):
        self.sequence = list(str(seq))
        self.positions = {}
        self.values = []
        self.num = ""
        self.i = 0

        self.generate()

    def generate(self):

        for i, num in enumerate(self.sequence):
            self.positions[i] = num

        for item1 in self.positions.items():
            for item2 in self.positions.items():
                if item1[1] == item2[1] and not abs(item1[0] - item2[0]) > 1 and not item2[0] < item2[0]:
                    self.values.append()


        """for num in self.sequence:
            if (num, self.sequence.count(num)) not in self.values:
                self.values.append((num, self.sequence.count(num)))"""

        for tupl in self.values:
            self.num += str(tupl[1]) + str(tupl[0])

    def __next__(self):

        return self.num
        raise StopIteration


    def __iter__(self):
        return self

if __name__ == "__main__":
    r = Permutations('szymon')
    for x in r:
        print(x)
