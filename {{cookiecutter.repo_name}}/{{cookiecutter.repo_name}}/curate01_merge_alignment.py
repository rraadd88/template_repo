from rohan.global_imports import *

def get01_dalignment(cfg,dalignmentp):
    from rohan.dandage.io_seqs import read_fasta
    d=read_fasta(cfg['uniprotalignmentp'])
    df1=pd.DataFrame({k:list(d[k]) for k in d})
    # uniprotid2features['sequence'][272:517]
    # uniprotid2features['sequence'][272]
    df1['position_uniprot']=list(range(273,517,1))

    poss=[]
    i=3
    for s in  df1['reference_DMS']:
        if s!='-':
            i+=1
            poss.append(i)
        else:
            poss.append('-')
    df1['position_DMS']=poss
    df1=df1.replace('-',np.nan).reset_index()
    to_table(df1,dalignmentp)
    
def map_intervals(x,df0):
    pos=range(x['start'],x['end']+1)
    df=pd.DataFrame({'position':pos,
    'feature name':np.repeat(x['feature name'],len(pos)),
    'feature type':np.repeat(x['feature type'],len(pos)),
        })
#     return df
    return df0.merge(df,left_on='position_uniprot',
              right_on='position',how='left').dropna()

def get02_dalignment_feats(dalignmentp,dseqfeaturesp,dalignment_featsp):
    # df003.apply(lambda x: map_intervals(x,df001),axis=1)
    df001=read_table(dalignmentp)
    df003=read_table(dseqfeaturesp)
    dfs=[]
    for rowi in range(len(df003)):
        dfs.append(map_intervals(df003.iloc[rowi,:],df001))

    df2=pd.concat(dfs,axis=0).pivot_table(columns='feature type',values='feature name',index='position_uniprot',aggfunc=sum)

    df2=df2.loc[:,(df2.apply(lambda x:len(unique_dropna(x)))>1).replace(False,np.nan).dropna().to_dict().keys()]
#     df2=df2.fillna('-')
    df2=df2.reset_index()        
    to_table(df2,dalignment_featsp)