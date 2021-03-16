import React, { Component } from 'react'
import axios from "axios";
import DisplayNote from './DisplayNote'
import CreateNewNote from './CreateNewNote';

class App extends Component {
  state = {
    notes:[],
    displayNote: false,
    currentNoteId:null,
    currentNoteTitle: null,
    currentNoteText:null,
    createNewNote:false
  }

  componentDidMount() {
    axios.get("/notes/list")
    .then((res) => this.setState({notes: res.data}))
  }

  viewNote = (id,title, text) =>{
    this.setState({
      displayNote: !this.state.displayNote,
      currentNoteId: id,
      currentNoteTitle:title,
      currentNoteText:text
    })
  }

  close = () =>{
    this.setState({
      displayNote:false,
      createNewNote:false
    });
  }

  createNote = () =>{
    this.setState({
      createNewNote:!this.state.createNewNote
    });
  }

  deleteNote = (note_id) =>{
    axios.delete(`/notes/delete/${note_id}/`)
    window.location.reload()
  }

  renderNotes = () => {
    return this.state.notes.map((note) => (
      <li key={note.pk} className="list-group-item d-flex justify-content-between align-items-center">
        <span>
          {note.title}
        </span>
        <span>
          <button className="btn btn-success mr-2" onClick={() => this.viewNote(note.pk, note.title, note.noteText)}>View</button>{' '}
          <button className="btn btn-danger" onClick={() => this.deleteNote(note.pk)}>Delete</button>
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
                <button className="btn btn-primary" onClick={this.createNote}>Create New Note</button>
                {<CreateNewNote createNote={this.state.createNewNote} onClose={this.close}/>}
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderNotes()}
                {<DisplayNote showNote={this.state.displayNote} noteTitle={this.state.currentNoteTitle} 
                noteText={this.state.currentNoteText} noteId={this.state.currentNoteId} 
                onClose={this.close}/>}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;
