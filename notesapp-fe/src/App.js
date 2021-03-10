import React from 'react'
import axios from "axios";

class App extends React.Component {
  state = {
    notes:[]
  }

  componentDidMount() {
    axios.get("/notes/list")
    .then((res) => this.setState({notes: res.data}))
  }

  render(){
    return(
      <div>
        {this.state.notes.map(note => (
          <div>
            <h2>Title: {note.title} </h2>
            <p>Text: {note.noteText}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
