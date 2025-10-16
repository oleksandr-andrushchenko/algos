# Given a text file file.txt, print just the 10th line of the file.
# Read from the file file.txt and output the tenth line to stdout.

sed -n '10p' file.txt
#awk 'NR==10' file.txt
#head -n 10 file.txt | tail -n 1