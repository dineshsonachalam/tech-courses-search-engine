import React from "react";
import { Input, AutoComplete } from "antd";
import { updateAutoCompleteOptions, updateSearchQuery } from "../redux/actions";
import { connect } from "react-redux";

class SearchBar extends React.Component {

      async getData(url) {
        const response = await fetch(url);
        return response.json();
      }

      async handleSearch(search_query){
        let url = process.env.REACT_APP_API_ENDPOINT+"/autocomplete?query="+search_query;
        const results = await this.getData(url);
        this.props.updateAutoCompleteOptions(results);
      }
      
      onSelect = (value) => {
        this.props.updateAutoCompleteOptions([]);
        this.props.updateSearchQuery(value);
      };      
      
      handleKeyDown = (event) => {
        if (event.key === "Enter") {
            this.props.updateSearchQuery(event.target.value);
          }
      }

      render() {
            return (
              <div>
              <AutoComplete
                dropdownMatchSelectWidth={252}
                style={{
                  width: 600,
                }}
                options={this.props.autocomplete_options}
                onSelect={this.onSelect}
                onSearch={this.handleSearch.bind(this)}
              >
                <Input.Search onKeyDown={this.handleKeyDown} size="large" placeholder="What do you want to learn? " enterButton={false} />
              </AutoComplete>
              </div>
            );
      }
}

// https://stackoverflow.com/a/50225424
const mapStateToProps = (state) => {
  return state.searchReducer;
};

const mapDispatchToProps = (dispatch) => {
  return {
    updateAutoCompleteOptions: (autocomplete_options) => dispatch(updateAutoCompleteOptions(autocomplete_options)),
    updateSearchQuery: (search_query) => dispatch(updateSearchQuery(search_query))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchBar);


