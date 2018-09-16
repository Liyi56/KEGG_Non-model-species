#!/usr/bin/env python
# -*- coding=utf-8 -*-
import re
import sys
import os
os.environ['R_USER']='administrator'
mydir=os.getcwd()
#kaas_result=sys.argv[1]
def kaas_deal_with(kaas_file_name='q000003-2.keg'):
    'deal_with the kaas result from http://www.genome.jp/tools/kaas/'
    #kaas_file_name=input("please tell me the kaas result_name:")
    kegg={}
    kegg_geneid={}
    kegg_1ist=[]
    f2=open(kaas_file_name)
    for line1 in f2:
        if 'D 'in line1 and ";" in line1:
            l1 = re.split("\s+",line1.rstrip("\n"))
            kegg_id=l1[2]
            gene_id=l1[1].replace('.1;','')
            kegg_name=line1.strip("\n").split(";")[2].lstrip()#kegg_name=str('\t'.join(re.split("\s+",line1.rstrip("\n"))[3:]))
            kegg_geneid[gene_id]=kegg_id
            if kegg_id not in kegg_1ist:
                kegg_1ist.append(kegg_id)
                kegg[kegg_id]=kegg_name
    f2.close()
    f3=open("KO_geneid.txt",'w')
    f3.write('KEGG_ID'+'\t'+'GeneIDs'+'\n')
    for i1 in kegg_geneid:
        f3.write( kegg_geneid[i1]+'\t'+i1+'\n')
    f3.close()
    f3=open("KO_kegg_name.txt",'w')
    f3.write('KEGG_ID'+'\t'+'name'+'\n')
    for i2 in kegg:
        f3.write(i2+'\t'+kegg[i2]+'\n')
    f3.close()
def use_rpy2():
    import rpy2.robjects as robjects
    r=robjects.r
    from rpy2.robjects.packages import importr
    importr('clusterProfiler')
    r.setwd(mydir)
    data=input("gene_list_file_name:")
    my_gene = r['read.table'](data,sep = '\t')
    my_gene = r['as.character'](r.unlist(my_gene))
    TERM2GENE1 = r['read.table']("KO_geneid.txt")
    TERM2NAME1 = r['read.table']("KO_kegg_name.txt",sep = '\t')
    x=r.enricher(my_gene, TERM2GENE=TERM2GENE1, TERM2NAME=TERM2NAME1)
    file_name = r.paste(data,".pdf", sep='')
    r.pdf(file= file_name)
    p = r.dotplot(x,showCategory=7,title="Enrichmentkegg_dot")
    r.plot(p)
    r['dev.off']() # 关闭设备
# if __name__ == '__main__':
#     demo=kaas_deal_with()
#     demo()
kaas_deal_with()
use_rpy2()
