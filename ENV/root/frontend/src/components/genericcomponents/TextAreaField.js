import React, { Component } from "react";

{/*
    Purpose: Class will be used to create all text area
             input control components for this application.

    Date created: 2/9/2020
*/}

class TextAreaField extends Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return (
            <div className="TextAreaField">
                <textarea
                    name={this.props.controlName}
                    value={this.props.textValue}
                    onChange={this.props.handleChange}
                    style={this.props.customStyle}
                />
            </div>
        )
    }
}

export default TextAreaField