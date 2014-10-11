'''
Created on 11 Oct 2014

@author: mariaz
'''


import requests
import StringIO
import csv
import numpy
import pickle
from iso3166 import countries


url_template = 'http://107.22.189.175/cckp-output/codess-{code}-m-a/{country_name}/{variable}/gfdl_cm2_1.1_{scenario}/'+\
    'table_yearly_{measurement}AR4_Global_Extr_50k_gfdl_cm2_1.1_{scenario}_{variable}_14_{period}.csv'
    
data_model = {}


def process_country(c, v, s, m):
    global url_template
    country = countries.get(c)
    url = url_template.format(code=c, country_name=country.name, variable=v, scenario=s, period=m[1], measurement=m[0])
    r = requests.get(url)
    print "[%d] %s %s %s %s" % (r.status_code, c, v, s, m)
    f = StringIO.StringIO(r.text)
    reader = csv.DictReader(f, delimiter=',')
    try:
        return [(int(row["yr"]),float(row["value"])) for row in reader]
    except:
        return [(0,0)]


def main():
#     clist = ['rus']
    clist = ['chn', 'ind', 'usa', 'idn', 'bra', 'pak', 'nga', 'bgd', 'rus', 'jpn', 'mex', 'phl', 'eth', 'vnm', 'deu', 'egy', 'irn', 'tur', 'tha', 'fra', 'gbr', 'cod', 'ita', 'mmr', 'zaf', 'prk', 'esp', 'col', 'ukr', 'tza']
#     variables = ['tasmax']    
    variables = ['tasmin', 'tasmax', 'pr', 'r02']
    measurements = [("", "2046_2065", "future"), ("baseline_", "1961_1990", "past"), ("depart_", "2046_2065", "future_delta")]
    scenarios = ["a2"]
#     scenarios = "a2 b1 a1b".split()

    global data_model
    for c in clist:
        data_model[c] = {}
        for v in variables:
            data_model[c][v] = {}
            for s in scenarios:
                for m in measurements:
                    data_model[c][v][m[2]] = process_country(c, v, s, m)
                    
    

    for c in clist:
        for v in variables:
            data_model[c][v]['base_avg'] = numpy.mean([t for (y,t) in data_model[c][v]['past']])
            print "%s %f" % (c, data_model[c][v]['base_avg'] )
        
    
   
    output = open('world.pkl', 'wb')
    
    # Pickle dictionary using protocol 0.
    pickle.dump(data_model, output)
    
    output.close()     
    
#     print data_model['chn']['tasmax']['past'] + data_model['chn']['tasmax']['future']

    
    #             print url
    #             r = requests.get("http://google.com")
    #     
    #             print "result-c %d" % (r.status_code)
    
#     print data_model



if __name__ == "__main__":
    main()



# import unittest
# 
# 
# class Test(unittest.TestCase):
# 
# 
#     def testName(self):
#         pass
# 
# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()