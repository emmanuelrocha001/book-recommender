var file_path = '../data/movies.csv'

class Term {
    constructor( term ) {
        this._term = term;
        this._frequency = 0;
        this._documents = [];

    }

    get get_term() {
        return this._term;
    }

    get get_frequency() {
        return this._frequency;
    }

    incrementTermFrequency() {
        this._frequency = this._frequency + 1;
    }

    addDocument( doc_index ) {
        this._documents.push( doc_index );
    }

    get get_documments() {
        return this._documents;
    }





}
// tokenize data
d3.csv( file_path ).then( data => {
    var count=0;

    var overviews = [];
    data.forEach( item => {
        // count = count+1;
        // console.log(count);
        // console.log( item['title']);
        overviews.push( String( item['overview'] ) );
    });

    // tokenize first row
    var terms = [];
    // keep track of unique terms
    var unique_terms = [];

    overviews.forEach( overview => {
        overview.split(' ').forEach( word => {
            // cleaning token
            // removing ,
            word = word.replace(/\,/g,'');
            // removing .
            word = word.replace(/\./g,'');
            // removing 's
            word = word.replace(/\'s/g,'');

            // check if term is new
            if ( unique_terms.indexOf( word ) == -1 ) {
                // add new term
                unique_terms.push( word );
                new_term = new Term( word );
                new_term.incrementTermFrequency();
                // new_term.addDocument( 0 );
                terms.push( new_term );
            } else {
                terms.forEach( term => {
                    if( term.get_term == word )
                    {
                        term.incrementTermFrequency();
                        // new_term.addDocument( 0 );
                    }
                });
            }
            // console.log( word );
        });

    });
    console.log( terms );


    // console.log( overviews );
}).catch( error => {
    console.log( error );
});

