from rohan.global_imports import *

def get01_ddms(cfg,ddmsp):
    df00=pd.read_csv(cfg['ddms_rawp'],header=4)
    from rohan.dandage.io_strs import replacemany
    df1=df00.join(df00['hgvs_pro'].str.split('.').apply(pd.Series)[1].apply(lambda x: 
[x[:3],x[-3:],int(replacemany(x,[x[:3],x[-3:]]))] 
).apply(pd.Series).rename(columns={0:'reference',1:'mutated',2:'position'}))
    from rohan.dandage.io_seqs import aathreeletters2one
    for col in ['reference','mutated']:
        df1[col]=df1[col].apply(aathreeletters2one)
    df1=df1.sort_values(by=['position'])
    to_table(df1,ddmsp)

def get02_ddms_corr(ddmsp,ddms_corrp):
    df1=read_table(ddmsp)
    df2=df1.select_dtypes(float).dropna(how='all',axis=1).corr(method='spearman')
    to_table(df2,ddms_corrp)
