
# coding: utf-8

# In[7]:

import graphlab


# In[15]:

trade_Buy_w_SF = graphlab.SFrame('MarketOrderDataFeb_May_onlyBuyFillsFinal.csv')


# In[17]:

trade_Buy_w_SF


# In[18]:

my_inputs = ['Days2Ex', 'Width', 'Bid Exchanges', 'Bid Size', 'Ask Exchanges', 'Ask Size',]


# In[20]:

trade_Buy_w_SF[my_inputs].show()


# In[21]:

train_data, test_data = trade_Buy_w_SF.random_split(.8, seed =0)


# In[24]:

regression_model = graphlab.linear_regression.create(train_data, target = 'Fill Dist From Ask', features = my_inputs)


# In[28]:

regression_model.evaluate(test_data)


# In[29]:

regression_model.summary()


# In[27]:

print regression_model["coefficients"]


# In[ ]:




# In[ ]:




# In[ ]:



