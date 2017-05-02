
# coding: utf-8

# In[152]:

import numpy as np
import pandas as pd


# In[153]:

taxi = pd.read_csv("nyc_taxi.csv").rename(columns = str.lower).rename(columns={'tpep_pickup_datetime': 'pickup_date', 'tpep_dropoff_datetime' : 'dropoff_date' })

taxi = taxi.assign(pickup_date = lambda x: pd.to_datetime(x['pickup_date'], format = '%Y-%m-%d %H:%M:%S'),
           dropoff_date = lambda x: pd.to_datetime(x['dropoff_date'], format = '%Y-%m-%d %H:%M:%S'))

taxi = taxi.set_index(['pickup_date'])


# In[154]:

taxi.columns


# In[155]:

taxi.sample(10)


# In[156]:

taxi.dtypes


# In[157]:

taxi = taxi.assign(pickup_hour = taxi.index.hour)
taxi.sample(10)


# In[158]:

# number of days covered by this dataset?
# len(taxi.pickup_date.dt.day.unique()) # 31



# In[159]:

taxi.sort_index(inplace=True)

x = pd.DataFrame(taxi.groupby(['pickup_hour'])['pickup_hour'].count())
x = x.assign(avg = x.pickup_hour / 31)
x['hour'] = x.index
x


# In[160]:

from bokeh.io import output_notebook, show, output_file, curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool
from bokeh.layouts import gridplot
from bokeh.charts import Bar, output_file, show
from bokeh.palettes import Viridis



# In[161]:


source = ColumnDataSource(x)

output_notebook()
p1 = figure(x_axis_label = "hour", y_axis_label = "average number of rides per hour", title = "average number of Uber rides per hour in Jan 2015")
p1.line('hour', 'avg', source = source, line_width = 5, color = "#E84F22")
p1.circle('hour', 'avg', source = source, color = '#E84F22', size = 8, line_width = 0)

show(p1)


# In[162]:

x = pd.DataFrame(taxi.groupby(['pickup_hour'])['tip_amount'].mean())
x['hour'] = x.index
x



# In[163]:

source = ColumnDataSource(x)

output_notebook()
p1 = figure(x_axis_label = "hour", y_axis_label = "average tip amount", title = "average tip given per hour in Jan 2015")
p1.circle('hour', 'tip_amount', source = source, color = '#F2C500', size = 8, line_width = 0)
p1.line('hour', 'tip_amount', source = source, line_width = 5, line_color = '#F2C500')
show(p1)


# In[ ]:




# In[ ]:




# In[ ]:



