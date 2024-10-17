import pandas as pd

def dataClean(data):
    date = data['time'].str.split(' ').str.get(0)
    data['time'] = data['time'].str.split(' ').str.get(1).astype(int)
    data['temp'] = data['temp'].astype(int)
    data['flux'] = data['flux'].astype(int)
    data['speed'] = data['speed'].astype(int)
    data['direction'] = data['direction'].astype(int)

    Date = pd.DataFrame(
    {
        'date': date
    })
     
    fullData = Date.join(data)
    
    full_data = fullData.loc[(data['time']>=615) & (data['time']<=1745)]
    return full_data