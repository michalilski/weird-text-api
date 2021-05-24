import codecs


def process_sentence_param(text):
    """Method to process raw query param

    This method processes raw text to prepare
    it for encoding e.g. removing double
    backslashes.
    Args:
        text: Raw text to process.
    Returns:
        Properly decoded text from url.
    """
    text_bytes = codecs.escape_decode(text)
    return text_bytes[0].decode("utf-8")
