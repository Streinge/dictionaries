# -*- coding: utf-8 -*-
import codecs
import random
NUMBER_REPIT_WORDS = 50
WORD_FILE_NAME = 'dict.txt'
# WORD_FILE_NAME = 'new_word.txt'
# WORD_FILE_NAME = 'repeat_word.txt'
status = False
dict = {}
f = codecs.open(WORD_FILE_NAME, 'r', 'utf-8')
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
f = codecs.open(WORD_FILE_NAME, 'w', 'utf-8')
sort_keys_dict = sorted(dict)
for i in sort_keys_dict:
    string = i
    for x in dict[i]:
        string = string + ' ' + x
    if i != sort_keys_dict[-1]:
        string += '\n'
    f.write(string)
f.close()
mode = None
dict_copy = dict.copy()
while mode != '3':
    try:
        dict = dict_copy.copy()
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
                keys_sort = sorted(dict.keys())
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
                del dict[keys_sort[cur]]
            print('ПРОВЕРКА 50 СЛОВ ЗАКОНЧИЛАСЬ')
            print('Осталось слов: ', len(dict))
    except ValueError:
        print('Кончились слова')
    mode = input('Если хотите выйти нажмите "3" :')
print('Goodbye')
