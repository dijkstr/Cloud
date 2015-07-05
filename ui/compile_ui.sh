#/usr/bin/bash


for file in `ls *.ui`
	do
	pyuic4 -o ui_${file%.ui}.py $file
	done
