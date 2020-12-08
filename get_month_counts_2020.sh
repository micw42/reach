#Get oa file list from ncbi
wget https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_file_list.txt

#Get all papers from 2020 and write them to a file
grep ". 2020" oa_file_list.txt > 2020_papers.txt

#Count the number of papers from each month in 2020
for month in $(cat months.txt)
do grep $month 2020_papers.txt | wc -l >> 2020_month_counts.txt
done

#Merge the columns of months and the month counts together
paste months.txt 2020_month_counts.txt > tmp_counts.txt
mv tmp_counts.txt 2020_month_counts.txt


