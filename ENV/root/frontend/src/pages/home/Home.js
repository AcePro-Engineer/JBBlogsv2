import React, { Component } from "react";

import {getBlogHeadingsData} from "../../utils/api/fetchresults";

import PostListing from "../../components/homecomponents/PostListings";

import "./styles/home.css";

{/* TODO: IMPLEMENT PROPER ERROR HANLDING! */}
 
class Home extends Component 
{
  constructor()
  {
     super();

     this.state = { 
       monthsheadingslist: [],
       requestErrorMessage: '',
       errorMessage: ''
      }
  }

  showErrorMessage()
  {
      if(this.state.requestErrorMessage != null && this.state.errorMessage != null)
      {
          return (<h3 className="error">{this.state.requestErrorMessage}<br/>{this.state.errorMessage} </h3>);
      } 
      else if(this.state.errorMessage != null)
      {
          return (<h3 className="error">{this.state.errorMessage}</h3>);
      }
  }

  componentDidMount()
  {
      let withinTheLastSpecifiedDays = 30;

      getBlogHeadingsData(withinTheLastSpecifiedDays,
      (res) => 
      {
          this.setState({monthsheadingslist: res.data})
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
      });
  }

  render() 
  {
    return (
      <div className="home-page">
          <PostListing postheadings={this.state.monthsheadingslist} />
      </div>
    );
  }
}
 
export default Home;
