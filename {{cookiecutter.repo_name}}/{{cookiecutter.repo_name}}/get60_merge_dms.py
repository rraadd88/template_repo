from rohan.global_imports import *
def get01_ddms_feats(dalignmentp,ddmsp,dalignment_featsp,ddms_featsp):
    df01=read_table(dalignmentp)
    df02=read_table(ddmsp)
    df03=read_table(dalignment_featsp)
    cols_ddms=['score','std','epsilon','activity_score','reference','mutated','position']
    df1=df01.merge(df02.loc[:,cols_ddms],left_on=['position_DMS','reference_DMS'],right_on=['position','reference'],
               how='left')
    df2=df1.merge(df03,on=['position_uniprot'],how='left')
    ## nan vaues in feats to 'not {feature type}'
    to_table(df2,ddms_featsp)