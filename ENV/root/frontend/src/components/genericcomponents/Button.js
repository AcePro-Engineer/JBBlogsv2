import React, { Component } from "react";

{/*
    Purpose: Class will be used to create all form button
             components.

    Date created: 2/9/2020
*/}

class Button extends Component
{
    render()
    {
        return (
                    <div className="Button">
                        <button type="button"
                            variant={this.props.buttonVariant}
                            disabled={this.props.IsDisabled}
                            onClick={this.props.handleClick}
                            style={this.props.customStyle}>
                            {this.props.label}
                        </button>
                    </div>
        )
    }
}

export default Button;