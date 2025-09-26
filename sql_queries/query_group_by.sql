-- Example: Group books by year published
SELECT year_published, COUNT(*) AS books_published
FROM books
GROUP BY year_published;
