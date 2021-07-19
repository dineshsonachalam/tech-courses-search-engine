import React from "react";
import ReactDOM from "react-dom";
import "antd/dist/antd.css"
import { Provider } from "react-redux";
// Step 5: Add the redux store to the React App
import store from "./redux/store";

import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  rootElement
);