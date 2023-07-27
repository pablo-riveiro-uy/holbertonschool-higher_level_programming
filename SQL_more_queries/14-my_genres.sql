-- Generes of a show by name

SELECT name FROM tv_genres, tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = show_id
WHERE title = "Dexter" AND genre_id = tv_genres.id
ORDER BY name;
