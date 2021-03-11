import React, { Component } from 'react'

class DisplayNote extends Component {
  render() {
    return (
    <h1>{this.props.id}</h1>
    );
  }
}

export default DisplayNote;