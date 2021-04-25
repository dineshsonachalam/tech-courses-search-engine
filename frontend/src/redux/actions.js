// Step 2: Create Actions for your Action Types

import { UPDATE_AUTOCOMPLETE_OPTIONS,
         UPDATE_SEARCH_QUERY,
         UPDATE_SEARCH_RESULTS} from './actionTypes';

export const updateAutoCompleteOptions = (autocomplete_options) => {
    return {
              type: UPDATE_AUTOCOMPLETE_OPTIONS,
              payload: {
                autocomplete_options: autocomplete_options
              }
    }
}

export const updateSearchQuery = (search_query) => {
  return {
            type: UPDATE_SEARCH_QUERY,
            payload: {
              search_query: search_query
            }
  }
}

export const updateSearchResults = (search_results) => {
  return {
            type: UPDATE_SEARCH_RESULTS,
            payload: {
              search_results: search_results
            }
  }
}

