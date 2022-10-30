import keyword


class My_dict:
    """
    sets attributes and checks for reserved words
    """

    def __init__(self, my_dict: dict):
        for key, value in my_dict.items():
            key_check = key
            if keyword.iskeyword(key):
                key_check = key + '_'

            if isinstance(value, dict):
                value = My_dict(value)
            setattr(self, key_check, value)

    def __str__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin():
    """
    Changes color of output
    """

    def __str__(self):
        title = super().__dict__['title']
        price = super().__dict__['price']

        return f'\033[1;{self.repr_color_code};10m {title} | {price} ₽'


class Advert(ColorizeMixin, My_dict):
    """
    Using parent class (My_dict), imposes conditions on the attributes
    """
    repr_color_code = 33

    def __init__(self, my_dict: dict):
        super().__init__(my_dict)
        if 'price' not in self.__dict__:
            my_dict['price'] = 0
        elif my_dict['price'] < 0:
            raise KeyError('must be >=0')
        if 'title' not in self.__dict__:
            raise ValueError('must contain title')


if __name__ == '__main__':
    a = {
        "title": "Вельш-корги",
        "price": 100,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, 25"
        }
    }
    lesson_ad = Advert(a)
    print(lesson_ad)
