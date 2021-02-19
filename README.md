# ABC

# BokJak

# installation
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

# License
MIT
