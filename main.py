books = [ 
    {'title': 'Война и мир', 'author': 'Лев Толстой', 'year': '1985'},
    {'title': 'Дом в котором', 'author': 'Мариам Петросян', 'year': '1583'},
    {'title': 'Гарри Поттер и философский камень', 'author': 'Дж. К. Роулинг', 'year': '1987'},
    {'title': 'Тетрадь смерти', 'author': 'Цугуми Оба', 'year': '2003'},
    {'title': 'Город, в котором меня нет', 'author': 'Кэй Самбэ', 'year': '2016'},]
for i in range(len(books)):
    print(f"**Книга {i + 1}***")
    print(f"Название: {books[i]['title']}, Автор: {books[i]['author']}")
    print(f"*** {books[i]['year']}***")
    print()