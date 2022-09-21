create table if not exists Genre (
	id SERIAL primary key,
	name VARCHAR(60) not NULL
);

create table if not exists Performer (
	id SERIAL primary key,
	name VARCHAR(60) not null 
);

create table if not exists GenresPerformers (
	genre_id INTEGER not null references Genre(id),
	performer_id INTEGER not null references Performer(id),
	constraint pk_gp primary key (genre_id, performer_id)
);

create table if not exists Album (
	id SERIAL primary key,
	title VARCHAR(60) not null,
	release_year INTEGER not null
);

create table if not exists PerformersAlbums (
	performer_id INTEGER not null references Performer(id),
	album_id INTEGER not null references Album(id),
	constraint pk_pa primary key (performer_id, album_id)
);

create table if not exists Digest (
	id SERIAL primary key,
	name VARCHAR(60) not null,
	release_year INTEGER not null
);

create table if not exists Track (
	id SERIAL primary key,
	name VARCHAR(60) not null,
	duration numeric not null,
	album_id INTEGER not null references Album(id)
);

create table if not exists DigestsTracks (
	digest_id INTEGER not null references Digest(id),
	track_id INTEGER not null references Track(id),
	constraint pk_dt primary key (digest_id, track_id)
);