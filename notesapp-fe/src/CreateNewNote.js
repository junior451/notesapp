import axios from "axios";
import React, { Component } from 'react'
import {Modal, ModalHeader, ModalBody, ModalFooter, Button, Form, Input, Label, FormGroup} from 'reactstrap'

class CreateNewNote extends Component {
  state = {
    title: '',
    noteText: ''
  }

  handleChange = (event) => {
    this.setState({
        [event.target.name]: event.target.value,
      });
  }

  saveNote = () => {
    const note = {title:this.state.title, noteText:this.state.noteText}
    axios.post("/notes/new/", note)
    window.location.reload()
  }

  render() {
    return(
      <Modal isOpen={this.props.createNote}>
        <ModalHeader>New Note</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="note title">Title</Label>
              <Input type="text" name="title"  onChange={this.handleChange}></Input>
            </FormGroup>
            <FormGroup>
              <Label for="note text">Text</Label>
              <textarea class="form-control" name="noteText"  rows="6" onChange={this.handleChange}></textarea>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="secondary" onClick={this.props.onClose}>Cancel</Button>
          <Button color="success" onClick={this.saveNote}>Save</Button>
        </ModalFooter>
      </Modal>
    )
  }
}

export default CreateNewNote;