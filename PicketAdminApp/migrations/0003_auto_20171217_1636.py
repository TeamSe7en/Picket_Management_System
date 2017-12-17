# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0002_auto_20171215_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='patronymic',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='spot',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='station',
            field=models.CharField(max_length=50, blank=True, null=True, choices=[('Баррикадная', 'Баррикадная'), ('Бульвар Дмитрия Донского', 'Бульвар Дмитрия Донского'), ('Румянцево', 'Румянцево'), ('Каширская_с', 'Каширская_с'), ('Щёлковская', 'Щёлковская'), ('Деловой центр', 'Деловой центр'), ('Ломоносовский проспект', 'Ломоносовский проспект'), ('Сретенский бульвар', 'Сретенский бульвар'), ('Беговая', 'Беговая'), ('Киевская_г', 'Киевская_г'), ('Юго-Западная', 'Юго-Западная'), ('Киевская_с', 'Киевская_с'), ('Улица Скобелевская', 'Улица Скобелевская'), ('Жулебино', 'Жулебино'), ('Зябликово', 'Зябликово'), ('Проспект Мира_о', 'Проспект Мира_о'), ('Алма-Атинская', 'Алма-Атинская'), ('Кунцевская_г', 'Кунцевская_г'), ('Медведково', 'Медведково'), ('Киевская_к', 'Киевская_к'), ('Шоссе Энтузиастов', 'Шоссе Энтузиастов'), ('Александровский сад', 'Александровский сад'), ('Южная', 'Южная'), ('Рязанский проспект', 'Рязанский проспект'), ('Котельники', 'Котельники'), ('Парк культуры_к', 'Парк культуры_к'), ('Спортивная', 'Спортивная'), ('Сухаревская', 'Сухаревская'), ('Лесопарковая', 'Лесопарковая'), ('Улица Старокачаловская', 'Улица Старокачаловская'), ('Студенческая', 'Студенческая'), ('Кунцевская_с', 'Кунцевская_с'), ('Отрадное', 'Отрадное'), ('Речной вокзал', 'Речной вокзал'), ('Аннино', 'Аннино'), ('Славянский бульвар', 'Славянский бульвар'), ('Печатники', 'Печатники'), ('Трубная', 'Трубная'), ('Октябрьская_о', 'Октябрьская_о'), ('Семёновская', 'Семёновская'), ('Минская', 'Минская'), ('Охотный ряд', 'Охотный ряд'), ('Севастопольская', 'Севастопольская'), ('Курская (Арбатско-Покровская)', 'Курская (Арбатско-Покровская)'), ('Раменки', 'Раменки'), ('Динамо', 'Динамо'), ('Бульвар Рокоссовского', 'Бульвар Рокоссовского'), ('Багратионовская', 'Багратионовская'), ('Достоевская', 'Достоевская'), ('Дубровка', 'Дубровка'), ('Новоясеневская', 'Новоясеневская'), ('Красносельская', 'Красносельская'), ('Белорусская_к', 'Белорусская_к'), ('Волгоградский проспект', 'Волгоградский проспект'), ('ВДНХ', 'ВДНХ'), ('Борисово', 'Борисово'), ('Партизанская', 'Партизанская'), ('Водный стадион', 'Водный стадион'), ('Тимирязевская', 'Тимирязевская'), ('Парк Победы_ж', 'Парк Победы_ж'), ('Тропарёво', 'Тропарёво'), ('Измайловская', 'Измайловская'), ('Третьяковская_о', 'Третьяковская_о'), ('Красногвардейская', 'Красногвардейская'), ('Марксистская', 'Марксистская'), ('Китай-город_о', 'Китай-город_о'), ('Филёвский парк', 'Филёвский парк'), ('Новые Черёмушки', 'Новые Черёмушки'), ('Пушкинская', 'Пушкинская'), ('Войковская', 'Войковская'), ('Митино', 'Митино'), ('Черкизовская', 'Черкизовская'), ('Электрозаводская', 'Электрозаводская'), ('Петровско-Разумовская_с', 'Петровско-Разумовская_с'), ('Бауманская', 'Бауманская'), ('Фонвизинская', 'Фонвизинская'), ('Сходненская', 'Сходненская'), ('Боровицкая', 'Боровицкая'), ('Пражская', 'Пражская'), ('Тёплый Стан', 'Тёплый Стан'), ('Выставочная', 'Выставочная'), ('Текстильщики', 'Текстильщики'), ('Дмитровская', 'Дмитровская'), ('Пролетарская', 'Пролетарская'), ('Тверская', 'Тверская'), ('Калужская', 'Калужская'), ('Каховская', 'Каховская'), ('Коньково', 'Коньково'), ('Преображенская площадь', 'Преображенская площадь'), ('Первомайская', 'Первомайская'), ('Улица Академика Янгеля', 'Улица Академика Янгеля'), ('Волоколамская', 'Волоколамская'), ('Чертановская', 'Чертановская'), ('Братиславская', 'Братиславская'), ('Октябрьская_к', 'Октябрьская_к'), ('Каширская_з', 'Каширская_з'), ('Китай-город_ф', 'Китай-город_ф'), ('Щукинская', 'Щукинская'), ('Сокольники', 'Сокольники'), ('Комсомольская_к', 'Комсомольская_к'), ('Улица 1905 года', 'Улица 1905 года'), ('Улица Горчакова', 'Улица Горчакова'), ('Краснопресненская', 'Краснопресненская'), ('Смоленская_с', 'Смоленская_с'), ('Цветной бульвар', 'Цветной бульвар'), ('Проспект Вернадского', 'Проспект Вернадского'), ('Парк Победы_с', 'Парк Победы_с'), ('Добрынинская', 'Добрынинская'), ('Саларьево', 'Саларьево'), ('Кузьминки', 'Кузьминки'), ('Полежаевская', 'Полежаевская'), ('Марьино', 'Марьино'), ('Университет', 'Университет'), ('Рижская', 'Рижская'), ('Кутузовская', 'Кутузовская'), ('Бутырская', 'Бутырская'), ('Марьина Роща', 'Марьина Роща'), ('Петровско-Разумовская_сал', 'Петровско-Разумовская_сал'), ('Полянка', 'Полянка'), ('Мякинино', 'Мякинино'), ('Третьяковская_ж', 'Третьяковская_ж'), ('Авиамоторная', 'Авиамоторная'), ('Комсомольская (Сокольническая)', 'Комсомольская (Сокольническая)'), ('Менделеевская', 'Менделеевская'), ('Кожуховская', 'Кожуховская'), ('Октябрьское поле', 'Октябрьское поле'), ('Таганская_к', 'Таганская_к'), ('Сокол', 'Сокол'), ('Шипиловская', 'Шипиловская'), ('Кантемировская', 'Кантемировская'), ('Чеховская', 'Чеховская'), ('Нахимовский проспект', 'Нахимовский проспект'), ('Бунинская аллея', 'Бунинская аллея'), ('Кропоткинская', 'Кропоткинская'), ('Петровско-Разумовская', 'Петровско-Разумовская'), ('Битцевский парк', 'Битцевский парк'), ('Чистые пруды', 'Чистые пруды'), ('Автозаводская', 'Автозаводская'), ('Бибирево', 'Бибирево'), ('Тушинская', 'Тушинская'), ('Тургеневская', 'Тургеневская'), ('Владыкино', 'Владыкино'), ('Белорусская_з', 'Белорусская_з'), ('Технопарк', 'Технопарк'), ('Выхино', 'Выхино'), ('Коломенская', 'Коломенская'), ('Нагатинская', 'Нагатинская'), ('Ясенево', 'Ясенево'), ('Савёловская', 'Савёловская'), ('Бульвар Адмирала Ушакова', 'Бульвар Адмирала Ушакова'), ('Фрунзенская', 'Фрунзенская'), ('Площадь революции', 'Площадь революции'), ('Строгино', 'Строгино'), ('Кузнецкий мост', 'Кузнецкий мост'), ('Профсоюзная', 'Профсоюзная'), ('Новослободская', 'Новослободская'), ('Проспект Мира_к', 'Проспект Мира_к'), ('Аэропорт', 'Аэропорт'), ('Спартак', 'Спартак'), ('Алексеевская', 'Алексеевская'), ('Академическая', 'Академическая'), ('Беляево', 'Беляево'), ('Варшавская', 'Варшавская'), ('Бабушкинская', 'Бабушкинская'), ('Планерная', 'Планерная'), ('Парк культуры_кр', 'Парк культуры_кр'), ('Красные Ворота', 'Красные Ворота'), ('Фили', 'Фили'), ('Перово', 'Перово'), ('Орехово', 'Орехово'), ('Лермонтовский проспект', 'Лермонтовский проспект'), ('Новокосино', 'Новокосино'), ('Алтуфьево', 'Алтуфьево'), ('Шаболовская', 'Шаболовская'), ('Новокузнецкая', 'Новокузнецкая'), ('Домодедовская', 'Домодедовская'), ('Смоленская_г', 'Смоленская_г'), ('Царицыно', 'Царицыно'), ('Тульская', 'Тульская'), ('Курская (Кольцевая)', 'Курская (Кольцевая)'), ('Воробьёвы горы', 'Воробьёвы горы'), ('Волжская', 'Волжская'), ('Лубянка', 'Лубянка'), ('Павелецкая_з', 'Павелецкая_з'), ('Таганская_ф', 'Таганская_ф'), ('Пионерская', 'Пионерская'), ('Международная', 'Международная'), ('Свиблово', 'Свиблово'), ('Ленинский проспект', 'Ленинский проспект'), ('Люблино', 'Люблино'), ('Павелецкая_к', 'Павелецкая_к'), ('Римская', 'Римская'), ('Площадь Ильича', 'Площадь Ильича'), ('Пятницкое шоссе', 'Пятницкое шоссе'), ('Библиотека им.Ленина', 'Библиотека им.Ленина'), ('Чкаловская', 'Чкаловская'), ('Молодёжная', 'Молодёжная'), ('Серпуховская', 'Серпуховская'), ('Арбатская_с', 'Арбатская_с'), ('Арбатская_г', 'Арбатская_г'), ('Крылатское', 'Крылатское'), ('Театральная', 'Театральная'), ('Новогиреево', 'Новогиреево'), ('Маяковская', 'Маяковская'), ('Крестьянская Застава', 'Крестьянская Застава'), ('Нагорная', 'Нагорная'), ('Ботанический сад', 'Ботанический сад')]),
        ),
        migrations.AlterField(
            model_name='place',
            name='metro',
            field=models.CharField(max_length=50, choices=[('Баррикадная', 'Баррикадная'), ('Бульвар Дмитрия Донского', 'Бульвар Дмитрия Донского'), ('Румянцево', 'Румянцево'), ('Каширская_с', 'Каширская_с'), ('Щёлковская', 'Щёлковская'), ('Деловой центр', 'Деловой центр'), ('Ломоносовский проспект', 'Ломоносовский проспект'), ('Сретенский бульвар', 'Сретенский бульвар'), ('Беговая', 'Беговая'), ('Киевская_г', 'Киевская_г'), ('Юго-Западная', 'Юго-Западная'), ('Киевская_с', 'Киевская_с'), ('Улица Скобелевская', 'Улица Скобелевская'), ('Жулебино', 'Жулебино'), ('Зябликово', 'Зябликово'), ('Проспект Мира_о', 'Проспект Мира_о'), ('Алма-Атинская', 'Алма-Атинская'), ('Кунцевская_г', 'Кунцевская_г'), ('Медведково', 'Медведково'), ('Киевская_к', 'Киевская_к'), ('Шоссе Энтузиастов', 'Шоссе Энтузиастов'), ('Александровский сад', 'Александровский сад'), ('Южная', 'Южная'), ('Рязанский проспект', 'Рязанский проспект'), ('Котельники', 'Котельники'), ('Парк культуры_к', 'Парк культуры_к'), ('Спортивная', 'Спортивная'), ('Сухаревская', 'Сухаревская'), ('Лесопарковая', 'Лесопарковая'), ('Улица Старокачаловская', 'Улица Старокачаловская'), ('Студенческая', 'Студенческая'), ('Кунцевская_с', 'Кунцевская_с'), ('Отрадное', 'Отрадное'), ('Речной вокзал', 'Речной вокзал'), ('Аннино', 'Аннино'), ('Славянский бульвар', 'Славянский бульвар'), ('Печатники', 'Печатники'), ('Трубная', 'Трубная'), ('Октябрьская_о', 'Октябрьская_о'), ('Семёновская', 'Семёновская'), ('Минская', 'Минская'), ('Охотный ряд', 'Охотный ряд'), ('Севастопольская', 'Севастопольская'), ('Курская (Арбатско-Покровская)', 'Курская (Арбатско-Покровская)'), ('Раменки', 'Раменки'), ('Динамо', 'Динамо'), ('Бульвар Рокоссовского', 'Бульвар Рокоссовского'), ('Багратионовская', 'Багратионовская'), ('Достоевская', 'Достоевская'), ('Дубровка', 'Дубровка'), ('Новоясеневская', 'Новоясеневская'), ('Красносельская', 'Красносельская'), ('Белорусская_к', 'Белорусская_к'), ('Волгоградский проспект', 'Волгоградский проспект'), ('ВДНХ', 'ВДНХ'), ('Борисово', 'Борисово'), ('Партизанская', 'Партизанская'), ('Водный стадион', 'Водный стадион'), ('Тимирязевская', 'Тимирязевская'), ('Парк Победы_ж', 'Парк Победы_ж'), ('Тропарёво', 'Тропарёво'), ('Измайловская', 'Измайловская'), ('Третьяковская_о', 'Третьяковская_о'), ('Красногвардейская', 'Красногвардейская'), ('Марксистская', 'Марксистская'), ('Китай-город_о', 'Китай-город_о'), ('Филёвский парк', 'Филёвский парк'), ('Новые Черёмушки', 'Новые Черёмушки'), ('Пушкинская', 'Пушкинская'), ('Войковская', 'Войковская'), ('Митино', 'Митино'), ('Черкизовская', 'Черкизовская'), ('Электрозаводская', 'Электрозаводская'), ('Петровско-Разумовская_с', 'Петровско-Разумовская_с'), ('Бауманская', 'Бауманская'), ('Фонвизинская', 'Фонвизинская'), ('Сходненская', 'Сходненская'), ('Боровицкая', 'Боровицкая'), ('Пражская', 'Пражская'), ('Тёплый Стан', 'Тёплый Стан'), ('Выставочная', 'Выставочная'), ('Текстильщики', 'Текстильщики'), ('Дмитровская', 'Дмитровская'), ('Пролетарская', 'Пролетарская'), ('Тверская', 'Тверская'), ('Калужская', 'Калужская'), ('Каховская', 'Каховская'), ('Коньково', 'Коньково'), ('Преображенская площадь', 'Преображенская площадь'), ('Первомайская', 'Первомайская'), ('Улица Академика Янгеля', 'Улица Академика Янгеля'), ('Волоколамская', 'Волоколамская'), ('Чертановская', 'Чертановская'), ('Братиславская', 'Братиславская'), ('Октябрьская_к', 'Октябрьская_к'), ('Каширская_з', 'Каширская_з'), ('Китай-город_ф', 'Китай-город_ф'), ('Щукинская', 'Щукинская'), ('Сокольники', 'Сокольники'), ('Комсомольская_к', 'Комсомольская_к'), ('Улица 1905 года', 'Улица 1905 года'), ('Улица Горчакова', 'Улица Горчакова'), ('Краснопресненская', 'Краснопресненская'), ('Смоленская_с', 'Смоленская_с'), ('Цветной бульвар', 'Цветной бульвар'), ('Проспект Вернадского', 'Проспект Вернадского'), ('Парк Победы_с', 'Парк Победы_с'), ('Добрынинская', 'Добрынинская'), ('Саларьево', 'Саларьево'), ('Кузьминки', 'Кузьминки'), ('Полежаевская', 'Полежаевская'), ('Марьино', 'Марьино'), ('Университет', 'Университет'), ('Рижская', 'Рижская'), ('Кутузовская', 'Кутузовская'), ('Бутырская', 'Бутырская'), ('Марьина Роща', 'Марьина Роща'), ('Петровско-Разумовская_сал', 'Петровско-Разумовская_сал'), ('Полянка', 'Полянка'), ('Мякинино', 'Мякинино'), ('Третьяковская_ж', 'Третьяковская_ж'), ('Авиамоторная', 'Авиамоторная'), ('Комсомольская (Сокольническая)', 'Комсомольская (Сокольническая)'), ('Менделеевская', 'Менделеевская'), ('Кожуховская', 'Кожуховская'), ('Октябрьское поле', 'Октябрьское поле'), ('Таганская_к', 'Таганская_к'), ('Сокол', 'Сокол'), ('Шипиловская', 'Шипиловская'), ('Кантемировская', 'Кантемировская'), ('Чеховская', 'Чеховская'), ('Нахимовский проспект', 'Нахимовский проспект'), ('Бунинская аллея', 'Бунинская аллея'), ('Кропоткинская', 'Кропоткинская'), ('Петровско-Разумовская', 'Петровско-Разумовская'), ('Битцевский парк', 'Битцевский парк'), ('Чистые пруды', 'Чистые пруды'), ('Автозаводская', 'Автозаводская'), ('Бибирево', 'Бибирево'), ('Тушинская', 'Тушинская'), ('Тургеневская', 'Тургеневская'), ('Владыкино', 'Владыкино'), ('Белорусская_з', 'Белорусская_з'), ('Технопарк', 'Технопарк'), ('Выхино', 'Выхино'), ('Коломенская', 'Коломенская'), ('Нагатинская', 'Нагатинская'), ('Ясенево', 'Ясенево'), ('Савёловская', 'Савёловская'), ('Бульвар Адмирала Ушакова', 'Бульвар Адмирала Ушакова'), ('Фрунзенская', 'Фрунзенская'), ('Площадь революции', 'Площадь революции'), ('Строгино', 'Строгино'), ('Кузнецкий мост', 'Кузнецкий мост'), ('Профсоюзная', 'Профсоюзная'), ('Новослободская', 'Новослободская'), ('Проспект Мира_к', 'Проспект Мира_к'), ('Аэропорт', 'Аэропорт'), ('Спартак', 'Спартак'), ('Алексеевская', 'Алексеевская'), ('Академическая', 'Академическая'), ('Беляево', 'Беляево'), ('Варшавская', 'Варшавская'), ('Бабушкинская', 'Бабушкинская'), ('Планерная', 'Планерная'), ('Парк культуры_кр', 'Парк культуры_кр'), ('Красные Ворота', 'Красные Ворота'), ('Фили', 'Фили'), ('Перово', 'Перово'), ('Орехово', 'Орехово'), ('Лермонтовский проспект', 'Лермонтовский проспект'), ('Новокосино', 'Новокосино'), ('Алтуфьево', 'Алтуфьево'), ('Шаболовская', 'Шаболовская'), ('Новокузнецкая', 'Новокузнецкая'), ('Домодедовская', 'Домодедовская'), ('Смоленская_г', 'Смоленская_г'), ('Царицыно', 'Царицыно'), ('Тульская', 'Тульская'), ('Курская (Кольцевая)', 'Курская (Кольцевая)'), ('Воробьёвы горы', 'Воробьёвы горы'), ('Волжская', 'Волжская'), ('Лубянка', 'Лубянка'), ('Павелецкая_з', 'Павелецкая_з'), ('Таганская_ф', 'Таганская_ф'), ('Пионерская', 'Пионерская'), ('Международная', 'Международная'), ('Свиблово', 'Свиблово'), ('Ленинский проспект', 'Ленинский проспект'), ('Люблино', 'Люблино'), ('Павелецкая_к', 'Павелецкая_к'), ('Римская', 'Римская'), ('Площадь Ильича', 'Площадь Ильича'), ('Пятницкое шоссе', 'Пятницкое шоссе'), ('Библиотека им.Ленина', 'Библиотека им.Ленина'), ('Чкаловская', 'Чкаловская'), ('Молодёжная', 'Молодёжная'), ('Серпуховская', 'Серпуховская'), ('Арбатская_с', 'Арбатская_с'), ('Арбатская_г', 'Арбатская_г'), ('Крылатское', 'Крылатское'), ('Театральная', 'Театральная'), ('Новогиреево', 'Новогиреево'), ('Маяковская', 'Маяковская'), ('Крестьянская Застава', 'Крестьянская Застава'), ('Нагорная', 'Нагорная'), ('Ботанический сад', 'Ботанический сад')]),
        ),
        migrations.AlterField(
            model_name='spot',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]