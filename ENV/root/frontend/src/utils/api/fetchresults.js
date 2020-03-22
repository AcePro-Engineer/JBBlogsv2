import axios from "axios";

{/*
    Purpose: Script sends all GET/HEADER requests to
             the back end api.

    Date created: 2/8/2020
 */}

{/* 
    Function returns a single blog heading record. 
*/}
export function getData(callback, errorcallback)
{
    let singleBlogHeadingURL = "http://127.0.0.1:8000/blogs/1";

    axios.get(singleBlogHeadingURL)
    .then(res => {
        if(callback != null)
        {
            callback(res);
        }
    })
    .catch(err => {
        if(errorcallback != null && err != null)
        {
            errorcallback(err);
        }
    })
}

{/* 
    Function returns a list of blog headings 
    that were created within the specified
    number of days(NOTE: Returning headings for the last 30 days at the present moment.)
*/}
export function getBlogHeadingsData(days, callback, errorcallback)
{
    const blogHeadingsListURL = "http://127.0.0.1:8000/headings/";

    const URL = blogHeadingsListURL + days;

    axios.get(URL)
    .then(res => {
        if(callback != null)
        {
            callback(res);
        }
    })
    .catch(err => {
        if(errorcallback != null  && err != null)
        {
            errorcallback(err);
        }
    })
}

{/* 
    Function returns a blog post record. 
*/}
export function getPostData(slug, callback, errorcallback)
{
    const blogPostURL = "http://127.0.0.1:8000/post/";

    const URL = blogPostURL + slug;

    axios.get(URL)
    .then(res => {
        if(callback != null)
        {
            callback(res);
        }
    })
    .catch(err => {
        if(errorcallback != null  && err != null)
        {
            errorcallback(err);
        }
    })
}
