#!/usr/bin/env python
# coding: utf-8

# Refine restaurant data
# Import restaurant data in dataframe format
import pandas as pd

df = pd.read_csv('C:\\Users\\user\\Desktop\\서울특별시 강남구 일반음식점 인허가 정보.csv', encoding="utf-8")
df.head(5)
df.columns

# Extract operating restaurants
df2 = df[df['상세영업상태명']=='영업']
# Extract columns
df2 = df2[['사업장명', '전화번호', '지번주소', '업태구분명', '좌표정보(X)', '좌표정보(Y)']]
df2.head(5)
len(df2)

# Check if there are null values
df2.isna()

# Drop rows with null values
df2 = df2.dropna(axis=0)
df2

# Reset index number
df2 = df2.reset_index(drop=True)

#Filtering out with '전화번호' to check it the numbers start with the right area code and are in 9 digits
list_i = []

for i in range(len(df2)):
    if len(df2['전화번호'][i])!= 10:
        if df2['전화번호'][i][:2]!='02':
            list_i.append(i)
            df3 = df2.drop(list_i)

df3.head(5)
len(df3)

#Save as a csv file
df3.to_csv('rest_02.csv')

#Reset index
df3 = df3.reset_index(drop=True)

#Filter by '업태구분명' to extract restaurants that offer lunch menus
cate_list = []

cate = ~(df3['업태구분명'].str.contains('호프/통닭|라이브카페|감성주점|정종/대포집/소주방|전통찻집'))
'''
for m in range(len(df3)):
    if cate is True:
        cate_list.append(m)
print(cate_list)
'''
df4 = df3[cate]
len(df4)

df4.to_csv('rest_03.csv')


#Import Google Geocoding API to get location data of restaurants
import googlemaps
from datetime import datetime

key_number = 'YOUR KEY NUMBER' #You need to first get the api key from Google
gmaps = googlemaps.Client(key=key_number)

loc_list = []
for i in df4['지번주소']:
    i = str(i)
    loc_list.append(i)


# In[197]:


#Get latitude and longtitude from gmaps api and store in a list
loc = loc_list
loc_num_list = []

for j in loc:
    result = gmaps.geocode(j, language="ko")
    try:
        latit = result[0]['geometry']['location']['lat']
    except IndexError:
        pass
    try:
        longti = result[0]['geometry']['location']['lng']
    except IndexError:
        pass
    locat_list = [latit, longti]
    loc_num_list.append(locat_list) 

loc_for_rest = pd.Series(loc_num_list)
loc_for_rest
loc_for_rest.to_csv('음식점 좌표.csv')

rest_loc_df = pd.read_csv('음식점 좌표.csv')
rest_loc_df.columns = ['인덱스', '좌표']
rest_loc_df = rest_loc_df['좌표']
rest_loc_df.head(5)
rest_loc_df.to_csv('음식점 좌표 추출.csv')

# Assign column names and reset index to the original dataset
# Location, rating, and density information will be added as columns
df_refine = df4[['사업장명', '업태구분명', '전화번호', '지번주소']]
df_refine.reset_index(drop=True)
df_refine.to_csv('공공데이터 전처리.csv')

#Generate rating data of restaurants
rating_list = []
import random

for i in range(len(df_refine)):
    x = random.uniform(50, 100)
    x = round(x, 2)
    rating_list.append(x)
rating_df = pd.Series(rating_list)
rating_df.mean()

#Generate density data of restaurants
density_list = []
import random

for i in range(len(df_refine)):
    x = random.uniform(0, 100)
    x = round(x, 2)
    density_list.append(x)
density_df = pd.Series(density_list)
density_df.mean()

df_extra = pd.concat([rest_loc_df, rating_df, density_df], axis=1)
df_extra.columns = ["좌표", "평점", "밀집도"]
len(df_extra)

df_extra.to_csv('음식점 좌표 평점 밀집도.csv')

#Concatenate original data and the dataframe with location, rating, and density
df_final = pd.concat([df_refine, df_extra], axis=1)