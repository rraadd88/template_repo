import argh
from os.path import basename,dirname
packagen=basename(dirname(__file__))

def workflow(cfgp,test=False,force=False,cores=4):
    """
    runs the analysis.   
    
    :param cfgp: path to configuration yaml file (ext:.yml)        
    """
    from rohan.dandage.io_fun import run_package
    cfg=run_package(cfgp,packagen=packagen,test=test,force=force,cores=cores)

## begin    
import sys
parser = argh.ArghParser()
parser.add_commands([workflow])

from rohan.dandage.io_strs import logging,get_logger,get_datetime
level=logging.ERROR
logp=get_logger(program=packagen,
           argv=[get_datetime()],
           level=level,
           dp=None)        
logging.info(f"start. log file: {logp}")
print(f"start. log file: {logp}")    
if __name__ == '__main__':
    logging.info('start')
    parser.dispatch()
    logging.info('finished')
    
