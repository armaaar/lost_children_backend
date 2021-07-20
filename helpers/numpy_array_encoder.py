import json
import numpy as np

class NumpyArrayEncoder(json.JSONEncoder):
    """Encoder used to serialize numpy arrays to json"""
    def default(self, o):
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        return super(NumpyArrayEncoder, self).default(o)
