import re
import random
import string
import secrets
from collections.abc import Iterable


def shuffle(array):
    i = 3
    while i > 0:
        random.shuffle(array)
        i -= 1
    return array


def flatt_list(nest_list):
    for i in nest_list:
        if isinstance(i, Iterable) and not isinstance(i, str):
            for j in flatt_list(i):
                yield j
        else:
            yield i
    


class PassGenerator(object):

    def __init__(self):
        self.list = []
        self.password = []

    def password_generator(self):
        letters = string.ascii_letters
        simples = string.punctuation
        digits = string.digits
        keyboard = letters + simples + digits
        self.list = list(keyboard.strip(" "))

        for _ in range(20):
            uniq = random.choice(shuffle(self.list))
            self.password.append(uniq)
        user_pass = "".join(self.password)
        return user_pass

    def token_generator(self):

        samples = list(string.punctuation.strip(" "))
        self.list = list((secrets.token_urlsafe(40)).strip(" "))
        for i in range(5, len(samples), 5):
            shuffle(samples)
            self.list.insert(i, samples[i])
        return "".join(self.list)
    
    def word_generator(self):

        with open('project/static/words.txt', 'r') as text:
            lines = text.readlines()
            for _ in lines:
                # self.list.append(_)
                # print(self.list)
                re.sub(r"[^a-zA-Z0-9]+", " ", _)
                arr = list(_.split(' '))
                self.list.append(arr)
            my_arr = list(flatt_list(self.list))
            for _ in range(15):
                random_word = random.choice(shuffle(my_arr))
                self.password.append(random_word)
            return " ".join(self.password)

            
            


# x = PassGenerator()
# x.word_generator()