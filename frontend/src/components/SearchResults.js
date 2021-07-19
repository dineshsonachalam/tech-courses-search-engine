import React from "react";
import { updateSearchResults, updateSearchQuery } from "../redux/actions";
import { List, Space, Tag } from "antd";
import { LikeOutlined,  TagOutlined } from "@ant-design/icons";
import { connect } from "react-redux";

class SearchResults extends React.Component {
  postData(url) {
    const requestOptions = {
      method: "POST"
    };
    fetch(url, requestOptions).then(response => 
      response.json().then(data => ({
          data: data,
          status: response.status
      })
      ).then(result => {
          this.props.updateSearchResults(result.data);
          this.props.updateSearchQuery("");
    }));    
  }

  render() {
    if(this.props.search_query){
      let url = process.env.REACT_APP_API_ENDPOINT+"/string-query-search?query="+this.props.search_query;
      this.postData(url);
    }
    
    const IconText = ({ icon, text }) => (
      <Space>
        {React.createElement(icon)}
        {text}
      </Space>
    );
    
    return (
        <div>
          {(this.props.search_results).length>0 &&
              <List
                  itemLayout="vertical"
                  size="large"
                  pagination={{
                    onChange: page => {
                    },
                    pageSize: 6,
                  }}
                  dataSource={this.props.search_results}
                  renderItem={item => (
                      <List.Item
                        key={item.id}
                        actions={[
                          <IconText icon={LikeOutlined} text={item.upvotes} key="list-vertical-like-o" />,
                          <Tag icon={<TagOutlined />} color="#55acee">{item.topic}</Tag>
                        ]}
                      >
                        <List.Item.Meta
                          title={<a href={item.url} rel="noreferrer" target="_blank">{item.title}</a>}
                          description={
                              <div>
                                {item.labels.map(label => <Tag key={label} color="success">{label}</Tag>)} 
                              </div>
                          }
                        />
                        {item.content}
                      </List.Item>
                  )}
              />
          }
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
    updateSearchQuery: (search_query) => dispatch(updateSearchQuery(search_query)),
    updateSearchResults: (search_results) => dispatch(updateSearchResults(search_results))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchResults);

