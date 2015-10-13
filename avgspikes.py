# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 01:00:18 2015

@author: mgordo
This script is to be run after script.py and preprocess.py.
It averages spike tests, so as to present only the behaviour against a sudden decrease
in bandwidth in -1.5 seconds before the spike, and 7 seconds after
"""

import time;
import numpy as np;
import sys
import collections
import matplotlib
from datetime import datetime
import os
import re
from os import listdir
from os.path import isfile, join


means=['10', '20', '40', '60', '80', '100', '120']
variances=['0', '10', '20', '40', '50']
losses=['0.0','2.5','5.0']
bandwidths=['1','40','100']
methods=['quic','tcp']
spikes=['0','1']
testnumber=['1','2','3','4','5']

def roundtime(time):
    
    decimals=time-int(time)    
    if(decimals>=0.5):
        return int(time)+0.5
    else:
        return int(time)+0.0


openpath=os.path.normpath('C:/Users/Miguel/Desktop/Scientific/processed/')
onlyfiles = [ os.path.normpath(openpath+'/'+f) for f in listdir(openpath) if isfile(join(openpath,f)) ]
flag=1
lista=collections.OrderedDict()
previous='start'
for fich in sorted(onlyfiles):
    
    parts=fich.split('_')
    method=parts[0].split('\\')
    if(method[-1]=='SUMtcp' or method[-1]=='SUMquic'):
        if(parts[-2]!='0'):
            temp=method[-1]+parts[1]+parts[2]+parts[3]+parts[4]
            if(previous=='start' or previous==temp):
                previous=method[-1]+parts[1]+parts[2]+parts[3]+parts[4]
                with open(fich,'r') as f:
                    time_of_anomaly=roundtime(float(parts[-2]))
                    min_limit=max(0,time_of_anomaly-1.5)
                    
                    max_limit=time_of_anomaly+7
                    count=0
                    lista[flag]=collections.OrderedDict()
                    for line in f:
                        parts2=line.split()
                        if(float(parts2[0])>=min_limit and float(parts2[0])<=max_limit):
                            lista[flag][count]=float(parts2[1])
                            count+=1
                        if(count>(3+14)):
                            break
                
                flag+=1
                
            if(flag>10):#average here
                flag=1
                previous='start'                
                route=os.path.normpath('C:/Users/Miguel/Desktop/Scientific/processed/AVG'+method[-1]+'_'+parts[1]+'_'+parts[2]+'_'+parts[3]+'_'+parts[4]+'_1.txt')
                f=open(route,'w')
                for key in xrange(0,18,1):
                    avg=0
                    for flaggie in xrange(1,11,1):
                        if(key not in lista[flaggie].keys()):
                            lista[flaggie][key]=0
                        avg+=lista[flaggie][key]
                    avg/=10
                    f.write(str(max(0,float(key/2.0)))+' '+str(avg)+'\n')
                f.close()
                lista=collections.OrderedDict()
        else:
            flag=1
            previous='start'
            lista=collections.OrderedDict()
            continue
            
        