from scrapy import cmdline
# find . -name "*pyc"|xargs rm
# fuck 总是加载老的文件。
# https://github.com/scrapy/scrapy/issues/2181

# find . -name "*pyc"|xargs rm  ; scrapy crawl github_rank_top -o rank.csv

name = 'github_rank_top'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())