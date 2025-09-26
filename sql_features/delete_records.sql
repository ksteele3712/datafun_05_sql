--Delete authors by last name:
DELETE FROM authors WHERE last IN ('Orwell', 'Austen', 'Bradbury');

--Delete authors with a specific first name:
DELETE FROM authors WHERE first = 'Jane';

--Delete books by title:
DELETE FROM books WHERE title IN ('1984', 'Pride and Prejudice', 'Fahrenheit 451');

--Delete books pulished before a certain year:
DELETE FROM books WHERE year_published < 1950;

--Delete books by a specicific author:
DELETE FROM books WHERE author_id = 'A001';