import React from 'react';
import Header from './components/layout/header';
import Content from './components/layout/content';

class App extends React.Component {
  render() {
    return(
    <div>
      <Header />
      <Content />
    </div>
    )
  }
}

export default App;
