#!/usr/bin/python

import urllib2
import json
import smtplib
SEP=" "
URL="http://finance.google.com/finance/info?client=ig&q=indexbom:sensex"

u = urllib2.urlopen(URL)
content = u.read()
#print content
obj = json.loads(content[4:])
#print obj
print obj[0]['l_fix'], obj[0]['c_fix'], obj[0]['cp_fix']
cp=float(obj[0]['cp_fix'])
if(cp < 0 ):
    m_str= "Sensex down : "+obj[0]['l_fix']+SEP+obj[0]['c_fix']+SEP+obj[0]['cp_fix']
    print m_str
    # TODO: Send mail if down by 1% 
