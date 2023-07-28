#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


churn = pd.read_csv(r"C:\Users\Hp\ML Practise\Datasets\Churn_Modelling.csv")


# In[3]:


churn


# In[4]:


#we can see that the columns 'RowNumber', 'CustomerId' and 'Surname' are not important and thus can be dropped 

churn.drop(['RowNumber','CustomerId','Surname'],axis=1,inplace=True)
churn


# In[5]:


churn.dtypes


# In[6]:


for i in churn.columns:
    print(i,'\n',churn[i].unique(),'\n')


# In[7]:


#Label Encoding

from sklearn import preprocessing
le1 = preprocessing.LabelEncoder()           #label encoder variable for 'Geography'
churn.Geography = le1.fit_transform(churn.Geography)

le2 = preprocessing.LabelEncoder()           #label encoder variable for 'Gender'
churn.Gender = le2.fit_transform(churn.Gender)

#it is always a good practice to use separate encoder variables, as then the data stored can easily be inversed


# In[8]:


churn.Geography.unique()


# In[9]:


churn.Gender.unique()


# In[10]:


#ip/op creation

ip=churn.drop('Exited',axis=1)
op=churn.Exited


# In[11]:


ip.head()


# In[12]:


op.head()


# In[13]:


#Data Standardization

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

#standardizing the input data
ip = sc.fit_transform(ip)


# In[14]:


#PCA

from sklearn.decomposition import PCA
pc = PCA(n_components=2)
#'n_components' reduces the dimensions to 2
p_comp = pc.fit_transform(ip)


# In[15]:


p_comp.shape

#there are still 150 rows, but the 4 input columns are reduced to 2 only


# In[16]:


p_df = pd.DataFrame(data=p_comp,columns=['PC1','PC2'])
p_df


# In[17]:


df_final = pd.concat([p_df,op],axis=1)
df_final


# In[18]:


plt.figure(figsize=(15,10))
plt.scatter(df_final['PC1'],df_final['PC2'],c=op,cmap='plasma')
plt.show()


# In[21]:


plt.figure(figsize=(15,10))
sns.boxplot(y=df_final['PC1'],hue=op)
plt.show()


# In[22]:


plt.figure(figsize=(15,10))
sns.boxplot(y=df_final['PC2'],hue=op)
plt.show()


# In[ ]:




