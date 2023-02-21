alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = ''
key = [6, 27, 1, 13, 16, 32, 28, 17, 15]

for i in range(0, len(text), 3):
    print(alph[(alph.find(text[i]) * key[0] + alph.find(text[i + 1]) * key[1] + alph.find(text[i + 2]) * key[2]) % 33], end='')
    print(alph[(alph.find(text[i]) * key[3] + alph.find(text[i + 1]) * key[4] + alph.find(text[i + 2]) * key[5]) % 33], end='')
    print(alph[(alph.find(text[i]) * key[6] + alph.find(text[i + 1]) * key[7] + alph.find(text[i + 2]) * key[8]) % 33], end = ' ')

