import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.css";

class Login extends Component {
  constructor() {
    super();
    this.state = {
      username: "",
      password: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log("manejando evento", event);
    console.log(event.target.name);
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    var params = {
      username: this.state.username,
      password: this.state.password
    };

    const url = "http://localhost:5000/sign-in";
    var data = JSON.stringify(params);
    fetch(url, {
      method: "POST",
      body: data,
      credentials: "include",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          this.props.history.push("/dashboard");
        }
      })
      .catch(error => {
        this.setState({ alert: true });
      });
    event.preventDefault();
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={this.state.username}
            onChange={this.handleChange}
            required
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={this.state.password}
            onChange={this.handleChange}
            required
          />

          <button type="submit">Login</button>
        </form>
      </div>
    );
  }
}

export default Login;
