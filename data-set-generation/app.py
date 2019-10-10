def main():
    # filename = 'test.txt'
    filename = 'booksummaries.txt'
    file = open( filename, encoding="US-ASCII", errors='ignore')
    # erase file contents
    new_file = open( 'books.csv', 'w')
    new_file.close()
    # open to append line by line
    new_file = open("books.csv", "a")


    # manually set columns
    new_file.write( '\"wikapedia_id\"\t\"freebase_id\"\t\"book-title\"\t\"book-author\"\t\"publication-date\"\t\"genres\"\t\"plot\"\n' )
    for line in file:
        # print(line)
        new_line = ''
        counter = 0
        line = line.rstrip('\n')
        for item in line.split('\t'):
            if( item != '' ):
                counter = counter + 1
                new_line = new_line + '\"' +  item + '\"\t'
        # remove trailing ;
        new_line = new_line.rstrip( '\t' )
        # add new line for next row
        new_line = new_line + '\n'
        if counter == 7:
            new_file.write( new_line )
        else:
            print( 'dirty row ' + str(counter) )


    file.close()
    new_file.close()



if __name__ == '__main__':
    main()