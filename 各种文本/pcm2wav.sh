#!/bin/sh
dir='/home/users/kokann/htkdata/vol3'
outdir='/home/users/kokann/htkdata/vol1_wav'
find $dir -name "*.raw" > list

for files in `cat list`;do
	echo $files
	wav_name=`echo $files | cut -d'.' -f1`;
	echo $wav_name.wav

	ffmpeg -f s16be -y -ar 16000 -ac 1 -i $files "$wav_name.wav"
done

rm -f list
