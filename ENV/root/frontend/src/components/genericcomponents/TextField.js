import React, { Component } from "react";

{/*
    Purpose: Class will be used to create all text input
             control components for this application.

    Date created: 2/8/2020
*/}

class TextField extends Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        let controlType = this.props.controlType !== null ? this.props.controlType : "text";

        return (
            <div className="TextField">
                <input type={controlType}
                    placeholder={this.props.controlPlaceHolder}
                    name={this.props.controlName}
                    value={this.props.textValue}
                    onChange={this.props.handleChange}
                    style={this.props.customStyle}
                    accept={this.props.imageTypes}
                />
            </div>
        )
    }
}

export default TextField;
