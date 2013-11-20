#rm money.db
#python importer.py init -

files=`ls -1 home_bank_stmts/staging/`
for file in $files
do

echo $file
python importer.py load home_bank_stmts/staging/$file
mv home_bank_stmts/staging/$file home_bank_stmts/latestload/


done

#python importer.py match -
#python importer.py summary -
