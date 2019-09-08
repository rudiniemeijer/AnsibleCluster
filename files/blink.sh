#!/bin/sh

url=p24.local

curl -s "http://$url:4000/clear" > /dev/null
for j in 0 1 2 3 4 5 6 7
do
    num=$(($j))
    hue="0.$num"
    curl -s "http://$url:4000/set?x=$j&y=0&hue=$hue" > /dev/null
    num=$(($j + 1))
    hue="0.$num"
    curl -s "http://$url:4000/set?x=$j&y=1&hue=$hue" > /dev/null
    num=$(($j + 2))
    hue="0.$num"
    curl -s "http://$url:4000/set?x=$j&y=2&hue=$hue" > /dev/null
    num=$(($j + 3))
    hue="0.$num"
    curl -s "http://$url:4000/set?x=$j&y=3&hue=$hue" > /dev/null
done
echo "done"