DROP TABLE albums;

CREATE TABLE albums(
id SERIAL PRIMARY KEY,
title VARCHAR,
artist VARCHAR
);

INSERT INTO albums (artist, title) VALUES ('Marvin Gaye', 'Whats going on');
INSERT INTO albums (artist, title) VALUES ('Stevie Wonder', 'Songs in the key of life');
INSERT INTO albums (artist, title) VALUES ('Nirvana', 'Nevermind');