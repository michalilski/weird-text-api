import re
from random import shuffle
from .settings import SEPARATOR


class Encoder:
    """Encoder class
    Prepared for encoding text into WeirdText.
    """

    def encode(self, text: str) -> str:
        """Method encoding text into WeirdText.
        Args:
            text: Text to encode.
        Returns:
            Encoded string.
        """
        # find words longer than 3 - only this can be shuffled
        words_regex = re.compile(r"[\w+]{4,}", re.U)
        # list of words to concatenate with encoded sentence
        original_words = words_regex.findall(text)

        for word in words_regex.finditer(text):
            start, end = word.span()
            # insert shuffled word in place of original one
            text = text[:start] + self._shuffle_word(text[start:end]) + text[end:]

        return SEPARATOR + text + SEPARATOR + " ".join(sorted(original_words))

    def _shuffle_word(self, word: str) -> str:
        """Method shuffling inside pare of word.
        Args:
            word: Word to shuffle.
        Returns:
            Shuffled word.
        """
        shuffle_part = list(word[1:-1])
        # shuffle word part using random.shuffle
        shuffle(shuffle_part)

        # check if shuffled part is not the same as original one
        if shuffle_part == list(word[1:-1]):
            first_char = shuffle_part[0]

            # to make it different replace first letter in part with first found different
            for i in range(1, len(shuffle_part)):
                if first_char != shuffle_part[i]:
                    shuffle_part[0], shuffle_part[i] = shuffle_part[i], shuffle_part[0]
                    break

        # if returned word is the same as original, this means its inside part consists of the same letters
        return word[0] + "".join(shuffle_part) + word[-1]
