import React from 'react';
import SearchBar from './components/SearchBar';
import SearchResults from "./components/SearchResults"
import Nav from "./components/Nav"
import { connect } from 'react-redux';

import { Layout} from 'antd';
const { Footer, Content } = Layout;

class App extends React.Component {
  render(){
    return (
      <div className="App">
        <Nav />  
        <Content>
            <div style={{ padding: 24}}>
                    <center>
                      <SearchBar />
                    </center>
                    <div style={{ padding: 24}}>
                      <SearchResults />
                    </div>
            </div>
        </Content>
        <div  style={ (this.props.search_results).length>0 ? {}: { position:"absolute", bottom:0, color: "blue", width:"100%"  } }>
            <Footer style={{ textAlign: 'center' }}> Stanford University © {(new Date().getFullYear())}, Stanford, California 94305.</Footer> 
        </div>
      </div>
    );
  }

}


const mapStateToProps = (state) => {
  return state.searchReducer;
}

const mapDispatchToProps = (dispatch) => {
  return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(App);

