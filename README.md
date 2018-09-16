# KEGG_Non-model-species
this is a pipeline of universal non-model species KEGG enrichment analysis.
firstly, the python rpy2.robjects is necessary. In addition, you need to install the R package clusterProfiler.
second ,you should prepare the  gene_list file and get the kaas result from http://www.genome.jp/tools/kaas/' , for example, 'lightcyan1.txt' and 'q000003-2.keg'
at last, run the 'deal_with2.py' and then you will get the result figure 'lightcyan1.txt.pdf'
