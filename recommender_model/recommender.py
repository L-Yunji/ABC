#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Build recommendation model: Content based filtering

#Import refined restaurant public data
import pandas as pd

rest_df = pd.read_csv('rest_public_data.csv')

len(rest_df)
rest_df

#Add a column that is a combination of rating and density
rest_df = rest_df.drop(rest_df.columns[0], axis=1)
rest_df['recommend'] = (rest_df['rest_rating']*0.3 + rest_df['rest_density']*0.7)
rest_df

rest_df.to_csv('data_0211.csv')
rest_df.to_json('data_0211.json')


#Content based filtering

#Vectorize texts into numbers
from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer(ngram_range=(1, 3))
c_vector_genres = count_vector.fit_transform(rest_df['rest_category'])
c_vector_genres.shape
c_vector_genres


#Get cosine_similarity with the vectors
from sklearn.metrics.pairwise import cosine_similarity

gerne_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1]
gerne_c_sim.shape
gerne_c_sim.shape


#Make recommendation by population density
def get_recommend_rest_list(rest_df, rest_title, top=30):
    
    #Extract information from the input restaurant as we want to get restaurants that are similar to the input
    target_rest_index = rest_df[rest_df['rest_name'] == rest_title].index.values
     
    #Take out information from one that has similar cosine similarity as the input restaurant
    sim_index = gerne_c_sim[target_rest_index, :top].reshape(-1)
    #Exclude oneself from the recommendation
    sim_index = sim_index[sim_index != target_rest_index]
    
    #Make into a dataframe, sort, and return the result
    result = rest_df.iloc[sim_index].sort_values('rest_density', ascending=True)[:10]
    #result = rest_df.iloc[sim_index]
    return result


#Make recommendation by rating
def get_recommend_rest_list2(rest_df, rest_title, top=30):
    
    #Extract information from the input restaurant as we want to get restaurants that are similar to the input
    target_rest_index = rest_df[rest_df['rest_name'] == rest_title].index.values
    
    #Take out information from one that has similar cosine similarity as the input restaurant
    sim_index = gerne_c_sim[target_rest_index, :top].reshape(-1)
    #Exclude oneself from the recommendation
    sim_index = sim_index[sim_index != target_rest_index]
    
    #Make into a dataframe, sort, and return the result
    result = rest_df.iloc[sim_index].sort_values('rest_rating', ascending=False)[:10]
    #result = rest_df.iloc[sim_index]
    return result

#Get recommendation by ABC recommender(A combination of density and rating)
def get_recommend_rest_list3(rest_df, rest_title, top=30):
    
    #Extract information from the input restaurant as we want to get restaurants that are similar to the input
    target_rest_index = rest_df[rest_df['rest_name'] == rest_title].index.values
    
    #Take out information from one that has similar cosine similarity as the input restaurant
    sim_index = gerne_c_sim[target_rest_index, :top].reshape(-1)
    #Exclude oneself from the recommendation
    sim_index = sim_index[sim_index != target_rest_index]
    
    #Make into a dataframe, sort, and return the result
    result = rest_df.iloc[sim_index].sort_values('recommend', ascending=True)[:10]
    #result = rest_df.iloc[sim_index]
    return result

#Recommendation list by low density
print(get_recommend_rest_list(rest_df, rest_title="강남역점 홍콩반점0410"))
#Recommendation by high rating number
print(get_recommend_rest_list2(rest_df, rest_title="강남역점 홍콩반점0410"))
#Recommendation by ABC recommendation
print(get_recommend_rest_list3(rest_df, rest_title="강남역점 홍콩반점0410"))

