from importer import *
import sys

if __name__ == '__main__':
    

    ### test whats in db per word
    action = sys.argv[1]
    f = sys.argv[2]

    if action == 'test':

        ### test for words 
        words = sys.argv[2:]
        for w in words:
            print test(w)
        ###
    elif action == 'doctest':
        ### initialise from csv
        import doctest
        doctest.testmod()

    elif action == 'init':
        ### initialise from csv
        initdb()

    elif action == 'load':
        load(f)

    elif action == 'match':

        #### catgorise from matchers
        categorise(matchers._matchers)

    elif action == 'summary':
        summaryview()
        help_summary()
        create_chart()

    elif action == 'normalise':
        print_categories()


    else:
        print "init, test, match"



