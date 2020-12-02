wget https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_file_list.txt

grep ". 2020" oa_file_list.txt > 2020_papers.txt

touch months.txt

for month in $(cat months.txt)
do grep $month 2020_papers.txt | wc -l >> 2020_month_counts.txt
done

paste months.txt 2020_month_counts.txt > tmp_counts.txt
mv tmp_counts.txt 2020_month_counts.txt


