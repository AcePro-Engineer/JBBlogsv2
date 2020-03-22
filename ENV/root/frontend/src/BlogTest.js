import React, { Component } from "react";
import axios from "axios";

class BlogTest extends Component
{
    state = {
        blogheading: []
    }

    componentDidMount()
    {
        axios.get('http://127.0.0.1:8000/blogs/1')
        .then(res => {this.setState({blogheading: res.data})})
        .catch(error => alert(error));
    }

    render()
    {
        return (
            <div id='blogcontent'>
                <h1>Testing the JBBlog backend application</h1>
                <p>
                    <span>{this.state.blogheading.title}</span><br/>
                    <span>{this.state.blogheading.description}</span>
                </p>
            </div>
        );
    }
}

export default BlogTest;
