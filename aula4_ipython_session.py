# coding: utf-8
a = pd.Series(np.random.normal(0,1,5),               index=['a','b','c','d','e'], name='my series')
import pandas as pd
a = pd.Series(np.random.normal(0,1,5),               index=['a','b','c','d','e'], name='my series')
a
get_ipython().magic(u'pinfo a.plot')
plot = a.plot(kind='bar)
plot = a.plot(kind='bar')
plot = a.plot()
get_ipython().magic(u'pinfo a.fillna')
import datetime as dt
d1 = dt.datetime(2015, 6, 30)
d1
d1.hour
d1.day
d1.year
d1.tzinfo
d1.strftime('%Y-%m-%d')
d1.strftime('%Y-%m-%d %H:%M:%S')
dt.datetime.strptime('2015-06-30 00:00:00', '%Y-%m-%d %H:%M:%S')
delta = dt.timedelta(seconds = 86400)
delta
d1
d1 + delta
d1.isoformat
d1.isoformat()
d1.isocalendar()
d1.toordinal()
dt.now()
dt.datetime.now()
dt.datetime.today()
a.index = pd.date_range(start='2014-1-1', periods=len(a)) # default 'period' is daily
a
a.plot()
b = a.resample('5min',fill_method='ffill')
b
b.head()
b.plot()
b = a.resample('5min')
b.plot()
b
df = pd.DataFrame({'A' : np.random.random(5),                   'B' : np.random.random(5),                   'C': np.random.random(5)}, index=np.arange(1,6))
df
df.plot()
df.query('A > B')
df['D'] = np.random.random(5)
df
df['D'] = np.random.random(6)
df['E'] = 5
df
df['F'] = pd.Series(np.random.random(4), index=np.arange(1,5))
df
df.apply(np.sqrt)
df.describe()
df['G'] = df['A'] + df['B']
df['H'] = np.sqrt(df['A'])
df
df.describe()
df.describe().T
df.plot()
df.drop('E', axis=1).plot(figsize=(8,12),                           subplots=True,                           sharex=True,                           kind='bar', rot=0); 
df.drop(['E', 'A'], axis=1).plot(figsize=(8,12),                           subplots=True,                           sharex=True,                           kind='bar', rot=0);
df.drop(['E', 'A'], axis=1).plot(figsize=(8,12),                           subplots=True,                           sharex=True,                           , rot=0);
df.drop(['E', 'A'], axis=1).plot(figsize=(8,12),                           subplots=True,                           sharex=True, rot=0);
df.to_csv()
df.to_csv('arquivo.csv')
df.to_csv('arquivo.csv', '\t')
df.to_pickle('arquivo.pkl')
c = pd.read_pickle('arquivo.pkl')
c
get_ipython().magic(u'run read_currents.py')
df
df.head()
df.index
df.index[0]
df['2013-04-18']
df.index['2013-04-18']
df.loc('2013-04-18')
a = df.loc('2013-04-18')
a
a.name
a.axis
df['2013-04-18':'2013-04-19']
df.plot()
df.drop(['vobs', 'vroms'], axis=1).plot(figsize=(8,12))
df.drop(['vobs', 'vroms'], axis=1).plot(figsize=(8,12), subplots=True)
df2 = df.resample('24H', how='mean')
df2 = df.resample('24H', method='mean')
df2 = df.resample('24h', how='mean')
df2 = df.resample('1d', how='mean')
df2 = df.resample('1D', how='mean')
df2 = df.resample(24, how='mean')
df2 = df.resample(periods=24, how='mean')
get_ipython().set_next_input(u'df2 = df.resample');get_ipython().magic(u'pinfo df.resample')
df2 = df.resample('1day', how='mean')
df2 = df.resample('day', how='mean')
df2 = df.resample('1day', how='mean')
df2 = df.resample('24H', how='mean')
type(df.index)
df.index = pd.to_datetime(df.index)
df
df.head()
type(df.index)
df.index[0]
df2 = df.resample('24H', how='mean')
df2.head()
df.drop(['vobs', 'vroms'], axis=1).plot(figsize=(8,12), subplots=True)
df2.drop(['vobs', 'vroms'], axis=1).plot(figsize=(8,12), subplots=True)
df['uromsday'] = df2['uroms']
df.head()
df.head(40)
df3 = df.dropna()
df3
df3.uroms.plot()
df3.uromsdat.plot()
df3.uromsday.plot()
df3.uromsday.plot()
df.uroms.plot()
df3.uromsday.plot(linewidth=3)
get_ipython().set_next_input(u"df['ufilt'] = pd.rolling_window");get_ipython().magic(u'pinfo pd.rolling_window')
df['ufilt'] = pd.rolling_window(window_type='hanning', window_size=24)
df['ufilt'] = pd.rolling_window(df['uroms'], window_type='hanning', window_size=24)
df['ufilt'] = pd.rolling_window(df['uroms'], window_type='hanning', window=24)
df['ufilt'] = pd.rolling_window(df['uroms'], window_type='hamming', window=24)
get_ipython().set_next_input(u"df['ufilt'] = pd.rolling_window");get_ipython().magic(u'pinfo pd.rolling_window')
df['ufilt'] = pd.rolling_window(df['uroms'], win_type='hamming', window=24)
df3.ufilt.plot(linewidth=3)
df.ufilt.plot(linewidth=3)
df['ufilt40'] = pd.rolling_window(df['uroms'], win_type='hamming', window=40)
df.ufilt40.plot(linewidth=3)
plt.legend()
df.to_csv('roms_vs_obs_filters.csv', sep='\t')
df.describe()
df.describe().T
filename = '/home/phellipe/Desktop/uerj-pythoncourse-20150629/sandbox/eduardorichard/A_SED.txt'
df = pd.read_csv(sep='\t')
df = pd.read_csv(filename, sep='\t')
df
df.head()
type(df.NO3)
df.NO3.dtype
df.NO3[0].dtype
type(df.NO3[0])
df = pd.read_csv(filename, sep='\t')
df
type(df.NO3[0])
df.head()
df.NO3.plot()
df.NO3.plot()
df.head()
df = pd.read_csv(filename, sep='\t', index_col=0)
df.head()
df = pd.read_csv(filename, sep='\t', index_col=[0, 2])
df
df.head()
df
df
df.keys()
list(df.keys())
df = pd.read_csv(filename, sep='\t', index_col=0)
d
df
campanhas = df.groupby('Campanha')
campanhas
campanhas
campanhas.head()
for month, group in groups:
        print month
        print group.head()
    
for campanha, group in campanhas:
        print campanha
        print group.head()
    
for campanha, group in campanhas:
        print campanha
        print "Nitrito mean concentration for a campanha %s = %s" %(campanha, group.NO2.mean())
    
for campanha, group in campanhas:
        print "Nitrito mean concentration for a campanha %s = %s" %(campanha, group.NO2.mean())
    
for campanha, group in campanhas:
        print "Bario mean concentration for a campanha %s = %s" %(campanha, group.Ba.mean())
    
radiais = df.groupby('Radial')
df = pd.read_csv(filename, sep='\t')
radiais = df.groupby('Radial')
for radial, group in radiais:
        print "Bario mean concentration for transect %s = %s" %(radial, group.Ba.mean())
    
get_ipython().magic(u'history')
get_ipython().magic(u'save aula4_ipython_session.py')
get_ipython().magic(u'save aula4_ipython_session')
get_ipython().magic(u'save aula4_ipython_session 1-178')


# coding: utf-8
import xray
ds = xray.open_dataset('/media/phellipe/9359-46F2/sebrazil20150605_00z_surf.nc')
ds = xray.open_dataset('/home/phellipe/Desktop/sebrazil20150605_00z_surf.nc')
ds
ds.lon
ds.lon.shape
ds.lat.shape
plt.pcolormesh(ds.lon, ds.lat, ds.sst[0,...])
ds.lon.shape
ds.lat.shape
ds.sst.shape
lon, lat = np.meshgrid(ds.lon.values, ds.lat.value)
lon, lat = np.meshgrid(ds.lon.values, ds.lat.values)
type(ds.lon)
type(ds.lon.values)
plt.pcolormesh(lon, lat, ds.sst[0,...].values)
plt.contourf(lon, lat, ds.sst[0,...].values, 40)
plt.contourf(lon, lat, ds.sst[-1,...].values, 40)
plt.contourf(lon, lat, ds.dep.values, 40)
ds
ssh = ds['ssh']
ssh
ds2 = ds.sel(lon=-48.68, lat=-28.3)
ds2 = ds.ssh.sel(lon=-48.68, lat=-28.3)
ds2 = ds.ssh.sel(lon=-48.68, lat=-25.3)
ds2 = ds.ssh.sel(lon=-48.68)
ds.sel(time=('2015-06-05'))
ds2 = ds.ssh.sel(lon='-48.68')
ds
ts = ds.ssh[:, 200, 300]
ts
df = ts.to_dataframe()
df
df = ts.to_pandas()
df
df.plot()
sstm = ds.sst.mean(axis=0)
sstm
plt.contourf(lon, lat, sstm, 40)
get_ipython().magic(u'save aula4_ipython_session_part2 1-40')
