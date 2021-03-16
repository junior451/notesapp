import React, { Component } from 'react'
import {Modal, ModalHeader, ModalBody, ModalFooter, Button} from 'reactstrap'
import EditNote from './EditNote'

class DisplayNote extends Component {
  state = {
    open:false
  }

  toggle = () => {
    this.setState({
      open: !this.state.open
    });
  }

  render() {
    return (
      <Modal centered isOpen={this.props.showNote}>
          <ModalHeader>{this.props.noteTitle}</ModalHeader>
          <ModalBody>
            {this.props.noteText}
          </ModalBody>
          <ModalFooter>
            <Button color='primary' onClick={this.toggle}>Edit</Button>
            <Button color='secondary' onClick={this.props.onClose}>Close</Button>
            {<EditNote editNote={this.state.open} onClose={this.toggle} title={this.props.noteTitle} 
            noteText={this.props.noteText} noteId={this.props.noteId}/>}
          </ModalFooter>
      </Modal>
    );
  }
}

export default DisplayNote;