Doing TDD as a first step
=========================

I have some legacy code (written by me, what a cowboy), that is in need of a
mid-sized refactoring.  Currently I iterate over a list of strings or "matchers"
which I then test aginst the description of the transaction.  If it matches I assign the category associated with that `matcher` to the transaction on a first come first served basis.

I have no tests I think.  I was writing it in a hurry.  The best reasons are the worst excuses.

Anyway, I currently store the matchers like this::

    _matchers = [

    ['goldex',                                      'costa', 'soho', 'luxury'],
    ['storage king',                                'storage', 'utilities', 'utilities'],

    ...

and I have about 200.  Its a mess.

I would rather convert them into the following ini-style format which will be
easier to maintain::

    [utilities]
    british gas
    southern water

    ...

I will lose a lot of fine grained-ness, but I am happy to do that, as this 
is about getting control.  And I suspect a "tagging" approach is going to be much more useful in the future.  (ie I intend to allow me to freeform tag any transactions, and only a few need be done that way such as "greece holiday", whereas frankly I cannot see a lot of value in tagging shopping in sansburys any different to Tesco.)


So I now need to define how my code will have to change to accomodate the new form.

`matchers.py` will probably best convert to a reader of an ini file, and supply
the _matchers array as usual.

`importer.py` will need to 

  1. remove everything but category high, and rename to just category
  2. handle the new format of matcher which will be a simple dict with lists
  3. this touches an awful lot...

So I shall first walk through the different processes, split them out,
possibly into new modules, and generally have a clean up.

Testing?
--------

I shall need a functional level test first, before descending into unit tests.
I shall use a small test corpus, with a small test matching corpus, and have the process run over them.

To this end I shall split this into a repo with the code and a repo with the data, because its the data I want to keep private.

 
