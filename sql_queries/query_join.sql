-- Example: List books with author names
SELECT books.title, authors.first_name, authors.last_name
FROM books
JOIN authors ON books.author_id = authors.author_id;
