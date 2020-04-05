import os
import sys
import datetime
import pickle
import LoveUpdate
ordir=os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
tdy=LoveUpdate.getdate()
if not os.path.exists('updatestat.lup'):
    lupfile=open('updatestat.lup', 'wb')
    statusdict={'lastupdate':tdy, 'updateme':True}
    pickle.dump(statusdict, lupfile)
    lupfile.close()
lupfile=open('updatestat.lup', 'rb')
statusdict=pickle.load(lupfile)
lupfile.close()
if statusdict['updateme']:
    retval=LoveUpdate.update('LovelacePM', tdy)
    if type(retval)==tuple:
        code=retval[1]
        tdy=retval[0]
    elif type(retval)==bool:
        code=retval
    else:
        code=True
    if code:
        statusdict['lastupdate']=tdy
        lupfile=open('updatestat.lup', 'wb')
        pickle.dump(statusdict, lupfile)
        lupfile.close()
        print('LovelacePM has autoupdated. If you wish to deactivate the autoupdate feature, use LovelacePM.updatecancel()')
    else:
        print('WARNING: error in autoupdate. Check internet connection if you wish to update LovelacePM. Moving on')
else:
    print('WARNING: LovelacePM autoupdate is deactivated. if you wish to activate autoupdate, use LovelacePM.updateset()')
def updateset():
    pdir=os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    lupfile=open('updatestat.lup', 'rb')
    statusdict=pickle.load(lupfile)
    lupfile.close()
    statusdict['updateme']=True
    lupfile=open('updatestat.lup', 'wb')
    pickle.dump(statusdict, lupfile)
    lupfile.close()
    os.chdir(pdir)
def updatecancel():
    pdir=os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    lupfile=open('updatestat.lup', 'rb')
    statusdict=pickle.load(lupfile)
    lupfile.close()
    statusdict['updateme']=False
    lupfile=open('updatestat.lup', 'wb')
    pickle.dump(statusdict, lupfile)
    lupfile.close()
    os.chdir(pdir)
del retval, tdy, lupfile
from utils import *
from wing import *
from body import *
from control import *
from aircraft import *
from xfoil_visc import *
from aerodynamic_output import *
from toolkit import *
os.chdir(ordir)
del ordir
