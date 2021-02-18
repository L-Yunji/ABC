import React from 'react';
import {Redirect} from 'react-router';

import Home from './../pages/Home';
import ABCLocation from './../pages/ABCLocation';
import Popular from './../pages/Popular';
import SafeLocation from './../pages/SafeLocation';

const routes = [
    {
        path: '/',
        exact: true,
        component: () => <Redirect to="/Home" />
    },
    {
        path: '/Home',
        component: () => <Home />
    },
    {
        path: '/ABCLocation',
        component: () => <ABCLocation />
    },
    {
        path: '/SafeLocation',
        component: () => <SafeLocation />
    },
    {
        path: '/Popular',
        component: () => <Popular />
    },
]

export default routes;