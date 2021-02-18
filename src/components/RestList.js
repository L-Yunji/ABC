import React, { Component } from 'react';
import RestData from '../data/rests.json';
import './../styles/rest.css';

class RestList extends Component {
    render() {
        return (
            <div>
                {RestData.map((RestDetail, index) => {
                    return <div>
                    <h2>{RestDetail.rest_name}</h2>
                    <p className="contents">
                    {RestDetail.rest_address}<br/>
                    {RestDetail.rest_number}<br/>
                    {RestDetail.rest_category}<br/>
                    <div>평점: {RestDetail.rest_rating}</div>
                    <div>밀집도: {RestDetail.rest_density}</div>
                    <hr width="100%"></hr>

                    </p>
                    </div>
                })}
            </div>
        );
    }
}

export default RestList;