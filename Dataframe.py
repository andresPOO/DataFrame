#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pandas


# In[4]:


import pandas as pd
#Una serie es un arreglo unidimencional


# In[5]:


miSerie=pd.Series((34,56,78,23,34))
miSerie


# In[9]:


#Diccionario en python

miDiccionario ={
    "Nombre": "Casa_1",
    "Area":120,
    "Baños": 3,
    "Propietario": [
        "Diana", "Paulo", "Pedro"
    ],
    "Barrio": {
        "Nombre": "Santa Librada",
        "Localidad": "Nariño"
    }
}
miDiccionario


# In[ ]:


#Data fram


# In[13]:


miDataframe=pd.DataFrame({"si": [10,15], "No":[50,68]})
miDataframe


# In[ ]:




