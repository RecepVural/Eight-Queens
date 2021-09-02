# Eight Queens
The problem is placing Queens in the situation which queens can`t atack each other. Chess table\
is created thanks to numpy fuctions. Horizantal attacks are prevented by using indexing to place queens.\
For vertical attacks, possible columns are put to a list. For each row, column is randomly selected from\
the columns list, then used column is removed. Diagonal attacks are preventing by controlling the\
(columns+1)*row_difference and (columns-1)*row_difference. Final situaion of chess table is printed.