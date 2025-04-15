from typing import Iterator, Iterable


class WordsIterator(Iterator):
    def __init__(self, words: "Words"):
        self._words = words
        self.pos = 0

    def __next__(self):
        try:
            value = self._words[self.pos]
            self.pos += 1
        except IndexError:
            raise StopIteration()

        return value


class Words(Iterable):
    def __init__(self, *args: str):
        self._words = list(args)

    def __getitem__(self, index):
        return self._words[index]

    def __iter__(self):
        return WordsIterator(self)

    def append(self, w):
        self._words.append(w)


def main(words: Words):
    for w in words:
        print(w)


if __name__ == "__main__":
    words = Words("First", "Second", "Third")

    main(words)

    """
    Output:
    
    First
    Second
    Third
    """
