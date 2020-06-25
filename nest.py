#!/usr/bin/env python3
import csv
import json
import pprint
import glob

'''
Reads in nest CSVs (finds them recursively), averages the samples and writes out a CSV 
 that can be imported into excel/graphed/etc.
'''

def load_json(filename):
    '''
    load the given json file and return a dictionary
    '''
    
    with open(filename) as f:
        data = json.load(f)

    return data

def load_csv(filename, data):
     '''
    load the given csv file and return a dictionary
    '''   
     with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row)
            Date=row['Date']
            Time=row['Time']
            data[Date + '_' + Time]={}
            if row['avg(temp)'] != "":
                data[Date + '_' + Time]['avg_humidity'] = float(row['avg(humidity)'])
            else:
                data[Date + '_' + Time]['avg_humidity'] = 0
            # convert celsius to fahrenheit
            if row['avg(temp)'] != "":
                data[Date + '_' + Time]['avg_temp'] = round((float(row['avg(temp)']) * 9/5)+32,2)
            else:
                data[Date + '_' + Time]['avg_temp'] = 0

def smooth_missing_data(data):
    '''
    avg day before and day after to smooth out missing data
    '''
    prev={}
    prev_minus_1 = {}
    fix_h=False
    fix_t=False
    for timestamp in data.keys():
        # fix prev if needed and reset fix flags
        if fix_h:
            if prev and prev_minus_1:
                #print ("smoothing: " + prev + " " + str(data[prev_minus_1]['avg_humidity']) + " " + str(data[timestamp]['avg_humidity']))
                data[prev]['avg_humidity'] = round((data[prev_minus_1]['avg_humidity'] + data[timestamp]['avg_humidity'])/2,2)
                fix_h = False
            else:
                print("Warning: prev empty, unable to smooth humidity")
                fix_h = False
        if fix_t:
            if prev and prev_minus_1:
                #print ("smoothing: " + prev + " " + str(data[prev_minus_1]['avg_temp']) + " " + str(data[timestamp]['avg_temp']))
                data[prev]['avg_temp'] = round((data[prev_minus_1]['avg_temp'] + data[timestamp]['avg_temp'])/2,2)
                fix_t = False
            else:
                print("Warning: prev empty, unable to smooth temp")
                fix_t = False
        # set fix flags
        if data[timestamp]['avg_humidity']==0:
            fix_h=True
        if data[timestamp]['avg_temp']==0:
            fix_t=True
        # update trailing pointers
        prev_minus_1 = prev
        prev=timestamp
        


def subtotal_by_day(data):
    '''
    returns a dictionary with one entry for each day (avg of all the 15 minute data points)
    '''
    ret = {}
    for timestamp in data.keys():
        date,time = timestamp.split('_')
        if date not in ret.keys():
            # starting a new date
            ret[date]={}
            ret[date]['avg_humidity']=0
            ret[date]['avg_temp']=0
            ret[date]['avg_humidity_cnt']=0
            ret[date]['avg_temp_cnt']=0
        #print(date + " " + time + " " + str(data[timestamp]))
        ret[date]['avg_humidity'] += data[timestamp]['avg_humidity']
        ret[date]['avg_temp'] += data[timestamp]['avg_temp']
        if  data[timestamp]['avg_humidity'] != 0:
            ret[date]['avg_humidity_cnt'] += 1
        if  data[timestamp]['avg_temp'] != 0:
            ret[date]['avg_temp_cnt'] += 1
    for date in ret.keys():
        ret[date]['avg_humidity'] = round(ret[date]['avg_humidity']/ ret[date]['avg_humidity_cnt'],2)
        ret[date]['avg_temp'] = round(ret[date]['avg_temp']/ ret[date]['avg_temp_cnt'],2)
    return ret

# JSON and CSV contain different 'stuff', CSV seems to have what I want: 15 minute avg temp and humidity data            
#d = ljson("/Users/micheleadkins/Documents/data/Nest/thermostats/corpus/2019/08/2019-08-summary.json")

# load the data
data={}
#FIXME: make the path a commandline option
for name in glob.glob('/Users/micheleadkins/Documents/data/Nest/thermostats/corpus/**/**/*.csv',recursive=True):
    load_csv(name, data)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)

# smooth out any missing values
smooth_missing_data(data)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)

# average by day
ret = subtotal_by_day(data)
print ("date, avg_humidity, avg_temp")
#FIXME: sort these keys
for date in ret.keys():
    if 'avg_humidity' in ret[date].keys() and 'avg_temp' in ret[date].keys():
        print(date + ", " + str(ret[date]['avg_humidity']) + ", " + str(ret[date]['avg_temp']))
    else:
        print("Warning: couldn't find avg temp and/or avg_humidity for " + date + " " + str(ret[date]))
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(ret)
