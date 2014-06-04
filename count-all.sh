export CORPUS=`echo no-tag/Trainset-Segmentation-1/*.seg no-tag/Trainset-Segmentation-2/*.seg`
echo "Corpus paths: $CORPUS"

echo -n "Counting words..."
./words.py $CORPUS | sort | uniq -c | sort -r -n > words.cnt
echo " Done."

echo -n "Counting prefixes..."
./prefixes.py $CORPUS | sort | uniq -c | sort -r -n > prefixes.cnt
echo " Done."

echo -n "Counting suffixes..."
./suffixes.py $CORPUS | sort | uniq -c | sort -r -n > suffixes.cnt
echo " Done."

echo -n "Binding prefixes..."
./bind-prefixes.py --count-file prefixes.cnt $CORPUS > prefixes.bind
echo " Done."

echo -n "Binding suffixes..."
./bind-suffixes.py --count-file suffixes.cnt $CORPUS > suffixes.bind
echo " Done."

