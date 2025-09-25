-- Insert authors data
INSERT INTO authors (author_id, first_name, last_name, year_born) VALUES
('10f88232-1ae7-4d88-a6a2-dfcebb22a596', 'Harper', 'Lee', NULL),
('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70', 'George', 'Orwell', NULL),
('e0b75863-866d-4db4-85c7-df9bb8ee6dab', 'F. Scott', 'Fitzgerald', NULL),
('7b144e32-7ff4-4b58-8eb0-e63dc3f9b8d', 'Aldous', 'Huxley', NULL),
('8d8107b6-1f24-481c-8a21-7d72b13b59b5', 'J.D.', 'Salinger', NULL),
('0cc3c8e4-e0c0-482f-b2f7-af87330de214', 'Ray', 'Bradbury', NULL),
('4dca0632-2c53-490c-99d5-4f6d41e56c0e', 'Jane', 'Austen', NULL),
('16f3e0a1-24cb-4ed6-a50d-509f6e367f7', 'J.R.R.', 'Tolkien', NULL),
('66cf58ab-90f1-448d-85e4-055e439e75c', 'J.K.', 'Rowling', NULL);

-- Insert books data
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('d6f83870-ff21-4a5d-90ab-26a49ab6ede1', 'To Kill a Mockingbird', 1960, '10f88232-1ae7-4d88-a6a2-dfcebb22a596'),
('6ff544f7-44d8-4f49-b8c4-cd6484f587d3', '1984', 1949, 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70'),
('f90d9fe-c44d-4d1d-b3ab-59343bf32bc2', 'The Great Gatsby', 1925, 'e0b75863-866d-4db4-85c7-df9bb8ee6dab'),
('38e35ef1-228f-4d6e-a587-bd4dc44e49c9', 'Brave New World', 1932, '7b144e32-7ff4-4b58-8eb0-e63dc3f9b8d'),
('c2a62ab4-cf5c-4246-9bf7-b2de615d4e62', 'Catcher in the Rye', 1951, '8d8107b6-1f24-481c-8a21-7d72b13b59b5'),
('3a1ad825-15e9-4a48-8eb2-bde3d46e44c9', 'Fahrenheit 451', 1953, '0cc3c8e4-e0c0-482f-b2f7-af87330de214'),
('c6679818-e509-4a6b-bc3a-979f6480edc8', 'Pride and Prejudice', 1813, '4dca0632-2c53-490c-99d5-4f6d41e56c0e'),
('be59125c-6cc2-4b3d-96f1-7257bfc8e0ef', 'The Hobbit', 1937, '16f3e0a1-24cb-4ed6-a50d-509f6e367f7');
