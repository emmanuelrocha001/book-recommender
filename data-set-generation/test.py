import pandas
import numpy

def main():
    data = pandas.read_csv( 'movies_metadata.csv' )

    # cleaning csv
    to_drop = ['adult', 'original_title', 'belongs_to_collection', 'production_countries', 'production_companies', 'spoken_languages', 'status','video', 'original_language', 'tagline' ]
    data.drop( to_drop, inplace=True, axis=1 )
    data.dropna( subset=[ 'overview', 'title'] )
    data.to_csv('movies.csv', index=False)
    print( data.head )



if __name__ == '__main__':
    main()