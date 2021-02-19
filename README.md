# HELLO, ABC(AI Beyond COVID19) - *[BOK JAK]*

```
"hello, we are Bok Jak, we solve your problem of safe and happy meal."
```
For 2021 KPMG Ideation Challenge

# *[Bok Jak]* solves all of your problems with Covid19

**[Bok Jak]** is responsible for your time and safety by providing dense information.
Did you not have enough time to find a restaurant with fewer people during the limited lunch time?
The delivery has increased due to Covid19, but has the sales been affected by the decrease in customers compared to before?
It's difficult to operate the company due to Covid19, do you want to reduce the operating cost?
Use **[Bok Jak]**.
Complexity is everything that solves all your problems.
Furthermore, we will enter a country suffering from Covid19 like Japan and provide safe and free meals to people around the world.

# Purpose of *[Bok Jak]*
*Team ABC* is made for a person that wants to have a safe meal with Covid19, restaurant owners that want to make a profit before Covid19, and a company that wants to reduce operating costs for its employees to have a safe meal.
We provide real-time density information for you and provides recommendation services to help diners make decisions for freer and safer meals. 
**[Bok Jak]** will also provide non-face-to-face order and payment services.
Finally, our goal is to reduce face-to-face contact with diners and restaurant staff to create a non-face-to-face meal and provide safety and freedom to individuals, restaurant owners and companys.

# what is your problem?
## 🙋 person :
* I want to eat a safe meal in a place with fewer people. 
* I visited several restaurants in person to find a restaurant with few people.
* It takes a lot of time to find a restaurant with fewer people.
* I always use the map app to use the visitor trend service in the restaurant, but not accurate.

## 👩‍🍳 restaurant owners :
* Sales plunge to Covid19. 
* There are online food services such as delivery, but I don't capture the same sales as before.
* Inventory should be thrown away because there are few customers.
* If there is a confirmed case in the store, I have to shut down our business, so I'm so worried about safety.

## 🏢 Company : 
* We were hit by sales with Covid19, which feel burdened by operating expenses. 
* If there is a confirmed case among employees, we should be shut down, so they should live a safe life.
* Employees are looking for restaurants with fewer people, so they don't start working even after lunch.

# Why *[Bok Jak]*
- McKinsey & Company's survey shows that Corona 19 has reduced meals in restaurants by 49%.

![Github](image/Changes in Korean food consumption pattern after COVID-19.png)

- According to data from the Gyeonggi Provincial Statistics Office, the most important factor in selecting restaurants after Covid19 is the density of customers (28%).

![Github](image/What to consider when choosing a restaurant after COVID-19.png)

- According to the Korea Institute for Food and Rural Affairs, the 2020 Food Industry Business Index has continued to fall since Covid19, the lowest at 59.33% in the fourth quarter of 2020.

![Github](image/Food industry economy flow.png)

- According to the Ministry of Agriculture, Food and Rural Affairs, the proportion of restaurant businesses has increased since the Covid19 outbreak, reaching 95.2% in the fourth quarter of 2020.

- The same survey also showed that restaurant businesses saw their decline to 59.2% in the fourth quarter of 2020.

![Github](image/코로나19 발생 이후 산업단지 외식업 매출 감소 추이.png)

- In these surveys, Even if the delivery service is used, it is difficult for restaurants to recover their sales, and consumers regard the density of customers as an important factor in selecting restaurants.
- So we create **[Bok Jak]**, which reduces face-to-face contact in the restaurant as much as possible.

# Solution
## Built With
* Scikit-learn
* Google Maps API

## Installation
Either through cloning with git or by using npm (the recommended way):<br/>
We use google maps api.
`npm install react-google-maps --save`
`npm install react-geocode --save`

## Quick Test
#### React
```
import React from "react";
```

#### Google Maps API
In order to run the end-to-end tests, you'll need to supply your API key via an environment variable.<br/>
Inpout your api key to {MY_API_KEY}.

```
Geocode.setApiKey("{MY_API_KEY}")
```

```
<MapWithAMarker googleMapURL="https://maps.googleapis.com/maps/api/js?key={MY_API_KEY}&v=3.exp&libraries=geometry,drawing,places" />
```         
 

and 

```npm start```


#### Python
```
pip install scikit-learn
pip install pandas
pip install numpy
pip install scipy
pip install googlemaps
```

#### Google Maps Geocoding API
For testing, you'll need to supply your API key for geocoding and add it in recommender_model/data_refining.py.

# How to use
## 👩‍🏫 Tutorial (여기에 유저 입장에서 앱을 사용하는 화면을 캡쳐해서 넣고 설명을 넣을 것)

# About Team ABC
https://github.com/Soyeon-ErinLee/Dobby-AI
About us, Dobby-AI
이 링크의 어바웃 어스처럼 우리에 대한 설명을 한 페이지로 만들어서 넣는건?

*Team ABC* is made up of Brilliant business logists, professional developers, and experienced designers.
After Covid19, we had an uneasy meal with precious people.
This kind of problem is also experienced by other people who value safety with Covid19.
We have a professional career history in each field.

|Photo|Name|Role|
|--|--|--|
|![image description](image/한정은.jpg)|Han Jeung Eun|Team Leader-Business Logistics|
|![image description](image/조규민.jpg)|조규민|Business Logistics|
|![image description](image/오채은.jpg)|오채은|Design/Front-end/Interface|
|![image description](image/이윤지.jpg)|이윤지|Engineering/Logic/Network/Data Science/Algorithm|
|![image description](image/이송.jpg)|Lee Song|Data/Database/Data Science/Algorithm|


This experience allows *Team ABC* to make up for their shortcomings and create synergy effects.
*Team ABC* can provide safer and freer meals to people through our synergy effect.

<!--Quote-->
> Keep distance, stay together, [Bok Jak]!

# License
MIT
