import React, {Component} from 'react';

{/*
    Purpose: Component displays all Post Submit form related errors.

    Date created: 3/15/2020
*/}

class PostSubmitFormErrors extends Component 
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return (
            <div className="PostSubmitFormErrors">
                {
                    this.props.formErrors.map((fieldName, i) =>
                            <p key={i}>{fieldName} {this.props.formErrors[fieldName]}</p>
                    )
                }
            </div>
        )
    }
}

export default PostSubmitFormErrors;
