import json
import numpy
from helpers.numpy_array_encoder import NumpyArrayEncoder


def serialize_encodings(encodings: list[numpy.ndarray]) -> str:
    """turn face encodings to json string"""
    return json.dumps(encodings, cls=NumpyArrayEncoder)

def serialize_encoding(encoding: numpy.ndarray) -> str:
    """turn a single face encoding to json string"""
    return json.dumps(encoding, cls=NumpyArrayEncoder)

def deserialize_encodings(json_str: str) -> list[numpy.ndarray]:
    """turn serialized json face encodings to original face encodings"""
    decoded_encodings: list[list] = json.loads(json_str)
    for index, encoding in enumerate(decoded_encodings):
        decoded_encodings[index] = numpy.asarray(encoding)
    return decoded_encodings

def deserialize_encoding(json_str: str) -> numpy.ndarray:
    """turn a single serialized json face encodings to original face encoding"""
    return numpy.asarray(json.loads(json_str))
