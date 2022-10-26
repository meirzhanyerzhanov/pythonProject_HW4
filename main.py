from typing import List
import json


class Advert:

    def __init__(self, my_dict):
        self.one_more_dict = my_dict.copy()
        if 'price' not in my_dict:
            my_dict['price'] = 0
        elif my_dict['price'] < 0:
            raise KeyError('must be >=0')
        self.text_dict = my_dict

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def return_output(self, item):
        if isinstance(item, dict):
            return Advert(item)
        else:
            return item

    def __getattr__(self, item):
        if item in self.text_dict:
            return self.return_output(self.text_dict[item])
        else:
            raise AttributeError("No category")

    def __str__(self):
        return f'{self.one_more_dict}'


if __name__ == '__main__':
    a = {
"title": "Вельш-корги",
"price": 1000,
"class": "dogs",
"location": {
"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
}
}
    lesson_ad = Advert(a)
    print(lesson_ad.class_)