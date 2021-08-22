## 4. Building UI using React and Redux.

**What is React?**

A declarative, efficient, and flexible JavaScript library for building user interfaces.

**What is Redux?**

Redux is a JS library for managing client data in applications. Redux allow your state to be available in one place. It is used to manage data in your application.

Things to care about when using redux:
1. Identify the state.
2. Write good reducers.
3. Let's redux state handle the rest.

**Building Parts of redux:**

1. Action -> Action have a type field that tells what kind of action to perform and all other fields contain information or data.
2. Reducer -> They are functions that take the (current state and action) and return the new state and tell the store how to do.
3. Store -> The store is the object which holds state of the application.

<img src="https://i.imgur.com/G45gjRr.png"/>

**React components used in our application:**

**What are React components?**

Components are independent and reusable bits of code. They serve the same purpose as JavaScript functions, but work in isolation and return HTML via a render() function.

Components are classified into two types, Class components and Function components.

**What's the difference between class vs functional components:**

In class component, we can access the value of the state by using this.state inside JSX and we would use setState to update the value of the state. You can set the function inside the event or outside of the render() method -- for readability.

In functional component, we would use useState to assign initial state and we would use setCount (in our example) to update the state. If we want to access the value of the state, we can omit this.state and call the name of the state instead, in our case, it would just be count.


**React components used in our application:**

Here all our React components are available in the **src/components** folder.

```
dineshsonachalam@macbook frontend % tree src/components 
src/components
├── Nav.js
├── ResponsiveAntMenu.js
├── SearchBar.js
└── SearchResults.js

0 directories, 4 files
```
<img src="https://i.imgur.com/eYefwnE.png"/>

**How Redux is integrated into this React application:**

Here all our Redux components are available in the **src/redux** folder. Here we intialized Actions, Search Reducer and Redux store.

```
dineshsonachalam@macbook frontend % tree src/redux 
src/redux
├── actionTypes.js
├── actions.js
├── reducers
│   ├── index.js
│   └── searchReducer.js
└── store.js

1 directory, 5 files
```

**To start the UI in development mode:**
```
npm i && npm run start --prefix frontend
```