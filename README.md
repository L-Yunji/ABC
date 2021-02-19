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
![image description](file:///C:/Users/user/Desktop/Changes%20in%20Korean%20food%20consumption%20pattern%20after%20COVID-19.png)

# Built With
* Scikit-learn
* Google Maps API

# Installation
Either through cloning with git or by using npm (the recommended way):<br/>
We use google maps api.
`npm install react-google-maps --save`
`npm install react-geocode --save`

# Quick Test
### React
```
import React from "react";
```

### Google Maps API
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


### Python
```
pip install scikit-learn
pip install pandas
pip install numpy
pip install scipy
pip install googlemaps
```

### Google Maps Geocoding API
For testing, you'll need to supply your API key for geocoding and add it in recommender_model/data_refining.py.


# Usage
Here are some screenshots of 'Bokjak' service.

# License
MIT
