import re
import string
import numpy as np
import pandas as pd

from os import listdir

stop_words = np.loadtxt('stop_words.csv', delimiter=',', dtype='str') # list of strings

def load_data(dir_path):
    """
    Function loads all poems from a given directory
    and then using numpy library it returns vector of stored poems

    :param dir_path: Path to directory containing data
    :returns: numpy array 
    """
    
    files = listdir(dir_path)
    data = list()
    count = 1
    
    print('Total amount of poems: ' + str(len(files)) + '\n')
    print('Loading|', end='')
    
    for file in files:
        path = dir_path + '/' + file
        with open(path, 'r', encoding='utf8') as poem:
            data.append(poem.read())
        # if count % (len(files) // 10) ==0:
        #     print('=', end='')
        count += 1
    print('>\t DONE')
    
    return np.array(data)

def is_slovak(string):
    english_words = np.loadtxt('200_CommonEnglishWords.txt', delimiter='\n', dtype='str')
    for word in english_words:
        if word in string:
            print(word, 'NIE JE SLOVENSKÉ!')
            return False
    return True
        


def remove_punctuation(string):
    punctuation = list(string.punctuation+'\n')
    print(punctuation)

    for word in punctuation:
        string = string.replace(word, '')
    return string

def get_stop_words():
    stop_words = []
    return stop_words

def remove_stop_words(string, stop_words):
    """
    Function removes stop words from string

    :param string: Single verse, type=string
    :returns: Filtered out string
    """
    string = string.lower()
    for word in stop_words:
        string = re.sub(r'\b' + word + r'\b', '', string)
    return res

if __name__ == "__main__":
    print(stop_words)
