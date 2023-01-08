Write the function insert_instruments, which will be responsible for completing the data in the instruments table. The function should take two arguments - a connection to the database and a list of records to be entered. Test the function against the following list:

instruments = [
('guitar', 'strings', 'medium'),
('piano', 'keyboard', 'hard'),
('harp', 'strings', 'hard'),
('triangle', 'percussion', 'easy'),
('flute', 'woodwind', 'medium'),
('violin', 'string', 'medium'),
('tambourine', 'percussion', 'easy'),
('organ', 'keyboard', 'hard')]

HINT: Instead of iteration through the list, you can use the executemany cursor method.