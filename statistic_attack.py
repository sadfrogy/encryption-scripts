ALPH_ENG = 'abcdefghijklmnopqrstuvwxyz'
ALPH_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
TEXT = 'Text'
ALPH = ALPH_ENG

result_dict = {}

for i in range(0, len(TEXT)):
    let = TEXT[i].casefold()
    if let in ALPH:
        if let not in result_dict:
            result_dict[let] = 1
        else:
            result_dict[let] += 1

print(result_dict) 