--количество исполнителей в каждом жанре:
select genre_id, count(*) from genresperformers 
group by genre_id 
order by genre_id; 
--количество треков, вошедших в альбомы 2019-2020 годов:
select count(*) from track 
where album_id = (select id from album where release_year >= 2019 and release_year <= 2020);
--средняя продолжительность треков по каждому альбому:
select album_id,avg(duration) from track 
group by album_id 
order by album_id;
--все исполнители, которые не выпустили альбомы в 2020 году (!!в моем случае нагляднее на 2018 году!!):
select distinct p.name from performer p 
left join (select pa.performer_id, a.release_year, a.id from performersalbums pa left join album a on (a.id = pa.album_id)) tmp on (p.id = tmp.performer_id) and (tmp.release_year = 2018) 
where tmp.id is null 
order by p.name;
--названия сборников, в которых присутствует конкретный исполнитель (выберите сами) --> Rihanna:
select distinct d.name from digest d 
left join digeststracks dt on d.id = dt.digest_id 
left join track t on dt.track_id = t.id 
left join album a on t.album_id = a.id 
left join performersalbums pa on a.id = pa.album_id 
left join performer p on pa.performer_id = p.id 
where p.name like '%Rihanna%' 
order by d.name;
--название альбомов, в которых присутствуют исполнители более 1 жанра:
select a.title from album a 
left join performersalbums pa on a.id = pa.album_id 
left join performer p on pa.performer_id = p.id 
left join genresperformers gp on p.id = gp.performer_id 
left join genre g on g.id = gp.genre_id 
group by a.title 
having count(distinct g.name) > 1 
order by a.title; 
--наименование треков, которые не входят в сборники:
select t.name from track t 
left join digeststracks dt on t.id = dt.track_id
where dt.digest_id is null;
--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько):
select p.name, t.duration  from performer p 
left join performersalbums pa on pa.performer_id = p.id
left join album a on pa.album_id = a.id 
left join track t on a.id = t.album_id
group by p.name,t.duration 
having t.duration = (select min(duration) from track)
order by p.name;
--название альбомов, содержащих наименьшее количество треков:
select distinct a.title from album a 
left join track t on a.id = t.album_id
where t.album_id in (
	select album_id from track 
	group by album_id 
	having count(id) = (
		select count(id) from track 
		group by album_id 
		order by count 
		limit 1
	)
)
order by a.title;
