# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='station',
            field=models.CharField(max_length=50, blank=True, null=True, choices=[('Белорусская_к', 'Белорусская_к'), ('Битцевский парк', 'Битцевский парк'), ('Кунцевская_с', 'Кунцевская_с'), ('Улица 1905 года', 'Улица 1905 года'), ('Курская (Арбатско-Покровская)', 'Курская (Арбатско-Покровская)'), ('Арбатская_с', 'Арбатская_с'), ('Новогиреево', 'Новогиреево'), ('Парк Победы_с', 'Парк Победы_с'), ('Кузнецкий мост', 'Кузнецкий мост'), ('Филёвский парк', 'Филёвский парк'), ('Динамо', 'Динамо'), ('Таганская_к', 'Таганская_к'), ('Планерная', 'Планерная'), ('Выставочная', 'Выставочная'), ('Красносельская', 'Красносельская'), ('Кропоткинская', 'Кропоткинская'), ('Комсомольская_к', 'Комсомольская_к'), ('Достоевская', 'Достоевская'), ('Чкаловская', 'Чкаловская'), ('Академическая', 'Академическая'), ('Театральная', 'Театральная'), ('Зябликово', 'Зябликово'), ('Кантемировская', 'Кантемировская'), ('Владыкино', 'Владыкино'), ('Котельники', 'Котельники'), ('Октябрьское поле', 'Октябрьское поле'), ('Китай-город_ф', 'Китай-город_ф'), ('Бауманская', 'Бауманская'), ('Боровицкая', 'Боровицкая'), ('Дубровка', 'Дубровка'), ('Домодедовская', 'Домодедовская'), ('Третьяковская_ж', 'Третьяковская_ж'), ('Петровско-Разумовская_сал', 'Петровско-Разумовская_сал'), ('Алтуфьево', 'Алтуфьево'), ('Алексеевская', 'Алексеевская'), ('Варшавская', 'Варшавская'), ('Царицыно', 'Царицыно'), ('Волоколамская', 'Волоколамская'), ('ВДНХ', 'ВДНХ'), ('Тургеневская', 'Тургеневская'), ('Лубянка', 'Лубянка'), ('Щукинская', 'Щукинская'), ('Китай-город_о', 'Китай-город_о'), ('Волгоградский проспект', 'Волгоградский проспект'), ('Спортивная', 'Спортивная'), ('Александровский сад', 'Александровский сад'), ('Водный стадион', 'Водный стадион'), ('Охотный ряд', 'Охотный ряд'), ('Беляево', 'Беляево'), ('Улица Старокачаловская', 'Улица Старокачаловская'), ('Полежаевская', 'Полежаевская'), ('Тушинская', 'Тушинская'), ('Арбатская_г', 'Арбатская_г'), ('Братиславская', 'Братиславская'), ('Шипиловская', 'Шипиловская'), ('Тропарёво', 'Тропарёво'), ('Сходненская', 'Сходненская'), ('Международная', 'Международная'), ('Первомайская', 'Первомайская'), ('Фрунзенская', 'Фрунзенская'), ('Ленинский проспект', 'Ленинский проспект'), ('Парк культуры_кр', 'Парк культуры_кр'), ('Трубная', 'Трубная'), ('Комсомольская (Сокольническая)', 'Комсомольская (Сокольническая)'), ('Крестьянская Застава', 'Крестьянская Застава'), ('Марьино', 'Марьино'), ('Технопарк', 'Технопарк'), ('Севастопольская', 'Севастопольская'), ('Университет', 'Университет'), ('Беговая', 'Беговая'), ('Электрозаводская', 'Электрозаводская'), ('Лесопарковая', 'Лесопарковая'), ('Багратионовская', 'Багратионовская'), ('Молодёжная', 'Молодёжная'), ('Бульвар Адмирала Ушакова', 'Бульвар Адмирала Ушакова'), ('Бунинская аллея', 'Бунинская аллея'), ('Проспект Мира_к', 'Проспект Мира_к'), ('Минская', 'Минская'), ('Текстильщики', 'Текстильщики'), ('Новокузнецкая', 'Новокузнецкая'), ('Полянка', 'Полянка'), ('Рязанский проспект', 'Рязанский проспект'), ('Алма-Атинская', 'Алма-Атинская'), ('Парк культуры_к', 'Парк культуры_к'), ('Красногвардейская', 'Красногвардейская'), ('Бульвар Рокоссовского', 'Бульвар Рокоссовского'), ('Студенческая', 'Студенческая'), ('Рижская', 'Рижская'), ('Лермонтовский проспект', 'Лермонтовский проспект'), ('Проспект Мира_о', 'Проспект Мира_о'), ('Библиотека им.Ленина', 'Библиотека им.Ленина'), ('Красные Ворота', 'Красные Ворота'), ('Бульвар Дмитрия Донского', 'Бульвар Дмитрия Донского'), ('Крылатское', 'Крылатское'), ('Щёлковская', 'Щёлковская'), ('Черкизовская', 'Черкизовская'), ('Тёплый Стан', 'Тёплый Стан'), ('Бутырская', 'Бутырская'), ('Киевская_с', 'Киевская_с'), ('Каширская_з', 'Каширская_з'), ('Улица Горчакова', 'Улица Горчакова'), ('Белорусская_з', 'Белорусская_з'), ('Пионерская', 'Пионерская'), ('Площадь революции', 'Площадь революции'), ('Проспект Вернадского', 'Проспект Вернадского'), ('Митино', 'Митино'), ('Пушкинская', 'Пушкинская'), ('Строгино', 'Строгино'), ('Новослободская', 'Новослободская'), ('Площадь Ильича', 'Площадь Ильича'), ('Улица Академика Янгеля', 'Улица Академика Янгеля'), ('Автозаводская', 'Автозаводская'), ('Краснопресненская', 'Краснопресненская'), ('Серпуховская', 'Серпуховская'), ('Речной вокзал', 'Речной вокзал'), ('Нагатинская', 'Нагатинская'), ('Аэропорт', 'Аэропорт'), ('Тульская', 'Тульская'), ('Свиблово', 'Свиблово'), ('Таганская_ф', 'Таганская_ф'), ('Сухаревская', 'Сухаревская'), ('Медведково', 'Медведково'), ('Сретенский бульвар', 'Сретенский бульвар'), ('Кунцевская_г', 'Кунцевская_г'), ('Пятницкое шоссе', 'Пятницкое шоссе'), ('Пролетарская', 'Пролетарская'), ('Воробьёвы горы', 'Воробьёвы горы'), ('Отрадное', 'Отрадное'), ('Шоссе Энтузиастов', 'Шоссе Энтузиастов'), ('Кузьминки', 'Кузьминки'), ('Выхино', 'Выхино'), ('Профсоюзная', 'Профсоюзная'), ('Бибирево', 'Бибирево'), ('Сокольники', 'Сокольники'), ('Каховская', 'Каховская'), ('Марьина Роща', 'Марьина Роща'), ('Сокол', 'Сокол'), ('Римская', 'Римская'), ('Калужская', 'Калужская'), ('Борисово', 'Борисово'), ('Волжская', 'Волжская'), ('Чистые пруды', 'Чистые пруды'), ('Коньково', 'Коньково'), ('Новые Черёмушки', 'Новые Черёмушки'), ('Павелецкая_к', 'Павелецкая_к'), ('Петровско-Разумовская', 'Петровско-Разумовская'), ('Нагорная', 'Нагорная'), ('Партизанская', 'Партизанская'), ('Войковская', 'Войковская'), ('Ясенево', 'Ясенево'), ('Чеховская', 'Чеховская'), ('Фонвизинская', 'Фонвизинская'), ('Чертановская', 'Чертановская'), ('Мякинино', 'Мякинино'), ('Печатники', 'Печатники'), ('Добрынинская', 'Добрынинская'), ('Павелецкая_з', 'Павелецкая_з'), ('Ломоносовский проспект', 'Ломоносовский проспект'), ('Дмитровская', 'Дмитровская'), ('Марксистская', 'Марксистская'), ('Измайловская', 'Измайловская'), ('Каширская_с', 'Каширская_с'), ('Улица Скобелевская', 'Улица Скобелевская'), ('Юго-Западная', 'Юго-Западная'), ('Третьяковская_о', 'Третьяковская_о'), ('Кутузовская', 'Кутузовская'), ('Ботанический сад', 'Ботанический сад'), ('Фили', 'Фили'), ('Смоленская_с', 'Смоленская_с'), ('Киевская_к', 'Киевская_к'), ('Деловой центр', 'Деловой центр'), ('Люблино', 'Люблино'), ('Спартак', 'Спартак'), ('Тимирязевская', 'Тимирязевская'), ('Аннино', 'Аннино'), ('Савёловская', 'Савёловская'), ('Парк Победы_ж', 'Парк Победы_ж'), ('Семёновская', 'Семёновская'), ('Менделеевская', 'Менделеевская'), ('Жулебино', 'Жулебино'), ('Коломенская', 'Коломенская'), ('Октябрьская_о', 'Октябрьская_о'), ('Пражская', 'Пражская'), ('Раменки', 'Раменки'), ('Преображенская площадь', 'Преображенская площадь'), ('Тверская', 'Тверская'), ('Славянский бульвар', 'Славянский бульвар'), ('Петровско-Разумовская_с', 'Петровско-Разумовская_с'), ('Нахимовский проспект', 'Нахимовский проспект'), ('Южная', 'Южная'), ('Новоясеневская', 'Новоясеневская'), ('Бабушкинская', 'Бабушкинская'), ('Авиамоторная', 'Авиамоторная'), ('Смоленская_г', 'Смоленская_г'), ('Курская (Кольцевая)', 'Курская (Кольцевая)'), ('Шаболовская', 'Шаболовская'), ('Саларьево', 'Саларьево'), ('Румянцево', 'Румянцево'), ('Цветной бульвар', 'Цветной бульвар'), ('Баррикадная', 'Баррикадная'), ('Орехово', 'Орехово'), ('Кожуховская', 'Кожуховская'), ('Октябрьская_к', 'Октябрьская_к'), ('Маяковская', 'Маяковская'), ('Перово', 'Перово'), ('Новокосино', 'Новокосино'), ('Киевская_г', 'Киевская_г')]),
        ),
        migrations.AlterField(
            model_name='place',
            name='metro',
            field=models.CharField(max_length=50, choices=[('Белорусская_к', 'Белорусская_к'), ('Битцевский парк', 'Битцевский парк'), ('Кунцевская_с', 'Кунцевская_с'), ('Улица 1905 года', 'Улица 1905 года'), ('Курская (Арбатско-Покровская)', 'Курская (Арбатско-Покровская)'), ('Арбатская_с', 'Арбатская_с'), ('Новогиреево', 'Новогиреево'), ('Парк Победы_с', 'Парк Победы_с'), ('Кузнецкий мост', 'Кузнецкий мост'), ('Филёвский парк', 'Филёвский парк'), ('Динамо', 'Динамо'), ('Таганская_к', 'Таганская_к'), ('Планерная', 'Планерная'), ('Выставочная', 'Выставочная'), ('Красносельская', 'Красносельская'), ('Кропоткинская', 'Кропоткинская'), ('Комсомольская_к', 'Комсомольская_к'), ('Достоевская', 'Достоевская'), ('Чкаловская', 'Чкаловская'), ('Академическая', 'Академическая'), ('Театральная', 'Театральная'), ('Зябликово', 'Зябликово'), ('Кантемировская', 'Кантемировская'), ('Владыкино', 'Владыкино'), ('Котельники', 'Котельники'), ('Октябрьское поле', 'Октябрьское поле'), ('Китай-город_ф', 'Китай-город_ф'), ('Бауманская', 'Бауманская'), ('Боровицкая', 'Боровицкая'), ('Дубровка', 'Дубровка'), ('Домодедовская', 'Домодедовская'), ('Третьяковская_ж', 'Третьяковская_ж'), ('Петровско-Разумовская_сал', 'Петровско-Разумовская_сал'), ('Алтуфьево', 'Алтуфьево'), ('Алексеевская', 'Алексеевская'), ('Варшавская', 'Варшавская'), ('Царицыно', 'Царицыно'), ('Волоколамская', 'Волоколамская'), ('ВДНХ', 'ВДНХ'), ('Тургеневская', 'Тургеневская'), ('Лубянка', 'Лубянка'), ('Щукинская', 'Щукинская'), ('Китай-город_о', 'Китай-город_о'), ('Волгоградский проспект', 'Волгоградский проспект'), ('Спортивная', 'Спортивная'), ('Александровский сад', 'Александровский сад'), ('Водный стадион', 'Водный стадион'), ('Охотный ряд', 'Охотный ряд'), ('Беляево', 'Беляево'), ('Улица Старокачаловская', 'Улица Старокачаловская'), ('Полежаевская', 'Полежаевская'), ('Тушинская', 'Тушинская'), ('Арбатская_г', 'Арбатская_г'), ('Братиславская', 'Братиславская'), ('Шипиловская', 'Шипиловская'), ('Тропарёво', 'Тропарёво'), ('Сходненская', 'Сходненская'), ('Международная', 'Международная'), ('Первомайская', 'Первомайская'), ('Фрунзенская', 'Фрунзенская'), ('Ленинский проспект', 'Ленинский проспект'), ('Парк культуры_кр', 'Парк культуры_кр'), ('Трубная', 'Трубная'), ('Комсомольская (Сокольническая)', 'Комсомольская (Сокольническая)'), ('Крестьянская Застава', 'Крестьянская Застава'), ('Марьино', 'Марьино'), ('Технопарк', 'Технопарк'), ('Севастопольская', 'Севастопольская'), ('Университет', 'Университет'), ('Беговая', 'Беговая'), ('Электрозаводская', 'Электрозаводская'), ('Лесопарковая', 'Лесопарковая'), ('Багратионовская', 'Багратионовская'), ('Молодёжная', 'Молодёжная'), ('Бульвар Адмирала Ушакова', 'Бульвар Адмирала Ушакова'), ('Бунинская аллея', 'Бунинская аллея'), ('Проспект Мира_к', 'Проспект Мира_к'), ('Минская', 'Минская'), ('Текстильщики', 'Текстильщики'), ('Новокузнецкая', 'Новокузнецкая'), ('Полянка', 'Полянка'), ('Рязанский проспект', 'Рязанский проспект'), ('Алма-Атинская', 'Алма-Атинская'), ('Парк культуры_к', 'Парк культуры_к'), ('Красногвардейская', 'Красногвардейская'), ('Бульвар Рокоссовского', 'Бульвар Рокоссовского'), ('Студенческая', 'Студенческая'), ('Рижская', 'Рижская'), ('Лермонтовский проспект', 'Лермонтовский проспект'), ('Проспект Мира_о', 'Проспект Мира_о'), ('Библиотека им.Ленина', 'Библиотека им.Ленина'), ('Красные Ворота', 'Красные Ворота'), ('Бульвар Дмитрия Донского', 'Бульвар Дмитрия Донского'), ('Крылатское', 'Крылатское'), ('Щёлковская', 'Щёлковская'), ('Черкизовская', 'Черкизовская'), ('Тёплый Стан', 'Тёплый Стан'), ('Бутырская', 'Бутырская'), ('Киевская_с', 'Киевская_с'), ('Каширская_з', 'Каширская_з'), ('Улица Горчакова', 'Улица Горчакова'), ('Белорусская_з', 'Белорусская_з'), ('Пионерская', 'Пионерская'), ('Площадь революции', 'Площадь революции'), ('Проспект Вернадского', 'Проспект Вернадского'), ('Митино', 'Митино'), ('Пушкинская', 'Пушкинская'), ('Строгино', 'Строгино'), ('Новослободская', 'Новослободская'), ('Площадь Ильича', 'Площадь Ильича'), ('Улица Академика Янгеля', 'Улица Академика Янгеля'), ('Автозаводская', 'Автозаводская'), ('Краснопресненская', 'Краснопресненская'), ('Серпуховская', 'Серпуховская'), ('Речной вокзал', 'Речной вокзал'), ('Нагатинская', 'Нагатинская'), ('Аэропорт', 'Аэропорт'), ('Тульская', 'Тульская'), ('Свиблово', 'Свиблово'), ('Таганская_ф', 'Таганская_ф'), ('Сухаревская', 'Сухаревская'), ('Медведково', 'Медведково'), ('Сретенский бульвар', 'Сретенский бульвар'), ('Кунцевская_г', 'Кунцевская_г'), ('Пятницкое шоссе', 'Пятницкое шоссе'), ('Пролетарская', 'Пролетарская'), ('Воробьёвы горы', 'Воробьёвы горы'), ('Отрадное', 'Отрадное'), ('Шоссе Энтузиастов', 'Шоссе Энтузиастов'), ('Кузьминки', 'Кузьминки'), ('Выхино', 'Выхино'), ('Профсоюзная', 'Профсоюзная'), ('Бибирево', 'Бибирево'), ('Сокольники', 'Сокольники'), ('Каховская', 'Каховская'), ('Марьина Роща', 'Марьина Роща'), ('Сокол', 'Сокол'), ('Римская', 'Римская'), ('Калужская', 'Калужская'), ('Борисово', 'Борисово'), ('Волжская', 'Волжская'), ('Чистые пруды', 'Чистые пруды'), ('Коньково', 'Коньково'), ('Новые Черёмушки', 'Новые Черёмушки'), ('Павелецкая_к', 'Павелецкая_к'), ('Петровско-Разумовская', 'Петровско-Разумовская'), ('Нагорная', 'Нагорная'), ('Партизанская', 'Партизанская'), ('Войковская', 'Войковская'), ('Ясенево', 'Ясенево'), ('Чеховская', 'Чеховская'), ('Фонвизинская', 'Фонвизинская'), ('Чертановская', 'Чертановская'), ('Мякинино', 'Мякинино'), ('Печатники', 'Печатники'), ('Добрынинская', 'Добрынинская'), ('Павелецкая_з', 'Павелецкая_з'), ('Ломоносовский проспект', 'Ломоносовский проспект'), ('Дмитровская', 'Дмитровская'), ('Марксистская', 'Марксистская'), ('Измайловская', 'Измайловская'), ('Каширская_с', 'Каширская_с'), ('Улица Скобелевская', 'Улица Скобелевская'), ('Юго-Западная', 'Юго-Западная'), ('Третьяковская_о', 'Третьяковская_о'), ('Кутузовская', 'Кутузовская'), ('Ботанический сад', 'Ботанический сад'), ('Фили', 'Фили'), ('Смоленская_с', 'Смоленская_с'), ('Киевская_к', 'Киевская_к'), ('Деловой центр', 'Деловой центр'), ('Люблино', 'Люблино'), ('Спартак', 'Спартак'), ('Тимирязевская', 'Тимирязевская'), ('Аннино', 'Аннино'), ('Савёловская', 'Савёловская'), ('Парк Победы_ж', 'Парк Победы_ж'), ('Семёновская', 'Семёновская'), ('Менделеевская', 'Менделеевская'), ('Жулебино', 'Жулебино'), ('Коломенская', 'Коломенская'), ('Октябрьская_о', 'Октябрьская_о'), ('Пражская', 'Пражская'), ('Раменки', 'Раменки'), ('Преображенская площадь', 'Преображенская площадь'), ('Тверская', 'Тверская'), ('Славянский бульвар', 'Славянский бульвар'), ('Петровско-Разумовская_с', 'Петровско-Разумовская_с'), ('Нахимовский проспект', 'Нахимовский проспект'), ('Южная', 'Южная'), ('Новоясеневская', 'Новоясеневская'), ('Бабушкинская', 'Бабушкинская'), ('Авиамоторная', 'Авиамоторная'), ('Смоленская_г', 'Смоленская_г'), ('Курская (Кольцевая)', 'Курская (Кольцевая)'), ('Шаболовская', 'Шаболовская'), ('Саларьево', 'Саларьево'), ('Румянцево', 'Румянцево'), ('Цветной бульвар', 'Цветной бульвар'), ('Баррикадная', 'Баррикадная'), ('Орехово', 'Орехово'), ('Кожуховская', 'Кожуховская'), ('Октябрьская_к', 'Октябрьская_к'), ('Маяковская', 'Маяковская'), ('Перово', 'Перово'), ('Новокосино', 'Новокосино'), ('Киевская_г', 'Киевская_г')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
    ]