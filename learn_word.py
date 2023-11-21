# -*- coding: utf-8 -*-
import codecs
import random
NUMBER_REPIT_WORDS = 50
status = False
dict = {}
f = codecs.open('dict.txt', 'r', 'utf-8')
# f = codecs.open('new_word.txt', 'r', 'utf-8')
while True:
    # считываем строку
    line = f.readline()
    if not line:
        break
    status = True
    list_line = []
    list_line = line.split()
    dict[list_line[0]] = []
    copy = list_line[:]
    for i in range(1, len(copy)):
        dict[list_line[0]].append(list_line[i])
f.close()
mode = None

while mode != '3':
    mode = input('Выбери режим работы (1.Проверка 2.Запись новых слов): ')
    if mode == '2':
        y = None
        y = input('Add another NEW WORD?(Y/N): ')
        while y != 'N':
            new_word = input('Insert new word: ')
            dict[new_word] = []
            f = codecs.open('dict.txt', 'a', 'utf-8')
            if status is False:
                f.write(new_word + ' ')
            else:
                f.write('\n' + new_word + ' ')
            i = 1
            x = None
            while x != 'N':
                new_word_meaning = input('Insert one meaning of the word: ')
                dict[new_word].append(new_word_meaning)
                x = input('Add another meaning of word?(Y/N): ')
                i += 1
            for i in range(len(dict[new_word])):
                f.write(dict[new_word][i] + ' ')
            y = input('Add another NEW WORD?(Y/N): ')
        f.close()
    elif mode == '1':
        keys_sort = sorted(dict.keys())
        print(keys_sort)
        for i in range(NUMBER_REPIT_WORDS):
            test_status = False
            cur = random.randint(0, len(keys_sort) - 1)
            list_copy = dict[keys_sort[cur]][:]
            print('Введите все значения слова "' + keys_sort[cur] + '"')
            count = 0
            while list_copy:
                if count <= 2:
                    var = input('Твое значение: ')
                    test_status = False
                    for i in range(0, len(list_copy)):
                        if var == list_copy[i]:
                            print('ЕСТЬ ТАКОЕ ЗНАЧЕНИЕ!')
                            list_copy.pop(i)
                            test_status = True
                            break
                    if test_status is False:
                        count += 1
                        print('НЕТ ТАКОГО ЗНАЧЕНИЯ')
                else:
                    z = input('Нужна подсказка?(Y/N): ')
                    if z == 'Y':
                        str = 'Значения слова "' + keys_sort[cur] + '": '
                        print(str, ' ', dict[keys_sort[cur]])
                        break
                    else:
                        count = 0
    mode = input('Если хотите выйти нажмите "3" :')
print('Goodbye')
