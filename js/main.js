import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work.js';

const myWork = [
  {
    'title': "Serverless Website",
    'image': {
      'desc': "",
      'src': "",
      'comment': ""
    }
  },
  {
    'title': "Resume",
    'image': {
      'desc': "",
      'src': "",
      'comment': ""
    }
  },
  {
    'title': "",
    'image': {
      'desc': "",
      'src': "",
      'comment': ""
    }
  }
]

ReactDOM.render(<ExampleWork />, document.getElementById('example-work'))
