# ABC

# 프로젝트 설명

# installation
Either through cloning with git or by using npm (the recommended way):
We use google maps api.
`npm install react-google-maps --save`
`npm install react-geocode --save`

# Quick Test
### React
```
import React from "react";
```

### Google Maps API
In order to run the end-to-end tests, you'll need to supply your API key via an environment variable.
Inpout your api key to {MY_API_KEY}.

```
Geocode.setApiKey("{MY_API_KEY}")
```
```
<MapWithAMarker
          googleMapURL="https://maps.googleapis.com/maps/api/js?key={MY_API_KEY}&v=3.exp&libraries=geometry,drawing,places"
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={<div style={{ height: `100vh` }} />}
          mapElement={<div style={{ height: `100%` }} />} />```

and 

```npm start```

# License
MIT
