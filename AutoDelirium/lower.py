file = open('data/lower', 'a')

word = "КРАНЫ БАШЕННЫЕ 10 Т 0,4582 [МАШ.-Ч], УСТАНОВКИ ДЛЯ СВАРКИ РУЧНОЙ ДУГОВОЙ (ПОСТОЯННОГО ТОКА) 0,13[МАШ.-Ч], 	СРЕДСТВА МАЛОЙ МЕХАНИЗАЦИИ 0,046 [МАШ.-Ч], ЭЛЕКТРОДЫ ДИАМЕТРОМ 2 ММ Э42А	0,00011 [Т], КОНСТРУКТИВНЫЕ ЭЛЕМЕНТЫ ВСПОМОГАТЕЛЬНОГО НАЗНАЧЕНИЯ (ДЕТАЛИ КРЕПЛЕНИЯ РЕЛЬС, ЭЛЕМЕНТЫ КРЕПЛЕНИЯ ПОДВЕСНЫХ ПОТОЛКОВ, ТРУБОПРОВОДОВ, ВОЗДУХОВОДОВ, ЗАКЛАДНЫЕ ДЕТАЛИ, ДЕТАЛИ КРЕПЛЕНИЯ СТЕНОВЫХ ПАНЕЛЕЙ, ВОРОТ, ПЕРЕПЛЕТОВ, РЕШЕТОК И Т.Д. ) МАССОЙ НЕ БОЛЕЕ 50 К 0,002 [Т], БЕТОН ТЯЖЕЛЫЙ С КРУПНОСТЬЮ ЗАПОЛНИТЕЛЯ 10 ММ И МЕНЕЕ, КЛАССА С12/15 (B15) 0,0047 [М3], РАСТВОРЫ КЛАДОЧНЫЕ ТЯЖЕЛЫЕ ЦЕМЕНТНЫЕ, МАРКИ 100  0,0055 [М3], СБОРНЫЕ ЖЕЛЕЗОБЕТОННЫЕ КОНСТРУКЦИИ (МАРКА ПО ПРОЕКТУ) (ЕД.ИЗМ.-ШТУКА)1 [ШТУКА]"


file.write(word.lower())
