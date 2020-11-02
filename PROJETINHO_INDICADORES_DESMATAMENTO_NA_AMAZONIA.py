#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
arquivo = pd.read_csv("C:/Users/davi-/OneDrive/Documentos/Arquivos/Users/Materiais_Assuntos/Ciência de dados/projeto ciência de dados/def_area_2004_20191.csv")
arquivo.rename(columns={'1':'ANO_ESTADO','1.1':'AC','1.2':'AM','1.3':'AP','1.4':'MA','1.5':'MT','1.6':'PA','1.7':'RO','1.8':'RR','1.9':'TO','1.10':'AMZ_LEGAL'},inplace=True)
conc = pd.DataFrame(arquivo)
#Função
def Medidas_Centralidade_Dispersao(coluna):
        print("Área de desmatamento (km²) por ano e estado, de 2004 a 2019, para a coluna :",coluna)
        print("Média : ", arquivo[coluna].mean())
        print("Mediana : ",arquivo[coluna].median())
        print("Desvio Padrão : ",arquivo[coluna].std())
        print("Variância : ",arquivo[coluna].var())
        print("Moda :\n",arquivo[coluna].mode())
        conc.boxplot(column=coluna)    


# In[22]:


arquivo.rename(columns={'1':'ANO_ESTADO','1.1':'AC','1.2':'AM','1.3':'AP','1.4':'MA','1.5':'MT','1.6':'PA','1.7':'RO','1.8':'RR','1.9':'TO','1.10':'AMZ_LEGAL'})


# In[23]:


Medidas_Centralidade_Dispersao("ANO_ESTADO")


# In[24]:


Medidas_Centralidade_Dispersao("AC")


# In[25]:


Medidas_Centralidade_Dispersao("AM")


# In[26]:


Medidas_Centralidade_Dispersao("AP")


# In[27]:


Medidas_Centralidade_Dispersao("MA")


# In[28]:


Medidas_Centralidade_Dispersao("MT")


# In[29]:


Medidas_Centralidade_Dispersao("PA")


# In[30]:


Medidas_Centralidade_Dispersao("RO")


# In[31]:


Medidas_Centralidade_Dispersao("RR")


# In[32]:


Medidas_Centralidade_Dispersao("TO")


# In[33]:


Medidas_Centralidade_Dispersao("AMZ")


# In[34]:


conc.boxplot()


# In[ ]:




