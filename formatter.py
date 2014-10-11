'''
Created on 11 Oct 2014

@author: mariaz
'''
import pickle

extra_data = {'egy': {'country_label': 'egypt', 'code': 'egy', 'continent': '4', 'population': '78075705'}, 'bgd': {'country_label': 'bangladesh', 'code': 'bgd', 'continent': '1', 'population': '151125475'}, 'nga': {'country_label': 'nigeria', 'code': 'nga', 'continent': '4', 'population': '159707780'}, 'usa': {'country_label': 'unitedstates', 'code': 'usa', 'continent': '2', 'population': '309326225'}, 'deu': {'country_label': 'germany', 'code': 'deu', 'continent': '2', 'population': '81776930'}, 'idn': {'country_label': 'indonesia', 'code': 'idn', 'continent': '1', 'population': '240676485'}, 'gbr': {'country_label': 'unitedkingdom', 'code': 'gbr', 'continent': '2', 'population': '62747868'}, 'cod': {'country_label': 'congo,dem.rep.', 'code': 'cod', 'continent': '4', 'population': '62191161'}, 'eth': {'country_label': 'ethiopia', 'code': 'eth', 'continent': '4', 'population': '87095281'}, 'pak': {'country_label': 'pakistan', 'code': 'pak', 'continent': '1', 'population': '173149306'}, 'col': {'country_label': 'colombia', 'code': 'col', 'continent': '3', 'population': '46444798'}, 'vnm': {'country_label': 'vietnam', 'code': 'vnm', 'continent': '1', 'population': '86932500'}, 'prk': {'country_label': 'korea,rep.(south)', 'code': 'prk', 'continent': '1', 'population': '49410366'}, 'tza': {'country_label': 'tanzania', 'code': 'tza', 'continent': '4', 'population': '44973330'}, 'fra': {'country_label': 'france', 'code': 'fra', 'continent': '2', 'population': '65031235'}, 'esp': {'country_label': 'spain', 'code': 'esp', 'continent': '2', 'population': '46576897'}, 'chn': {'country_label': 'china', 'code': 'chn', 'continent': '1', 'population': '1337705000'}, 'ukr': {'country_label': 'ukraine', 'code': 'ukr', 'continent': '2', 'population': '45870700'}, 'mmr': {'country_label': 'myanmar', 'code': 'mmr', 'continent': '1', 'population': '51931231'}, 'irn': {'country_label': 'iran', 'code': 'irn', 'continent': '4', 'population': '74462314'}, 'tha': {'country_label': 'thailand', 'code': 'tha', 'continent': '1', 'population': '66402316'}, 'jpn': {'country_label': 'japan', 'code': 'jpn', 'continent': '1', 'population': '127450459'}, 'zaf': {'country_label': 'southafrica', 'code': 'zaf', 'continent': '4', 'population': '50895698'}, 'tur': {'country_label': 'turkey', 'code': 'tur', 'continent': '2', 'population': '72137546'}, 'phl': {'country_label': 'philippines', 'code': 'phl', 'continent': '1', 'population': '93444322'}, 'ita': {'country_label': 'italy', 'code': 'ita', 'continent': '2', 'population': '60483385'}, 'ind': {'country_label': 'india', 'code': 'ind', 'continent': '1', 'population': '1205624648'}, 'rus': {'country_label': 'russianfederation', 'code': 'rus', 'continent': '2', 'population': '142389000'}, 'mex': {'country_label': 'mexico', 'code': 'mex', 'continent': '3', 'population': '117886404'}, 'bra': {'country_label': 'brazil', 'code': 'bra', 'continent': '3', 'population': '195210154'}}

if __name__ == '__main__':

    pkl_file = open('world.pkl', 'rb')
    
    data_model = pickle.load(pkl_file)
    
    print data_model['jpn']['tasmax']['base_avg']
    
    clist = ['chn', 'ind', 'usa', 'idn', 'bra', 'pak', 'nga', 'bgd', 'jpn', 'mex', 'phl', 'eth', 'deu', 'egy', 'tur', 'tha', 'fra', 'gbr', 'ita', 'mmr', 'zaf', 'esp', 'col', 'ukr']
    variables = ['tasmin', 'tasmax', 'pr', 'r02']
    measurements = [("", "2046_2065", "future"), ("baseline_", "1961_1990", "past"), ("depart_", "2046_2065", "future_delta")]
    scenarios = ["a2"]
    years = [1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065]
#     years = [1970, 2050]
    
    for c in clist:
        for v in variables:
            data_model[c][v]['combined'] = dict(data_model[c][v]['past'] + data_model[c][v]['future'])

#     for y in years:
    
    for y in years:
        filename = "%d.csv" % (y)
        f = open(filename, "w")
        print >>f,  "continent, country_label, temperature, rainfall, population, code"
        for c in clist:
#             {'country_label': 'Egypt', 'code': 'EGY', 'continent': '4', 'population': '78075705'}
            print >> f, ",".join(map(str,[extra_data[c]["continent"],  extra_data[c]['country_label'], data_model[c]['tasmax']['combined'][y] - data_model[c]['tasmax']['base_avg'], data_model[c]['pr']['combined'][y] / data_model[c]['pr']['base_avg'], extra_data[c]['population'], c]))
#             print >> f, ",".join(map(str,[extra_data[c]["continent"],  extra_data[c]['country_label'], data_model[c]['tasmax']['combined'][y], data_model[c]['pr']['combined'][y], extra_data[c]['population'], c]))
        f.close()
        
    for y in years:
        temps = []
        pr = []
        for c in clist:
            temps +=  [data_model[c]['tasmax']['combined'][y] - data_model[c]['tasmax']['base_avg']]
            pr += [data_model[c]['pr']['combined'][y] / data_model[c]['pr']['base_avg']]
        print "[%s, %s], " % (temps, pr)
        
    print "********************"
    print countries
