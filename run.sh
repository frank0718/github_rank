#!/bin/bash 
rm *.json ; 
find . -name "*pyc"|xargs rm  ; 

langs=("Python" "Golang" "Javascript" "HTML" "Shell" "C")
# langs=("Java")
for lang in ${langs[@]} ;  
do 
	scrapy crawl github_rank_top -a lang=${lang} -o ${lang}.json
	sleep 5 
done 