-- Example: Count books per author
SELECT author_id, COUNT(*) AS book_count
FROM books
GROUP BY author_id;
