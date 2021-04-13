
#https://linuxhint.com/bash_arithmetic_operations/
pred_file=pred_test_b_min_max_xsum_cktXX_trainv2Eng_ckt30.txt
ref_file=test.target

# train data v2
nums=(1275 1158 1167 1261 1067 1247)
#train data v3, total 6630 lines
nums=(100 1133 1105 1092 1108 937 1155)


mkdir tmp
postfix=pred
postfix2=ref

cp $pred_file tmp/PRED
cp $ref_file tmp/REF
cd tmp


let s=0
for n in ${nums[@]} 
do 
let s=$(expr $s+$n)
echo $s
head -$s PRED |tail -$n > ${postfix}_$s
done
tail -n +100 PRED > PRED2


let s=0
for n in ${nums[@]} 
do 
let s=$(expr $s+$n)
echo $s
head -$s REF |tail -$n > ${postfix2}_$s
done
tail -n +100 REF > REF2

let s=0
for n in ${nums[@]} 
do 
let s=$(expr $s+$n)
echo $s
files2rouge ${postfix}_$s ${postfix2}_$s >> score.txt
echo -------sample $n------- >> score.txt
echo >> score.txt
echo >> score.txt
done
rm -r ${postfix}_* ${postfix2}_*

files2rouge REF2 PRED2 >> score.txt
echo >> score.txt
