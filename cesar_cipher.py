ALPH_ENG = 'abcdefghijklmnopqrstuvwxyz'
ALPH_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
TEXT = 'Text that you want to encrypt'
KEY = 9
ALPH = ALPH_ENG

result = ''

for i in range(0, len(TEXT)):
    let = TEXT[i].casefold()
    if let in ALPH:
        result += ALPH[(ALPH.find(let) + KEY) % len(ALPH)]
    else:
        result += let

print(result)
