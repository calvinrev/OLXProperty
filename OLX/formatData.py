from datetime import datetime

def getValue(li, key):
    for i in li:
        if i['key']==key:
            try:
                return int(float(i['value']))
            except:
                return i['value']

def getFacilities(li):
    for i in li:
        if i['key']=='p_facility':
            res = []
            for val in i['values']:
                res.append(val['value'])
            return '-'.join(res)

def formatDate(dt):
    temp = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%f%z")
    return datetime.strftime(temp, "%Y-%m-%d %H:%M:%S")

def batchProcess(iterable, n=50):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]