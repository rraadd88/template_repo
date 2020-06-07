from rohan.global_imports import *
from rohan.dandage.io_dict import to_dict,read_dict

def get01_uniprotid2features(cfg,uniprotid2featuresp):
    import requests, sys
    requestURL = "https://www.ebi.ac.uk/proteins/api/features/P12931?types=ACT_SITE,DOMAIN,HELIX,TURN,STRAND,REGION,MOTIF,VARIANT"
    r = requests.get(requestURL, headers={ "Accept" : "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    responseBody = r.text
    import ast
    uniprotid2features=ast.literal_eval(responseBody)
    to_dict(uniprotid2features,uniprotid2featuresp)

    
def get01_dseqfeatures(cfg,dseqfeaturesp):
    import requests, sys
    #INIT_MET, SIGNAL, PROPEP, TRANSIT, CHAIN, PEPTIDE, TOPO_DOM, TRANSMEM, DOMAIN, REPEAT, CA_BIND, ZN_FING, 
    #DNA_BIND, NP_BIND, REGION, COILED, MOTIF, COMPBIAS, ACT_SITE, METAL, BINDING, SITE, NON_STD, MOD_RES, LIPID, 
    #CARBOHYD, DISULFID, CROSSLNK, VAR_SEQ, VARIANT, MUTAGEN, UNSURE, CONFLICT, NON_CONS, NON_TER, HELIX, TURN, 
    #STRAND, INTRAMEM.
    requestURL = "https://www.ebi.ac.uk/proteins/api/features/P12931?types=ACT_SITE,DOMAIN,HELIX,TURN,STRAND,REGION,MOTIF,VARIANT"
    r = requests.get(requestURL, headers={ "Accept" : "text/x-gff"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    responseBody = r.text
    from io import StringIO
    df1=delunnamedcol(pd.read_table(StringIO(responseBody),comment='#',
                  names=[
                         'end','Unnamed1','Unnamed2','Unnamed3','feature description']))
    df1.index.names=['uniprot id','db','feature type','start']
    df1=df1.reset_index()
    def get_feature_name(s):
        from rohan.dandage.io_dict import str2dict
        d=str2dict(s['feature description'])
        return d['Note'] if 'Note' in d else d['ID'] if 'ID' in d else s['feature type']
    df1['feature name']=df1.apply(lambda x: get_feature_name(x),axis=1)
    df1.loc[df1['feature type'].isin(['HELIX','STRAND','TURN']),'feature type']='secondary structure'
    to_table(df1,dseqfeaturesp)
    