"""
Get a random string from mantras.txt (if present) and return it.
"""

import random
def get_random_mantra():
    try:
        with open("mantras.txt", "r") as f:
            lines = f.read().splitlines()
            mantra = random.choice(lines)

            return mantra
    except FileNotFoundError:
        # todo log no mantras.txt
        # do not fail
        return