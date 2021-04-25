// Step 3: Create reducers for the action types

import { combineReducers } from "redux";

import searchReducer from "./searchReducer";

export default combineReducers({ searchReducer });