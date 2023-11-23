import numpy as np

from poem_functions import *


dir_path = './Data'
data = load_data(dir_path)

for poem in data:
    if is_slovak(poem):
        for verse in poem.split(sep='\n\n')[1:]:
            verse = remove_punctuation(verse)
