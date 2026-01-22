-- Netflix Project

DROP TABLE IF EXISTS netflix;
CREATE TABLE netflix (
	show_id VARCHAR(5),
	type VARCHAR(10),
	title VARCHAR(250),
	director VARCHAR(550),
	casts VARCHAR(1050),
	country VARCHAR(550),
	date_added VARCHAR(55),
	release_year INT,
	rating VARCHAR(15),
	duration VARCHAR(15),
	listed_in VARCHAR(250),
	description varchar(550)
)

SELECT * FROM netflix

SELECT COUNT(*) AS total_content
FROM netflix

SELECT DISTINCT type FROM netflix

-- Business problems & solutions

-- 1. Count the number of Movies vs TV Shows

-- My solution
SELECT type, COUNT(type) AS Movies_vs_TV_shows FROM netflix
GROUP BY type

-- Tutorial Solution
SELECT type, COUNT(*) AS total_content FROM netflix
GROUP BY type

-- 2. Find the most common rating for movies and TV shows

-- My solution

SELECT rating, COUNT(rating) as common_rating FROM netflix
GROUP BY rating
ORDER BY common_rating DESC

-- Tutorial solution
SELECT
	type,
	rating
FROM 
(SELECT
	type,
	rating,
	COUNT(*),
	RANK() OVER(PARTITION BY type ORDER BY COUNT(*) DESC) as ranking
	-- rating,
	-- MAX(rating)
FROM netflix
GROUP BY 1, 2) as t1
WHERE ranking = 1
-- ORDER BY 1, 3 DESC


-- 3. List all movies released in a specific year (e.g., 2020)

-- My solution

CREATE OR REPLACE FUNCTION select_all_movies_from_a_year (p_year INTEGER) 
RETURNS TABLE(title VARCHAR) 
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT net.title 
	FROM netflix net
	WHERE type = 'Movie' AND release_year = p_year;
END; 
$$;

SELECT * FROM select_all_movies_from_a_year(2020)


-- Tutorial solution
-- filter 2020
-- movies

SELECT * FROM netflix
WHERE type = 'Movie' AND release_year = 2020

-- 4. Find the top 5 countries with the most content on Netflix

-- My solution

SELECT country, COUNT(title) AS content_quant FROM netflix
WHERE country <> '[null]'
GROUP BY 1
ORDER BY content_quant DESC
LIMIT 5

-- Tutorial solution

SELECT 
	TRIM(UNNEST(STRING_TO_ARRAY(country, ','))) AS new_country,
	COUNT(show_id) AS total_content 
FROM netflix
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5

SELECT 
	UNNEST(STRING_TO_ARRAY(country, '')) AS new_country
FROM netflix

-- 5. Identify the longest movie

-- YouTube comments solution

SELECT title, substring(duration, 1, position ('m' IN duration) - 1)::int duration
FROM netflix
WHERE type = 'Movie' AND duration IS NOT NULL
-- Enhacement
ORDER BY duration DESC
LIMIT 1

-- Tutorial solution

SELECT * FROM netflix
WHERE 
	type = 'Movie'
	AND
	duration = (SELECT MAX(duration) FROM netflix)

-- 6. Find content added in the last 5 years

-- My solution

SELECT * FROM netflix
WHERE CAST(RIGHT(date_added, 4) AS NUMERIC) >= EXTRACT(YEAR FROM CURRENT_DATE) - 5

-- Tutorial solution

SELECT * FROM netflix
WHERE 
	TO_DATE(date_added, 'Month DD, YYYY') >= CURRENT_DATE - INTERVAL '5 years'

SELECT CURRENT_DATE - INTERVAL '5 years'

-- 7. Find all the movies/TV shows by director 'Rajiv Chilaka'!

-- My solution
SELECT * FROM netflix
WHERE director ILIKE '%Rajiv Chilaka%'

-- Tutorial solution

SELECT * FROM netflix
WHERE director ILIKE '%Rajiv Chilaka%'

-- 8. List all TV shows with more than 5 seasons

-- My solution

SELECT title, duration FROM netflix
WHERE duration ILIKE 'season' AND CAST(TRIM(LEFT(duration, 2)) AS NUMERIC) > 5

SELECT title, CAST(TRIM(LEFT(duration, 2)) AS NUMERIC) FROM netflix

SELECT * FROM netflix
WHERE title ILIKE 'Dick Johnson Is Dead'


-- Tutorial solution

SELECT * FROM netflix
WHERE 
	type = 'TV Show' AND
	SPLIT_PART(duration, ' ', 1)::int > 5
	-- CAST(SPLIT_PART(duration, ' ', 1) AS numeric) > 5

SELECT
	SPLIT_PART('Apple Banana Cherry', ' ', 1)

-- 9. Count the number of content items in each genre

-- My solution

SELECT 
	TRIM(UNNEST(STRING_TO_ARRAY(listed_in, ','))), 
	COUNT(show_id) FROM netflix
GROUP BY 1
ORDER BY 2 DESC

-- Tutorial solution

SELECT 
	UNNEST(STRING_TO_ARRAY(listed_in, ',')),
	COUNT(show_id) AS total_content
	-- listed_in,
FROM netflix
GROUP BY 1
ORDER BY 2 DESC

-- 10.Find each year and the average numbers of content release in India on netflix. 
-- return top 5 year with highest avg content release!

-- My solution
SELECT * FROM netflix

SELECT release_year, TRIM(UNNEST(STRING_TO_ARRAY(country, ','))), COUNT(show_id) FROM netflix
WHERE country ILIKE '%India%'
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 5

-- Tutorial solution

SELECT 
	EXTRACT(YEAR FROM TO_DATE(date_added, 'Month DD, YYYY')) AS year,
	COUNT(*) AS yearly_content,
	ROUND(COUNT(*)::numeric/(SELECT COUNT(*) FROM netflix WHERE country = 'India')::numeric * 100, 2) AS avg_content_per_year
	-- TO_DATE(date_added, 'Month DD, YYYY') AS date,
FROM netflix
WHERE country = 'India'
GROUP BY 1

-- 11. List all movies that are documentaries

-- My solution

SELECT * FROM netflix
WHERE listed_in ILIKE '%Documentaries%'

SELECT title, TRIM(UNNEST(STRING_TO_ARRAY(listed_in, ','))) AS genre FROM netflix
WHERE listed_in ILIKE '%Documentaries%'
GROUP BY 1, 2

-- Tutorial solution

SELECT * FROM netflix
WHERE listed_in ILIKE '%documentaries%'

-- 12. Find all content without a director

-- My solution

SELECT title FROM netflix
WHERE director IS NULL

-- Tutorial solution

SELECT * FROM netflix
WHERE director IS NULL

-- 13. Find how many movies actor 'Salman Khan' appeared in last 10 years!

-- My solution

SELECT * FROM netflix

SELECT title, TRIM(UNNEST(STRING_TO_ARRAY(casts, ','))), date_added FROM netflix
WHERE casts ILIKE '%Salman Khan%' AND 
TO_DATE(date_added, 'Month DD, YYYY') >= CURRENT_DATE - INTERVAL '10 years'
GROUP BY 1, 2, 3

-- Tutorial solution

SELECT * FROM netflix
WHERE 
casts ILIKE '%Salman Khan%'
AND 
release_year > EXTRACT(YEAR FROM CURRENT_DATE) - 10

-- 14. Find the top 10 actors who have appeared in the highest number of movies produced in India.

-- My solution

SELECT UNNEST(STRING_TO_ARRAY(casts, ',')), COUNT(show_id) FROM netflix
WHERE country = 'India'
GROUP BY casts
ORDER BY 2 DESC

-- Tutorial solution

SELECT
UNNEST(STRING_TO_ARRAY(casts, ',')) AS actors,
COUNT(*) total_content
FROM netflix
WHERE country ILIKE '%india%'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10

-- 15. Categorize the content based on the presence of the keywords 'kill' and 'violence' in the description field. Label content containing these keywords as 'Bad' and all other 
-- content as 'Good'. Count how many items fall into each category.

-- My solution

SELECT COUNT(show_id), title, description FROM netflix
WHERE description ILIKE '%kill%' OR description ILIKE '%violence%'
GROUP BY title, description

-- Tutorial solution
WITH new_table
AS
(SELECT *,
	CASE 
	WHEN description ILIKE '%kill%' 
	OR
	description ILIKE '%violence%' THEN 'Bad Content'
	ELSE
	'Good Content'
	END category
FROM netflix)
SELECT category, COUNT(*)
FROM new_table
GROUP BY 1

WHERE 
	description ILIKE '%kill%'
	OR 
	description ILIKE '%%violence'
