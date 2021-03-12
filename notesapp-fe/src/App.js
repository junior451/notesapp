import React, { Component } from 'react'
import { Card, CardText, CardBody, CardTitle } from 'reactstrap'
import axios from "axios";
import DisplayNote from './DisplayNote'

class App extends Component {
  state = {
    notes:[],
    displayNote: false,
    currentNoteTitle: null,
    currentNoteText:null,
    createNewNote:false
  }

  componentDidMount() {
    axios.get("/notes/list")
    .then((res) => this.setState({notes: res.data}))
  }

  viewNote = (title, text) =>{

    this.setState({
      displayNote: !this.state.displayNote,
      currentNoteTitle:title,
      currentNoteText:text
    })
  }

  closeNote = () =>{
    this.setState({
      displayNote:!this.state.displayNote
    });
  }

  renderNotes = () => {
    return this.state.notes.map((note) => (
      <li key={note.pk} className="list-group-item d-flex justify-content-between align-items-center">
        <span>
          {note.title}
        </span>
        <span>
          <button className="btn btn-secondary mr-2" onClick={() => this.viewNote(note.title, note.noteText)}>View</button>{' '}
          <button className="btn btn-danger">Delete</button>
        </span>
      </li>
    ));
  };

  render(){
    return (
      <main className="container" >
        <h1 className="text-black text-uppercase text-center my-4">NotesApp</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button className="btn btn-primary">Create New Note</button>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderNotes()}
                {<DisplayNote showNote={this.state.displayNote} noteTitle={this.state.currentNoteTitle} 
                noteText={this.state.currentNoteText} onClose={this.closeNote}/>}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;
