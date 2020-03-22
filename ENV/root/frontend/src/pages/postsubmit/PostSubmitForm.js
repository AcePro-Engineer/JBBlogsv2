import React, { Component } from "react";

import {saveChanges} from "../../utils/api/postresults";
import {saveAsDraft} from "../../utils/api/postresults";
import {publishPost} from "../../utils/api/postresults";
import {convertToSlug} from "../../utils/convertToSlug";

import TextField from "../../components/genericcomponents/TextField";
import TextAreaField from "../../components/genericcomponents/TextAreaField";
import Button from "../../components/genericcomponents/Button";

import './styles/submit.css';

import PostSubmitFormErrors from "../../components/errorcomponents/PostSubmitFormErrors";

{/*
    Purpose: Form handles the creation of blog Posts.

    Date created: 2/12/2020
*/}

{/* 
    DEVELOPER NOTE: Using an inline CSS style in order
                    to ensure the necessary styles
                    are applied to my custom components.
                    For some reason my custom components
                    cannot be styled by an external style
                    sheet. I will revisit this issue
                    at a later time.
*/}

{/*
    POST STATUES: 0 - DRAFT
                  1 - PUBLISHED
*/}

const textFieldStyles = {
    width: '98%'
}

const headingDescriptionStyles = {
    width: '98%',
    height: '75px'
}

const articleBodyStyles = {
    width: '98%',
    height: '340px'
}

const buttonStyes = {
    margin: '5px',
    backgroundColor: '#008CBA',
    border: 'none'
}

class PostSubmitForm extends Component
{
    constructor(props)
    {
        super(props);

        this.handleHeadingChange = this.handleHeadingChange.bind(this);
        this.handlePostChange = this.handlePostChange.bind(this);
        this.handleImageChange = this.handleImageChange.bind(this);

        this.handleSaveChanges = this.handleSaveChanges.bind(this);
        this.handleSaveAsDraft = this.handleSaveAsDraft.bind(this);
        this.handlePublish = this.handlePublish.bind(this);
        this.handleCancel = this.handleCancel.bind(this);

        this.state = {
            username: '',
            title: '',
            article_image: null,
            headingDescription: '',
            articleBody: '',
            requestErrorMessage: '',
            errorMessage: '',
            formErrors: {userId: '',
                         headingTitle: '', 
                         headingDescriptionIsNull: '',
                         headingDescriptionIsLessThanFiveChars: '',
                         headingDescriptionIsGreaterThanOneHundChars: '',
                         articleTitleIsNull: '',
                         articleTitleIsLessThanFiveChars: '',
                         articleTitleIsGreaterThanOneHundChars: '',
                         articlebodyIsNull: '',
                         articleBodyIsLessThanTwoHundChars: '',
                         articleSlugIsNull: ''},
            headingIsValid: false,
            postIsValid: false,
            formIsValid: false,
            headingChanged: false,
            postChanged: false
        }
    }

    loadPostData()
    {
        {/*
            Method loads the post information via the form props.
            Post information is only loaded this way if a pre-existing
            post is selected to be edited by the post owner.
        */}

        this.setState({
            title: this.props.title,
            article_image: this.props.article_image,
            headingDescription: this.props.headingDescription,
            articleBody: this.props.articleBody
        });
    }

    createData()
    {
        {/*
            Function creates request objects(heading/post) that will sent to 
            the api to be saved to the database.
            
            Params: createHeaderObject - Expected Type: boolean
                    If true create heading object.
        */}

        let blogPostObj = {
            heading_title: this.state.title,
            description: this.state.headingDescription,
            preview_image: this.state.article_image,
            post_title: this.state.title,
            slug: convertToSlug(this.state.title),
            article: this.state.articleBody,
            user: this.state.username,
            headingChanged: this.state.headingChanged,
            postChanged: this.state.postChanged
        }

        return blogPostObj;
    }

    handleHeadingChange(event)
    {
        {/*
            Event method handles all blog heading related changes.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        const value = event.target.value;
        const name = event.target.name;

        this.setState({headingChanged: true});
        this.setState({[name]: value},
            () => {this.validateField(name, value)});
    }

    handlePostChange(event)
    {
        {/*
            Event method handles all blog post related changes.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        const value = event.target.value;
        const name = event.target.name;

        this.setState({postChanged: true});
        this.setState({[name]: value},
            () => {this.validateField(name, value)});
    }

    handleImageChange(event)
    {
        {/*
            Event method handles all blog image related changes.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        const image_file = event.target.files[0];

        this.setState({headingChanged: true,
                       postChanged: true,
                       article_image: image_file});
    }

    handleSaveChanges(event)
    {
        {/*
            Event method saves all blog heading/article changes.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        let blogPostData = this.createData();
        let auth_token = localStorage.getItem('token');

        saveChanges(blogPostData, auth_token,
            (res =>
            {
                alert("Changes saved!");
            },
            (err) =>
            {
                if(err != null && err.response != null)
                {
                    this.setState({requestErrorMessage: err.message});
                    this.setState({errorMessage: err.response.data.message});
                    alert(err.message);
                    alert( err.response.data.message);
                }
                else
                {
                    this.setState({errorMessage: 'An unknown error has occurred please report this issue to your system administrator.'});
                }
            }));
    }

    handleSaveAsDraft(event)
    {
        {/*
            Event method saves the article post as a article draft.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        let blogPostData = this.createData();
        let auth_token = localStorage.getItem('token');

        saveAsDraft(blogPostData, auth_token,
            (res =>
            {
                alert("Changes saved!");
            },
            (err) =>
            {
                if(err != null && err.response != null)
                {
                    this.setState({requestErrorMessage: err.message});
                    this.setState({errorMessage: err.response.data.message});
                }
                else
                {
                    this.setState({errorMessage: 'An unknown error has occurred please report this issue to your system administrator.'});
                }
            }));
    }

    handlePublish(event)
    {
        {/*
            Event method publishes the article post.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();

        let blogPostData = this.createData();
        let auth_token = localStorage.getItem('token');

        publishPost(blogPostData, auth_token,
            (res =>
            {
                alert("Changes saved!");
            },
            (err) =>
            {
                if(err != null && err.response != null)
                {
                    this.setState({requestErrorMessage: err.message});
                    this.setState({errorMessage: err.response.data.message});
                }
                else
                {
                    this.setState({errorMessage: 'An unknown error has occurred please report this issue to your system administrator.'});
                }
            }));
    }

    handleCancel(event)
    {
        {/*
            Event method clears the form and/or closes the post edit form.

            Params: event - Expected Type: Event object
                    References all event related properties.
        */}

        event.preventDefault();
    }

    validateField(FieldName, value)
    {
        {/*
            Method hanldes all form field validation.

            Params: FieldName - Expected Type: string
                    Name if field being validated.

                    value - Expected Type: object
                    Value of the correspoding field being validated.
        */}

        let titleIsValid = false;

        let IsNull = false;
        let IsLessThanFiveChars = false;
        let IsGreaterThanOneHundChars = false;

        let IsArticleBodyNull = false;
        let IsBodyLessThanTwoHundChars = false;

        let fielidValidationErrors = this.state.formErrors;
        let headingIsValid = this.state.headingIsValid;
        let postIsValid = this.state.postIsValid;

        switch(FieldName)
        {
            case 'userId':
                headingIsValid = postIsValid = value > 0 ? true : false;
                fielidValidationErrors.userId = headingIsValid && postIsValid ? '' : 'Invalid user.';
            case 'title' :
                titleIsValid = value != null ? true : false;
                fielidValidationErrors.headingTitle = titleIsValid ? '' : 'All post must have a title';
                headingIsValid = postIsValid = titleIsValid;
            case 'headingDescription':
                IsNull = value != null ? true : false;
                fielidValidationErrors.headingDescriptionIsNull = IsNull ? 'All posts must have a short description.' : '';

                IsLessThanFiveChars = value.length > 5 ? true: false;
                fielidValidationErrors.headingDescriptionIsLessThanFiveChars = IsLessThanFiveChars ? 'All short descriptions must be greater than 5 characters.' : '';

                IsGreaterThanOneHundChars = value.length > 100 ? false : true;
                fielidValidationErrors.headingDescriptionIsGreaterThanOneHundChars = IsGreaterThanOneHundChars ? 'All short descriptions can only be 100 characters long.' : '';

                headingIsValid = !IsNull && !IsLessThanFiveChars && !IsGreaterThanOneHundChars;
            case 'articleBody':
                IsArticleBodyNull = value != null ? true : false;
                fielidValidationErrors.articlebodyIsNull = IsArticleBodyNull ? 'All posts must have a article.' : '';

                IsBodyLessThanTwoHundChars = value.length < 200 ? true : false;
                fielidValidationErrors.articleBodyIsLessThanTwoHundChars = IsBodyLessThanTwoHundChars ? 'Articles cannot be less than 200 charaters.' : '';

                postIsValid = !IsArticleBodyNull && !IsBodyLessThanTwoHundChars;
            default:
                break;
        }

        this.setState({formErrors: fielidValidationErrors,
                      headingIsValid: headingIsValid,
                      postIsValid: postIsValid},
                      this.validateForm());
    }

    validateForm()
    {
        {/* 
            Method checks if all changes in the form are valid. 
        */}

        this.setState({formIsValid: this.state.headingIsValid && this.state.postIsValid});
    }

    componentDidMount()
    {
        {/* Username = Owner of blog post. */}
        this.setState({username: this.props.username});

        {/* 
            If "selected for edit" then load the form state via
            the form props values.
        */}

        if(this.props.selectedForEdit)
        {
            this.loadPostData();
        }
    }

    render()
    {
        let errors = [];

        if(this.state.formErrors.length > 0)
        {
            errors = <PostSubmitFormErrors formErrors={this.state.formErrors} />;
        }

        return (
                <div className="PostSubmitForm">
                    <div id="submitform-content">
                        <div id="HeadingSection">
                            <h2>Heading</h2>
                            <label id="headingTitleLabel" for="headingTitleTextBox">Title</label>
                            <TextField controlName="title"
                                    value={this.state.headingTitle}
                                    handleChange={this.handleHeadingChange}
                                    id="headingTitleTextBox"
                                    customStyle={textFieldStyles}
                            />

                            <label id="headingDescLabel" for="headingDescriptionTextBox">Short Description of Article</label>
                            <TextAreaField controlName="headingDescription"
                                    value={this.state.headingDescription}
                                    handleChange={this.handleHeadingChange}
                                    id="headingDescriptionTextBox"
                                    customStyle={headingDescriptionStyles}
                            />
                        </div>
                        <div id="ArticleSection">
                            <h2>Article</h2>
                            <label id="articleBodyLabel" for="articleBodyTextBox">Article Body</label>
                            <TextAreaField controlName="articleBody"
                                    value={this.state.articleBody}
                                    handleChange={this.handlePostChange}
                                    id="articleBodyTextBox"
                                    customStyle={articleBodyStyles}
                            />
                            <label id="articleImageLabel" for="articleImageBox">Add Image</label>
                            <TextField controlName="article_image"
                                    controlType="file"
                                    value={this.state.article_image}
                                    handleChange={this.handleImageChange}
                                    id="articleImageBox"
                                    imageTypes="image/jpeg, image/png"
                            />
                        </div>
                        <div id="buttonArea">
                            <Button buttonVariant="primary"
                                    IsDisabled={false}
                                    handleClick={this.handleSaveChanges}
                                    label="Save Changes"
                                    id="btn-save-changes"
                                    customStyle={buttonStyes}
                            />

                            <Button buttonVariant="primary"
                                    IsDisabled={false}
                                    handleClick={this.handleSaveAsDraft}
                                    label="Save as Draft"
                                    id="btn-save-as-draft"
                                    customStyle={buttonStyes}
                            />

                            <Button buttonVariant="primary"
                                    IsDisabled={false}
                                    handleClick={this.handlePublish}
                                    label="Publish"
                                    id="btn-publish"
                                    customStyle={buttonStyes}
                            />

                            <Button buttonVariant="primary"
                                    IsDisabled={false}
                                    handleClick={this.handleCancel}
                                    label="Cancel"
                                    id="btn-cancel"
                                    customStyle={buttonStyes}
                            />
                        </div>
                    </div>
                </div>
        )
    }
}

export default PostSubmitForm;
