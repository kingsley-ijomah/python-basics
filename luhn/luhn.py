import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        # reverse list with ::-1
        self.card_num_list = list(re.findall(r'\d', card_num)[::-1])

    def doubler(self):
        for (key, value) in enumerate(self.card_num_list):
            value = int(value)
            if key % 2 != 0:
                value = value * 2
                if value > 9: value -= 9
                yield(value)
            else:
                yield(value)

    def valid(self):
        if len(self.card_num_list) <= 1 or len(re.findall(r'[^\s\d]', self.card_num)) > 0:
            return False
        else:
            return(sum(list(self.doubler()))) % 10 == 0
