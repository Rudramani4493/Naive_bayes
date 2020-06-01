#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import metrics
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


param=pd.read_csv('CMC.csv')


# In[4]:


X= param.iloc[:,0:-1]
y= param.iloc[:,-1]


# In[5]:


#viewing top 5 lines of data
param.head()


# In[6]:


param.columns= ['Age','wife_education','husband_education','children','religion','working','husband_job','living_std','media_exp','contraceptive']


# In[7]:


param.info()


# In[8]:


#correlation table
param.corr()


# In[10]:


from sklearn.preprocessing import MinMaxScaler
model=MinMaxScaler()
X = model.fit_transform(X)


# In[12]:


#naive Bayes classifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.25)


# In[13]:


md=GaussianNB()
md.fit(X_train,y_train)


# In[15]:


expected = y_test
predicted = md.predict(X_test)


# In[16]:


#Classification report and confusion matrix
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


# In[21]:


#sample cross validation for k=12
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics


# In[23]:


scores = cross_val_score(md, X, y, cv=12)
print ("Cross-validated scores:", scores)


# In[25]:


#Making a dictionary with k values as keys and mean of cross validation score as values
s={}
for i in range(2,31):
    scores = cross_val_score(md, X, y, cv=i+1)
    s[i]=scores.mean()
    i=i+1


# In[26]:


#plot
fig, ax = plt.subplots()
lists = sorted(s.items())
x, y = zip(*lists) 
ax.plot(x, y)
ax.set_xlabel('K value')
ax.set_ylabel('Cross validation score')
ax.set_title('Mean Cross validation score Vs K value')
plt.show()


# In[ ]:




