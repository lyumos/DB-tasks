-- название и год выхода альбомов, вышедших в 2018 году:
select title,release_year from album where release_year = 2018;
-- название и продолжительность самого длительного трека:
select name,duration from track where duration = (select max(duration) from track);
-- название треков, продолжительность которых не менее 3,5 минуты:
select name from track where duration >= 3.5;
-- названия сборников, вышедших в период с 2018 по 2020 год включительно:
select name from digest where release_year >=2018 and release_year <=2020;
-- исполнители, чье имя состоит из 1 слова:
select name from performer where name not like '% %';
-- название треков, которые содержат слово "мой"/"my":
select name from track where name like '%my%' or name like '%My%' or name like '%мой%' or name like '%моя%';