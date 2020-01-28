import React, { Component } from "react";

class DashBoard extends Component {
  constructor() {
    super();
    this.state = {
      points: []
    };
    this.handlePoints = this.handlePoints.bind(this);
  }

  handlePoints(event) {
    const url = "http://localhost:5000/get-weather";

    fetch(url, {
      method: "GET",
      credentials: "include"
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          this.setState({ points: data.result });
        }
      })
      .catch(error => {
        return [];
      });
    event.preventDefault();
  }

  render() {
    const text = this.state.points.map(point => (
      <li>
        lat = {point[0]} - long = {point[1]}
      </li>
    ));
    return (
      <div>
        <button type="submit" onClick={this.handlePoints}>
          Find
        </button>
        {text}
      </div>
    );
  }
}

export default DashBoard;
