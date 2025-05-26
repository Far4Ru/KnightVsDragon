# Богатырь против Змея Горыныча
## в процессе разработки

**Пошаговая стратегическая игра с элементами головоломки и RPG**, где игрок управляет богатырём в сражении против Змея Горыныча.  

## Особенности  
- **пошаговые бои** на клеточном поле;
- **механика атак**: размещение мечей для нанесения урона и защита от огней;
- **комбинации**: усиление урона с помощью комбинаций;
- **заклинания и предметы**: получение уникальных эффектов.

## Технологии  
- python 3;
- python arcade 3.1.0.

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
<symmary>Финальная сборка</summary>

> pyinstaller --onefile --windowed --icon=assets/icons/icon.png --add-data="assets/*:assets" main.py
</details>
