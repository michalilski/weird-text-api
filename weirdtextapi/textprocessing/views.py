from django.http import JsonResponse
from django.http.response import Http404

from .decoder import Decoder
from .encoder import Encoder
from .utils import process_sentence_param

encoder = Encoder()
decoder = Decoder()


def encode(request):
    """WeirdText encoding method.
    Args:
        request: User request with sentence
        to encode.
    Returns:
        Json response with encoded text.
    """
    if request.method == "GET":
        raw_sentence = request.GET.get("data", "")
        sentence = process_sentence_param(raw_sentence)
        return JsonResponse({"encoded": encoder.encode(sentence)})
    return Http404


def decode(request):
    """WeirdText decoding method.
    Args:
        request: User request with text
        to decode.
    Returns:
        Json response with decoded text.
    """
    if request.method == "GET":
        raw_sentence = request.GET.get("data", "")
        sentence = process_sentence_param(raw_sentence)
        return JsonResponse({"decoded": decoder.decode(sentence)})
    return Http404
