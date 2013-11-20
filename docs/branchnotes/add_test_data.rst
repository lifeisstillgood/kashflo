add_test_data
-------------

We should provide some test data for a functional style testing as
the first test wrapping.  This will give some degree of confidence
over the system, whilst leaving unittesting till later (I feel
you get a higher degree of confidence over the whole system without
going in and fixing the whole mess *right now*)

Test data needed

* a CSV file of right format holding 5 or so transactions

* a test data folder, a testdata output folder
  conf: testdatafolder -> includes output in it

* a test rig, that runs the importer, clears things up and tests to 
  see if we get the right output (!)

