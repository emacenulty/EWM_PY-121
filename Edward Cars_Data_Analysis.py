#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis Exercise
# * For this part we will be using the `data/cars.csv` dataset

# In[1]:


# Import the libraries you'll need here.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

get_ipython().run_line_magic('matplotlib', 'inline')
import scipy.stats as stats

df = pd.read_csv('cars.csv')
df.head()

get_ipython().system('pip3 install seaborn')


# In[2]:


get_ipython().system('pip3 install seaborn')


# # Load the csv file into a pandas dataframe.
# 

# In[3]:


# Load the csv file into a pandas dataframe.
fname ='cars.csv'
df = pd.read_csv(fname)
print(df)


# # Data clean up part 1.
# 
# 1. Print the number of duplicate rows we have in our dataframe.
# 
# 2. Modify our df to have all duplicate rows removed. 
# 
# 3. Do a sanity check to make sure all duplicates have been removed by printing the total number of duplicate rows again.

# In[4]:


# 1. Print the number of duplicate rows we have in our dataframe.
df.duplicated().sum


# In[9]:


#  2. Modify our df to have all duplicate rows removed. 
new_df = df.drop_duplicates(keep=False)


# In[12]:


# 3. Do a sanity check to make sure all duplicates have been removed by printing the total number of duplicate rows again.
new_df.duplicated().sum


# # Data clean up part 2.
# * Which column has the most null values and how many null values does it have?
# * Print how long our dataframe is.
# * Remove any row that has a null value in it. 
# * Do a sanity check and pring how long our dataframe is now that we have removed our null values.

# In[31]:


# * Which column has the most null values and how many null values does it have?
new_df.isnull().sum


# In[28]:


new_df[180:210]
#could not find any null


# In[9]:


# * Print how long (aka how many rows) our dataframe is.
new_df.shape


# In[66]:


# * Remove any row that has a null value in it. 

#i didnt find any
df_df=new_df.dropna(how ='any')


# In[67]:


# * Do a sanity check and pring how long our dataframe is now that we have removed our null values.
df_df.shape


# ### Make a bar chart that displays how many time each brand of car appears in this data. 
# _Brand of car is the `Make` of the car._

# In[41]:


Make_count = pd.value_counts(df_df['Make'])


# In[44]:


# Make a bar chart that displays how many times each brand of car appears in this data. 

Make_count = pd.value_counts(df_df['Make'])
import matplotlib.pyplot as plt
import math
#df_df.plot.bar()
get_ipython().run_line_magic('matplotlib', 'inline')
Make_count.plot.bar()
#xAxis = range(1)
#plt.bar(xAxis,new_df)
#plt.title('Frequency distribution')
#plt.xlabel('exam')
#plt.ylabel('score')
#plt.show()


# # Make the cart more legible, by making it a horizontal bar chart and changing the figure size.

# In[49]:


# Make the cart more legible, by making it a horizontal bar chart and changing the figure size.
Make_count = pd.value_counts(df_df['Make'])
import matplotlib.pyplot as plt
import math
plt.rcParams['figure.figsize']=(15,10)
#df_df.plot.bar()
Make_count.plot.barh()


# ### Make a timeline line chart in which the x-axis is the year, and the y-axis is the average MSRP.
# * What's noticeable about it and what do you think the error is...
# 

# In[84]:


#df_df['Year'] = pd.to_datetime(df.Year)
df.groupby(df_df.Year)['MSRP'].mean()


# In[85]:


# Make a timeline line chart in which the x-axis is the year, and the y-axis is the average MSRP.
#DF_year = df_df(index_col='Year')
#DF_year
plt.plot(df_df.groupby(df_df.Year)['MSRP'].mean())

plt.show()


# # It seems as though in the years before 2000, they were counting in tens.
# Make a new column that is called `adjusted_price`, that contains all prices, however, for 
# every year before 2000 make it 10x the original MSRP.

# In[75]:


# Make a new column that is called `adjusted_price`, that contains all prices, however, for every year before 2000 make it 10x the original MSRP.
#Adjusted_MSRP = df_df.MSRP*10 if df_df.Year< 2000 else = df_df.MSRP
df_df['Adjusted_MSRP'] =  np.where(df_df['Year'] <= 2000 (df_df.MSRP*10)


# # Replot the new adjusted price.  
# * Make the y-axis start at 0 and go up to 100,000

# In[33]:


# Replot the new adjusted price and make the y-axis start at 0 and go up to 100,000

plt.plot(df.groupby(df.Year)['Adjusted_MSRP'].mean())

plt.show()


# # What are the top 5 car makers make the most expensive cars on average. 
# * I only want the top 5, make sure your answer is the top 5 and only the top 5. 
# * Use our `adjusted_price` column for this

# In[94]:


# What are the top 5 car makers make the most expensive cars on average. 
expensive= df.groupby(df_df.Make)['MSRP'].mean()

#expensive.groupby("MSRP").head(5)


# # What are the top 5 car makers that have the highest median highway MPG?

# In[95]:


# Which car makers have the highest median highway MPG?
df.groupby(df.Make)['highway MPG'].median().head(5)


# # Using `sns.histplot`, make histogram of the adjusted_price of just these car makers.
# * ['Chevrolet', 'Ford', 'Toyota']

# In[36]:


# Using `sns.histplot`, make histogram of the adjusted_price of just these car makers.



# # Remake the same histogram, but limit the x-axis from 0 to 100,000

# In[37]:


# Remake the same histogram, but limit the x-axis from 0 to 100,000



# # Plot the relationship between Engine HP and highway MPG

# In[97]:


# Plot the relationship between Engine HP and highway MPG

plt.plot(df_df['Engine HP'],df_df['highway MPG'])
plt.show()


# # Remove any statisical outliers from Engine HP and highway MPG and plot the result.
# * Statisical outliers meaning values that are further than 3 standard deviations from the mean 
# * Create a new columns for z-scores for each 'Engine HP' and 'highway MPG' named 'Engine HP_zscore' and 'highway MPG_zscore'
# * Calculate the z-scores for each of our target columns.
# * Make sure you set the z-scores to be their absolute values. 
# * Create condition masks for when either of those absolute values are greater than 3.
# 
# * Create a new dataframe that is a copy of our dataframe using df.copy()
# 
# * Using our new dataframe
#     * Filter out all Engine HP Z-Scores that are greater than 3
#     * Filter out all Highway MPG z-scores that are greater than 3.
#     * Make the same scatterplot plotting the relationship of Engine HP and Highway MPG as before but with the this dataframe.

# In[23]:


# Remove any statisical outliers from Engine HP and highway MPG



# # What does this plot tell you about how Engine HP affects highway MPG?

# In[26]:


# What does this plot tell you about how Engine HP affects highway MPG?
print('YOUR ANSWER HERE')


# # Using a pairplot, display all of the linear relationship.
# * Which variables look like they have the strongest linear relationship (Besides MSRP and adjusted_price).

# In[27]:


# Using a pairplot, display all of the linear relationship.



# In[28]:


# * Which variables look like they have the strongest linear relationship (Besides MSRP and adjusted_price).
print('YOUR ANSWER HERE')


# # Find which features actually have the strongest linear relationship using correlations.
# * Make a heatmap plot of all of the correlations in our dataset.
# * Change the figure size of our heatmap plot to be 8x8
# * Which feature does Engine HP have the strongest relationship with, and why do you think that relationship exists.

# In[29]:


# * Make a heatmap plot of all of the correlations in our dataset.
# * Change the figure size of our heatmap plot to be 8x8


# # [EXTRA CREDIT] 
# * In the column names, replace all the spaces with an underscore, and make them all lowercase as well
# * Using subplots, display the histogram of adjusted_price for 'Ford' and 'Toyota' appear on charts side by side. 
#     * `f, axes = plt.subplots(1, 2, figsize=(13,5))`
# 
# 

# In[30]:


# * In the column names, replace all the spaces with an underscore, and make them all lowercase as well



# In[ ]:




