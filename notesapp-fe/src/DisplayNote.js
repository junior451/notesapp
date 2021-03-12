import React, { Component } from 'react'
import {Modal, ModalHeader, ModalBody, ModalFooter, Button} from 'reactstrap'

class DisplayNote extends Component {
  render() {
    return (
      <Modal centered isOpen={this.props.showNote}>
          <ModalHeader>{this.props.noteTitle}</ModalHeader>
          <ModalBody>
            {this.props.noteText}
          </ModalBody>
          <ModalFooter>
            <Button color='primary'>Edit</Button>
            <Button color='secondary' onClick={this.props.onClose}>Close</Button>
          </ModalFooter>
      </Modal>
    );
  }
}

export default DisplayNote;