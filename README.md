# DB-tasks

**Первое задание** заключается в проектировании БД-версии музыкального сайта. Требования следующие:

  1. На сайте должна быть возможность увидеть список музыкальных жанров.
  2. Для каждого жанра можно получить список исполнителей, которые исполняют в соответствующем жанре. 
  3. Исполнители могут петь в разных жанрах, как и одному жанру могут принадлежать несколько исполнителей.
  4. Для каждого исполнителя можно получить список его альбомов.
  5. Альбом могут выпустить несколько исполнителей вместе. Как и исполнитель может принимать участие во множестве альбомов.
  6. Для каждого альбома можно получить список треков, которые в него входят.
  7. У жанра есть название.
  8. У исполнителя есть имя (псевдоним) и жанр, в котором он исполняет.
  9. У альбома есть название, год выпуска и его исполнитель.
  10. У трека есть название, длительность и альбом, которому этот трек принадлежит.
  11. Сборник имеет название и год выпуска. В него входят различные треки из разных альбомов.
  12. Один и тот же трек может присутствовать в разных сборниках.

Полученная схема выглядит следующим образом:

![image](https://user-images.githubusercontent.com/63208434/191584662-ef278229-be73-45e8-91d8-869896ba6034.png)

* SQL-запросы, создающие спроектированную БД, представлены в файле [CREATE.sql](https://github.com/lyumos/DB-tasks/blob/main/CREATE.sql)

* SQL-nзапросы, заполняющие спроектированную БД, представлены в файле [INSERT.sql](https://github.com/lyumos/DB-tasks/blob/main/INSERT.sql)

* SQL-запросы, которые выводят информацию согласно инструкциям ниже, представлены в файле [SELECT.sql](https://github.com/lyumos/DB-tasks/blob/main/SELECT.sql)
1. название и год выхода альбомов, вышедших в 2018 году;
2. название и продолжительность самого длительного трека;
3. название треков, продолжительность которых не менее 3,5 минуты;
4. названия сборников, вышедших в период с 2018 по 2020 год включительно;
5. исполнители, чье имя состоит из 1 слова;
6. название треков, которые содержат слово "мой"/"my".

* SQL-запросы, которые выводят информацию согласно инструкциям ниже(продвинутая выборка данных), представлены в файле [SELECT_2_.sql](https://github.com/lyumos/DB-tasks/blob/main/SELECT_2_.sql)
1. количество исполнителей в каждом жанре;
2. количество треков, вошедших в альбомы 2019-2020 годов;
3. средняя продолжительность треков по каждому альбому;
4. все исполнители, которые не выпустили альбомы в 2020 году;
5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
6. название альбомов, в которых присутствуют исполнители более 1 жанра;
7. наименование треков, которые не входят в сборники;
8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
9. название альбомов, содержащих наименьшее количество треков.


**Второе задание** заключатеся в написании программы на Python для управления клиентами. Решение представлено в файле [db.py](https://github.com/lyumos/DB-tasks/blob/main/db.py).

Требуется хранить персональную информацию о клиентах:
1. имя
2. фамилия
3. email
4. телефон

При этом, телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона.

В программе представлены следующие функции для управления данными:

1. Функция, создающая структуру БД (таблицы)
2. Функция, позволяющая добавить нового клиента
3. Функция, позволяющая добавить телефон для существующего клиента
4. Функция, позволяющая изменить данные о клиенте
5. Функция, позволяющая удалить телефон для существующего клиента
6. Функция, позволяющая удалить существующего клиента
7. Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
