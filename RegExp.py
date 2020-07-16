#(\+7|8)?\s?\(?(\d{3}|\d{3})\)?(\-|\s)?(\d{3})(\-|\s)?(\d{2})(\-|\s)?(\d{2})
import re
from pprint import pprint
import csv


def compile(text1, string_to_compile, string_to_group):
    text = []
    pattern = re.compile(string_to_compile)
    for string in text1:
        text.append(pattern.sub(string_to_group, string))
    return text


def search(text, string_to_compile):
    text4 = []
    pattern = re.compile(string_to_compile)
    for i in text:
        text4.append(pattern.search(i))
    return text4


def add_to_list(text):
    new_list1 = []
    for mas in text:
        for i in mas:
            a = (i.split(','))
            new_list1.append(a)
    return new_list1


def append_name_amd_surname_to_list(text):
    text5 = []
    for i in text:  # ФИ
        text5.append(f'{i.group()}')
    return text5


# begin
with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:

    text = []
    for i in f:

        text.append(i)
############################1
pattern = re.compile(r'([А-Я][а-я]\w*)(\s?|,)([А-Я][а-я]\w*)')
text1 = []
for string in text:
    text1.append(pattern.sub(r"\1 \3", string))#1
t1 = compile(text1, r",+", r",")
#############################2
text1 = compile(t1, r"(\+7|8)?\s?\(?(\d{3}|\d{3})\)?(\-|\s)?(\d{3})(\-|\s)?(\d{2})(\-|\s)?(\d{2})", r"+7(\2)\4-\6-\8")#2
#############################3
text2 = compile(text1, r'^([А-Я][а-я]\w*)(\s?|,)([А-Я][а-я]\w*)', r"\1,\3,")
#######################################4
text3 = []
for i in text2:
    text3.append(i.replace(',,', ',').replace(',\n', '').replace('\n', ''))#4
########################################5
text5 = append_name_amd_surname_to_list(search(text3, r'^([А-Я]{1}[а-я]\w*)(,{1})([А-Я]{1}[а-я]\w*)'))
##############################################6
txt6 = compile(text3, r"\(?(доб.)(\s?)(\d*)\)?", r",\1\3")
##############################################7
A = set()
for i in text5:
    A.add(i)
#############################################8
text6 = []
for i in A:
    text6.append(i)
#########################################9
mas1 = []
for i in text6:
    mas = []
    for a in txt6:
        if i in a:
           mas.append(a)
    mas1.append(mas)
##################################10

mas_2_5 = []
for i in mas1:

    mas_1_5 = []
    if len(i) > 1:
        count = len(i)

        string = ''
        for a in i:
            string += a
            if count > 1:
                string += ','
                count -= 1
        mas_1_5.append(string)
    else:
        mas_1_5 = i
    mas_2_5.append(mas_1_5)

###################################11
mas2 = add_to_list(mas_2_5)

###################################12
mas3 = []
for i in mas2:
    mas4 = []
    for a in i:
        new_string = a.strip()
        mas4.append(new_string)
    mas3.append(mas4)

#################################13

for i in mas3:
    massive_to_check_words = i
    index_counter = 0
    words_counter = 0
    for a in massive_to_check_words:
        for z in i:
            if a == z:
                words_counter += 1
                if words_counter > 1:
                    del(i[index_counter])
            index_counter += 1
        index_counter = 0
        words_counter = 0

pprint(mas3)


# # TODO 2: сохраните получившиеся данные в другой файл

with open("phonebook.csv", "w", encoding='utf-8') as f:
   datawriter = csv.writer(f, delimiter=',')

   datawriter.writerows(mas3)

