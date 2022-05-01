#!/usr/bin/env python
# coding: utf-8

# ***Violinplot of "Likely to recommend Instruction Partners"***
# 
# Violin plot is similar to a box and whisker plot or density map. It shows the distribution of quantitative data (Likely to recommend IP, 1-10) across categories (Submitter roles) such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a density estimation of the distribution.

# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import seaborn as sns


# ***Reading data***

# In[8]:


df=pd.read_csv('Partnership Data Lead _ Systems and Data Analyst - Content Exercise Data.csv')


# ***Establishing themes, size and color settings***

# In[12]:


sns.set_theme(style="whitegrid")
sns.set(rc={'figure.figsize':(20,8.27)})


# ***The violinplot, with each category scaled to have the same area***

# In[7]:


ax = sns.violinplot(x="Submitter Role", y="Likely to recommend Instruction Partners", data=df, cut=0, inner="quartile")


# In[ ]:




