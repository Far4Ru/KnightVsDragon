# Богатырь против Змея Горыныча

Пошаговая стратегическая игра с элементами головоломки и RPG, где игрок управляет богатырём в сражении против Змея Горыныча.  

<p align='center'>в процессе разработки</p>

![1 Уровень](presentation/level1.png)


- система ходов: игрок и Змей атакуют по очереди;
- механика атак: размещение мечей для нанесения урона и защита от огней;
- комбинации: усиление урона с помощью комбинаций.

<details>
<summary>Скриншоты</summary>

![Меню](presentation/menu.png)
![Диалог](presentation/dialog.png)
</details>

## Технологии  
- [Python 3](https://www.python.org/);
- [Python Arcade 3.1.0](https://api.arcade.academy/en/stable/).

## Разработка
<details>
<summary>Создание и активация виртуального окружения</summary>

> python3 -m venv venv  
> source venv/bin/activate
</details>

<details>
<summary>Установка зависимостей</summary>

> pip install -r requirements.txt
</details>

<details>
<summary>Запуск</summary>

> python3 main.py
</details>


<details>
<summary>Финальная сборка</summary>

> pyinstaller --onefile --windowed --icon=assets/icons/icon.png --add-data="assets/*:assets" main.py
</details>
