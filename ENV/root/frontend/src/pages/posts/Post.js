import React, { Component } from "react";

import {getPostData} from "../../utils/api/fetchresults";

import './styles/post.css';

{/*
    Purpose: Form displays Blog Post article.

    Date created: 2/21/2020
*/}

class Post extends Component
{
    constructor(props)
    {
        super(props);

        this.state = {
            postTitle: '',
            articleBody: '',
            image: '',
            requestErrorMessage: '',
            errorMessage: ''
        }
    }

    getSearchString(search)
    {
        if(search != null)
        {
            if(search.length > 1)
            {
                let strLength = search.length;
                return search.slice(1, strLength);
            }
        }

        return search;
    }

    componentDidMount()
    {
        let blogSlug = this.getSearchString(this.props.location.search);

        getPostData(blogSlug,
            (response) =>
            {
                this.setState({
                    postTitle: response.data.post_title,
                    articleBody: response.data.article,
                    image: response.data.post_image,
                    isLoaded: false
                });
            },
            (error) =>
            {
                if(error != null && error.response != null)
                {
                    alert(error.message);
                    this.setState({requestErrorMessage: error.message});
                    this.setState({errorMessage: error.response.data.message});
                }
                else
                {
                    this.setState({errorMessage: 'An unknown error has occurred please report this issue to your system administrator.'});
                }
            });
    }

    render()
    {
        return (
            <div className="Post">
                <div id="post-content">
                    <img src={this.state.image}
                        align="left" 
                        alt="cannot display" 
                        width="50%" height="50%"
                        id="postlisting-img"
                    />
                    <h1 id="articleTitle">{this.state.postTitle}</h1>
                    <p id="article">
                        {this.state.articleBody}
                    </p>
                </div>
            </div>
        )
    }
}

export default Post;
