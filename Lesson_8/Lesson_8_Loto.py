import random

class LotoCard:
    def __init__(self, player):
        self.player = player
        self.card = [['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  ']]



    def fillout_card(self):
        num_counter = 1
        my_list = []
        while num_counter < 16:
            number = random.randint(1, 90)
            if number in my_list:
                continue
            my_list.append(number)
            for i in range(9):
                similar_num_counter = 0
                for item in my_list:
                    upper_boarder = (i + 1) * 10
                    if i == 8:
                        upper_boarder = 91
                    if i * 10 <= item < upper_boarder:
                        similar_num_counter += 1
                if similar_num_counter > 3:
                    my_list.pop()
            num_counter += 1
        my_list.sort()
        for el in my_list:
            i = 0
            while i < 9:
                upper_boarder = (i + 1) * 10
                if i == 8:
                    upper_boarder = 91
                if i * 10 <= el < upper_boarder:
                    counter = [[],[],[]]
                    for j, line in enumerate(self.card):
                        for item in self.card[j]:
                            if item != '  ':
                                counter[j].append(item)
                    if len(counter[0]) >= len(counter[1]):
                        if len(counter[1]) >= len(counter[2]):
                            if self.card[2][i] == '  ':
                                self.card[2][i] = el
                            else:
                                counter[2].append(0)
                                i -= 1
                                continue
                        else:
                            if self.card[1][i] == '  ':
                                self.card[1][i] = el
                            else:
                                counter[1].append(0)
                                i -= 1
                                continue
                    else:
                        if self.card[0][i] == '  ':
                            self.card[0][i] = el
                        else:
                            counter[0].append(0)
                            i -= 1
                            continue
                i += 1
        # for i in self.card:
        #     print(i)





    def draw_card(self):
        print('-'* 9 + self.player + '-'* 10)
        for i in self.card:
            for index, j in enumerate(i):
                if j != '  ' and int(j) < 10:
                    j = ' ' + str(j)
                print(j, end=' ')
                if index % 8 == 0 and index != 0:
                    print('\n'.strip())
        print('-' * 27)


card1 = LotoCard('-Player-')
card2 = LotoCard('Computer')


card1.fillout_card()
card1.draw_card()
card2.fillout_card()
card2.draw_card()
