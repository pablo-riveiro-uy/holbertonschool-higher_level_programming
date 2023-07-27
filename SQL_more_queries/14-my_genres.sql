-- Generes of a show by name

SELECT name FROM tv_genres
INNER JOIN tv_show INNER JOIN tv_show_genres on tv_genres.id = tv_show.genre_id
WHERE tv_genres.title = 'Comedy'
ORDER BY name ASC;
