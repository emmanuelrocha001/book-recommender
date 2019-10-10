import csv
import pandas
import json

class TermData:
    def __init__( self ):
        self._frequency = 1
        self._documents = []

    def incrementFrequency(self):
        self._frequency = self._frequency + 1
    def addDocument( self, doc_id ):
        if doc_id not in self._documents:
            self._documents.append( doc_id )

def main():
    dataset = pandas.read_csv( "movies.csv" )

    terms = {}
    # dataset_to_process = 1000
    dataset_to_process = len(dataset['overview'])
    dirty_files_count = 0
    for i in range( dataset_to_process ):
        if isinstance( dataset['overview'][i], str ):
            print( 'currently processing document %d' % (i) )
            for word in dataset['overview'][i].split(' '):

                # cleaning term
                # remove ,
                new_word = word.replace( ',', '' )
                # remove .
                new_word = new_word.replace( '.', '' )
                # remove 's
                new_word = new_word.replace( '\'s', '' )
                # remove trailing symbols
                new_word = new_word.strip(';')
                new_word = new_word.strip('\'')
                new_word = new_word.strip('\"')
                new_word = new_word.strip(' ')
                new_word = new_word.strip('(')
                new_word = new_word.strip(')')
                new_word = new_word.strip('[')
                new_word = new_word.strip(']')
                new_word = new_word.strip('?')
                new_word = new_word.strip('!')


                # make lowercase
                new_word = new_word.lower()


                # for item in terms.keys():
                #     print(item)
                if new_word in terms.keys():
                    terms[ new_word ].incrementFrequency()
                    terms[ new_word ].addDocument( i )

                else:
                    meta_data = TermData()
                    meta_data.addDocument( i )
                    terms.update( { new_word: meta_data })
        else:
            dirty_files_count = dirty_files_count + 1
    # make json file for terms
    data_json = {}
    data_json['terms'] = []

    for term in terms.keys():
        data_json['terms'].append({
            'word': term,
            'frequency': terms[term]._frequency,
            'documents': terms[term]._documents
        })

    # dump json file
    with open( 'terms.json', 'w' ) as outfile:
        json.dump( data_json, outfile )

    print( 'number of dirty files: %d' % dirty_files_count )
    print( 'number of terms: %d' % len(terms))
    print( 'json file successfully created' )




if __name__ == '__main__':
    main()