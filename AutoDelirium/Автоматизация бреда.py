file = open('data/mats', 'a')


def cons_of_mats(a, b, c):
    consume = a * b
    file.write(str(consume))
    file.write(str(c))
    file.write('; ')


length = int(input('Кол-во материалов: '))
user_materials = []
i = 0
volume = float(input('Объём работы: '))
while i < length:
    material = str(input('Материал: '))
    hpp = float(input('Норма расхода: '))
    measure = str(input('Единица измерения: '))
    file.write(str(material) + ', ')
    cons_of_mats(hpp, volume, measure)
    i += 1
