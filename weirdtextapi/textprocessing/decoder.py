import re
from typing import Union

from .exceptions import SeparatorPositionException, SeparatorsNumberException
from .settings import SEPARATOR


class Decoder:
    """Decorder class
    Prepared for decoding text encoded by WeirdText encoder.
    """

    def decode(self, encoded_text: str) -> str:
        """Method decoding encoded text by WeirdText encoder.
        Args:
            encoded_text: Text to decoded.
        Returns:
            Decoded string.
        """
        text, words_list = self._preprocess_raw_text(encoded_text)
        # regex for finding words longer than 3 - only this words could be encoded
        words_regex = re.compile(r"[\w+]{4,}", re.U)

        # iterating through all encoded words to replace them with decoded ones
        for word in words_regex.finditer(text):
            start, end = word.span()
            current_encoded = text[start:end]

            # finding matching word from list to replace encoded one
            for i in range(len(words_list)):
                current_word = words_list[i]

                if self._is_valid_replacement(current_encoded, current_word):
                    # replacing encoded word in text with original one
                    text = text[:start] + current_word + text[end:]
                    # removing word from list as it is no more needed
                    del words_list[i]
                    break

        return text

    def _preprocess_raw_text(self, text: str) -> Union[str, list]:
        """Method preprocessing raw text passed to decoder.

        First text will be validated by checking number of separators
        and position of first one found. Than raw text will be split
        into encoded sentence (only) and list of original words.
        Args:
            text: Raw text to preprocess.
        Returns:
            Encoded sentence (only) and list of original words.
        """
        found_separators = re.finditer(SEPARATOR, text)

        separator_list = [x for x in found_separators]

        if len(separator_list) != 2:
            raise SeparatorsNumberException(
                "Encoded text does not have two separators."
            )

        if separator_list[0].span()[0] != 0:
            raise SeparatorPositionException(
                "Encoded text does not begin with proper separator."
            )

        return text[separator_list[0].span()[1] : separator_list[1].span()[0]], text[
            separator_list[1].span()[1] :
        ].split(" ")

    def _is_permutation(self, word: str, pattern: str) -> bool:
        """Method checking if word characters are permutation of pattern.

        There are two dictionaries having characters of words as keys and
        number of occurrences in word as values. If they are the same words
        are permutation of each other.
        Args:
            word: Base word.
            pattern: Pattern to compare base word with.
        Returns:
            Information if word is permutation of pattern.
        """
        return self._prepare_counting_dict(word) == self._prepare_counting_dict(pattern)

    def _prepare_counting_dict(self, word: str) -> dict:
        """Method generating dictionary from word.

        Each character is set as key and number of its occurrences is
        value.
        Args:
            word: Word to generate dictionary.
        Returns:
            Dictionary generated from word.
        """
        word_dict = {}
        for char in word:
            word_dict[char] = word_dict.setdefault(char, 0) + 1
        return word_dict

    def _is_valid_replacement(self, encoded_word: str, current_word: str) -> bool:
        """Method checking if encoded word should be replaced with current word from list.

        Each character is set as key and number of its occurrences is
        value.
        Args:
            encoded_word: Encoded word from sentence.
            current_word: Potential replacement from list.
        Returns:
            Information if current_word is proper replacement for encoded_word.
        """
        return (
            len(current_word) == len(encoded_word)
            and encoded_word[0] == current_word[0]
            and encoded_word[-1] == current_word[-1]
            and self._is_permutation(encoded_word[-1:1], current_word[-1:1])
        )
