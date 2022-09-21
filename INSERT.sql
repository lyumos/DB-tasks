insert into Genre(name)
values('Поп'),('Танцевальная'),('Электроника'),('Инди'),('R&B');

insert into Performer(name)
values('Руки вверх!'),('Sia'),('Michael Jackson'),('David Guetta'),('Radiohead'),('Hozier'),('The Weeknd'),('Rihanna');

insert into genresperformers(genre_id,performer_id)
values(1,1),(1,2),(1,3),(1,7),(1,8),(2,1),(2,3),(2,7),(2,8),(3,4),(4,5),(4,6),(5,7),(5,8);

insert into ALbum(title,release_year)
values('Сделай погромче!',1998),('Не бойся, я с тобой!',2001),('This is acting',2018),('1000 Forms of Fear',2014),('After Hours',2018),('The Highlights',2021),('Unapologetic',2018),('ANTI',2018);

insert into performersalbums(performer_id,album_id)
values(1,1),(1,2),(1,4),(2,3),(2,4),(3,1),(4,5),(4,7),(5,1),(5,3),(6,3),(6,4),(6,8),(7,5),(7,6),(8,7),(8,8),(8,3);

insert into track(name,duration,album_id)
values(' My Work',3.58,8),('Love on the Brain',2.6,7),('My Diamonds',4.2,5),('Stay',3.4,3),('Jump',3.5,4),('Крошка моя',5.2,1),('18 мне уже',2.3,2),('Blinding Lights',2.6,6),('The Hills',3.6,4),('Save my Tears',3.0,2),('Bad',4.4,3),('Beat it',6.6,2),('Who is it',3.3,5),('Black or White',3.7,7),('My Dirty Diana',2.8,8);

insert into digest(name,release_year)
values('Happiness Forever',2018),('Flash Backs',2017),('Best of the Best',2020),('Great Songs', 2016),('Old but Gold', 2019),('Hits of all times',2021),('Tracks that made my day', 2015),('Christmas Hits',2020);

insert into digeststracks(digest_id,track_id)
values(1,4),(1,5),(1,13),(2,5),(2,13),(2,6),(2,7),(3,1),(3,2),(3,3),(3,4),(3,15),(3,14),(3,12),(3,11),(3,10),(3,9),(4,5),(4,13),(5,4),(5,5),(6,8),(6,6),(6,9),(6,10),(7,6),(7,7),(8,4),(8,5);