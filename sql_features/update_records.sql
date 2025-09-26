--Update the genre of a book:
UPDATE books
SET genre = 'Science Fiction'
WHERE title = '1984';

--Correct the year published for a book:
UPDATE books
SET year_published = 1949
WHERE title = '1984';

--Update the last name of an author:
UPDATE authors
SET last = 'Rowling'
WHERE first = 'J.K.' AND last = 'Rolling';

--Change the first name of an author by author_id:
UPDATE authors
SET first = 'George'
WHERE author_id = 'A002';