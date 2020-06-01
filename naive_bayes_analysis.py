#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


param = pd.read_csv('CMC.csv')


# In[7]:


param.head(20)


# In[8]:


param.describe()


# In[9]:


param.info()


# In[10]:


param.dtypes


# In[11]:


from pandas import DataFrame


# In[12]:


param.columns= ['Age','wife_education','husband_education','children','religion','working','husband_job','living_std','media_exp','contraceptive']


# In[13]:


param.info()


# In[14]:


print('\n Effect of wife education on contraceptive adopted')
wife_education_effect=pd.crosstab(index=param['wife_education'],columns=param['contraceptive'],margins = True, margins_name="Total")
wife_education_effect.columns = ["no use","short term","long term","row total"]
wife_education_effect.index = ["low","high1","high2","high3","coltotal"]
print(wife_education_effect)
print('\n The crosstab is as:')
print('wife_education_effect')
print('\nPrior probabilities\n')
print(wife_education_effect/wife_education_effect.loc["coltotal"])
print('Table in the from of heatmap')
edu_wife_effect1 = pd.crosstab(index = param['wife_education'], columns = param['contraceptive'])
print(sns.heatmap(edu_wife_effect1,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# from the crosstab it is clear that educated wife has no relation with the contraceptive method adoopted.

# 

# In[15]:


print('\n Effect of Husband job on contraceptive adopted')
husband_job_effect = pd.crosstab(index=param['husband_job'],columns=param['contraceptive'],margins= True, margins_name= "Total")
husband_job_effect.columns = ["no use","short term","long term","row total"]
husband_job_effect.index = ["1","2","3","4","coltotal"]
print(husband_job_effect)
print('\n Prior probabilities\n')
print(husband_job_effect/husband_job_effect.loc["coltotal"])
print('Table in the from of heatmap')
husband_job_effect1 = pd.crosstab(index = param['husband_job'], columns = param['contraceptive'])
print(sns.heatmap(edu_wife_effect1,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# No pattern hence no clear observation 

# In[16]:


print('\n  Effect of media exposure on contraceptive method adopted\n')
Media_effect_conc= pd.crosstab(index=param["media_exp"],columns=param["contraceptive"],margins= True, margins_name= "Total")
Media_effect_conc.columns = ["no use","short term","long term","row total"]
Media_effect_conc.index = ["low","high","coltotal"]
print('\n The table:\n')
print(Media_effect_conc)
print('\n Prior probabilities:\n')
print(Media_effect_conc/Media_effect_conc.loc["coltotal"])
media1= pd.crosstab(index=param["media_exp"],columns=param["contraceptive"])
print(sns.heatmap(media1,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# No conclusions

# In[17]:


print('\n Effect of wife working status on contraceptive method adopted\n')
wife_working_stata=pd.crosstab(index=param["working"],columns=param["contraceptive"],margins=True,margins_name="Total")
wife_working_stata.columns = ["no use","short term","long term","row total"]
wife_working_stata.index = ["yes","no","coltotal"]
print('\n The table:\n')
print(wife_working_stata)
print('\n Prior probabilities:\n')
print(wife_working_stata/wife_working_stata.loc["coltotal"])
working1= pd.crosstab(index=param["working"],columns=param["contraceptive"])
print(sns.heatmap(working1,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# More Number of non working womens are there.But no conclusions

# In[18]:


param.info()


# In[20]:


print('\n Effect of living standard on contraceptive method adopted\n')
livingS=pd.crosstab(index=param["living_std"],columns=param["contraceptive"],margins=True,margins_name="Total")
livingS.columns = ["no use","short term","long term","row total"]
livingS.index = ["1","2","3","4","coltotal"]
print('\n The table:\n')
print(livingS)
print('\n Prior probabilities:\n')
print(livingS/livingS.loc["coltotal"])
liv= pd.crosstab(index=param["living_std"],columns=param["contraceptive"])
print(sns.heatmap(liv,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# In[21]:


print('\n Effect on husband job status on contraceptive adopoted\n')
Hus_job=pd.crosstab(index=param["husband_education"],columns=param["contraceptive"],margins=True,margins_name="Total")
Hus_job.columns = ["no use","short term","long term","row total"]
Hus_job.index = ["1","2","3","4","coltotal"]
print('\n The table:\n')
print(Hus_job)
print('\n Prior probabilities:\n')
print(Hus_job/Hus_job.loc["coltotal"])
liv= pd.crosstab(index=param["husband_education"],columns=param["contraceptive"])
print(sns.heatmap(liv,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# No conclusion

# In[23]:


print('\n Effect religion on contraceptive adopoted\n')
Rel=pd.crosstab(index=param["religion"],columns=param["contraceptive"],margins=True,margins_name="Total")
Rel.columns = ["no use","short term","long term","row total"]
Rel.index = ["0","1","coltotal"]
print('\n The table:\n')
print(Rel)
print('\n Prior probabilities:\n')
print(Rel/Rel.loc["coltotal"])
Reee= pd.crosstab(index=param["religion"],columns=param["contraceptive"])
print(sns.heatmap(Reee,cmap = 'YlGnBu', linewidths=.5, annot=True, fmt='d'))


# Islam tend to have more childs as observed not using any contraceptive are more among them.

# In[ ]:




