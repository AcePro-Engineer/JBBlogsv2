import React, { Component } from "react";
import { NavLink, HashRouter } from "react-router-dom";
import {convertToSlug} from "../../utils/convertToSlug";
import "./styles/card.css";

{/*
    Purpose: Component is used to generate a Card display.
             Card is used to display blog heading information.
*/}

class Card extends Component
{
    constructor(props)
    {
        super(props);
    }
    
    render()
    {
        let blogSlug = convertToSlug(this.props.title);

        return (
                <HashRouter>
                    <div key={this.props.id} className="card">
                        <section>
                            <img src={this.props.image_URL}
                                align="left" 
                                alt="cannot display" 
                                width="466" height="311"
                                id="postlisting-img"/>
                            <div id="container">
                                <NavLink to={{
                                        pathname: '/pages/posts/Post/',
                                        search: `${blogSlug}`,
                                        hash: '#'
                                    }}
                                    id="post-title-slug">
                                    <h2>{this.props.title}</h2>
                                </NavLink>
                                <p id="brief-description">{this.props.description}</p>
                            </div>
                        </section>
                    </div>
                </HashRouter>
        );
    }
}

export default Card;
