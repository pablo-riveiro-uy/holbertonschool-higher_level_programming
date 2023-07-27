-- Filter by Genre

SELECT title FROM  tv_genres, tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy' AND tv_genres.id = tv_show_genres.genre_id
ORDER BY title ASC;