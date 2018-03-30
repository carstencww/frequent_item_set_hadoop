#!/bin/bash

OUT_FILE=/user/ChanCarsten/hw1b
IN_FILE=/user/ChanCarsten/input/*
echo $PWD
hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=32 \
-D mapred.reduce.tasks=12 \
-file $PWD/part1c_map1.py -mapper part1c_map1.py \
-file $PWD/part1c_red1.py -reducer part1c_red1.py \
-input $IN_FILE \
-output $OUT_FILE

hadoop fs -getmerge $OUT_FILE ./supp.txt
hadoop dfs -rm -R $OUT_FILE

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=32 \
-D mapred.reduce.tasks=12 \
-file $PWD/supp.txt \
-file $PWD/part1c_map2.py -mapper part1c_map2.py \
-file $PWD/part1c_red2.py -reducer part1c_red2.py \
-input $IN_FILE \
-output $OUT_FILE

hadoop fs -getmerge $OUT_FILE ./final.txt
cat final.txt | sort -t$'\t' -k2nr | head -n100 > final_output.txt
