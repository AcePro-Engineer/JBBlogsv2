import axios from "axios";

{/*
    Purpose: Script sends all POST/PUT/PATCH requests to
             the back end api.

    Date created: 2/8/2020
*/}

{/*
    Function returns a FormData object. FormData object is used
    to send blog post information to the backend api in order
    to save blog post creations/modificatications to the database.
*/}
 function parseBlogData(blogPostData)
 {
    let post_form_data = new FormData()

    post_form_data.append('heading_title', blogPostData.heading_title);
    post_form_data.append('description', blogPostData.description);
    post_form_data.append('preview_image', blogPostData.preview_image);
    post_form_data.append('post_title', blogPostData.post_title);
    post_form_data.append('slug', blogPostData.slug);
    post_form_data.append('status', blogPostData.status);
    post_form_data.append('article', blogPostData.article);
    post_form_data.append('user', blogPostData.user);

    return post_form_data;
}

{/*
    Functions sends all blog post modifcations to the backend api.
*/}
export function saveChanges(changesData, auth_token, callBack, errorCallBack)
{
    if(changesData !== null)
    {
        const postEditsURL = "http://127.0.0.1:8000/post/";

        let formData = parseBlogData(changesData);

        axios.defaults.headers.common['Authorization'] = 'JWT ' + auth_token;

        axios.post(postEditsURL, formData)
            .then(response => {
                if(callBack != null)
                {
                    callBack(response);
                }
            })
            .catch(error => {
                if(errorCallBack != null)
                {
                    errorCallBack(error);
                }
            })
    }
    else
    {
        return () => alert("Invalid post submission");
    }
}

{/*
    Function sends all blog post information to the 
    backend api as a DRAFT post.
*/}
export function saveAsDraft(draftData, auth_token, callBack, errorCallBack)
{
    if(draftData !== null)
    {
        const draftURL = "http://127.0.0.1:8000/draft/";

        let formData = parseBlogData(draftData);

        axios.defaults.headers.common['Authorization'] = 'JWT ' + auth_token;

        axios.post(draftURL, formData)
            .then(response => {
                if(callBack != null)
                {
                    callBack(response);
                }
            })
            .catch(error => {
                if(errorCallBack != null)
                {
                    errorCallBack(error);
                }
            })
    }
    else
    {
        return () => alert("Invalid post submission");
    }
}

{/*
    Function sends all blog post imformation to the backend api
    as a PUBLISHED post.
*/}
export function publishPost(publishData, auth_token, callBack, errorCallBack)
{
    if(publishData !== null)
    {
        const publishURL = "http://127.0.0.1:8000/publish/";

        let formData = parseBlogData(publishData);

        axios.defaults.headers.common['Authorization'] = 'JWT ' + auth_token;
        
        axios.post(publishURL, formData)
            .then(response => {
                if(callBack != null)
                {
                    callBack(response);
                }
            })
            .catch(error => {
                if(errorCallBack != null)
                {
                    errorCallBack(error);
                }
            })
    }
    else
    {
        return () => alert("Invalid post submission");
    }
}
