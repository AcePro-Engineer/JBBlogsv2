import React, { Component } from 'react';
import Card from "./Card";

{/*
    Purpose: Component is used to generate a list of Card display components.
             This list displays all published article headings on the Home page.
*/}

class PostListing extends Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return (
            <div>
                {
                    this.props.postheadings.map(c =>
                    <Card key={c.id} 
                        title={c.heading_title} 
                        image_URL={c.preview_image} 
                        description={c.description}/>)
                }
            </div>
        )
    }
}

export default PostListing;
