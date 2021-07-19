// Step 3: Create reducers for the action types
import {UPDATE_AUTOCOMPLETE_OPTIONS, UPDATE_SEARCH_QUERY, UPDATE_SEARCH_RESULTS} from "../actionTypes";

const initialState = {
    autocomplete_options: [],
    search_query: "",
    search_results: []
};

const searchReducer = (state=initialState, actions) => {
    switch(actions.type) {
        case UPDATE_AUTOCOMPLETE_OPTIONS:
            return {...state, autocomplete_options: actions.payload.autocomplete_options};
        case UPDATE_SEARCH_QUERY:
            return {...state, search_query: actions.payload.search_query};
        case UPDATE_SEARCH_RESULTS:
            return {...state, search_results: actions.payload.search_results};
        default:
            return {...state};
    }
};

export default searchReducer;