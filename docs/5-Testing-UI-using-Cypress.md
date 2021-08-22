## 5. Testing UI using Cypress.

**What is Cypress?**

Fast, easy and reliable testing for anything that runs in a browser. Cypress is the most popular choice for Integration testing for web applications.

**Cypress Features**

- Test runner: So hands down one of the best features about Cypress is its test runner. It provides a whole new experience to end-to-end testing.
- Setting up tests: Another great feature that we talked about already is setting up tests are extremely easy, you just install Cypress and then everything gets set up for you
- Automatic waits – you will barely have to use waits when using Cypress
- Stubbing – you can easily stub application function behavior and server response.

**Running Cypress Integration test**

The cypress integration tests for our application is available at frontend/cypress/integration/search-courses.spec.js filepath.

```
dineshsonachalam@macbook tech-courses-search-engine % tree frontend/cypress
frontend/cypress
├── fixtures
│   └── example.json
├── integration
│   └── search-courses.spec.js
├── plugins
│   └── index.js
└── support
    ├── commands.js
    └── index.js

4 directories, 5 files
dineshsonachalam@macbook tech-courses-search-engine % 
```

**Running your Cypress Test in the Cypress Test Runner:**

To open the Cypress Test Runner, you can execute the following command below:
```
npx cypress open
```

Once the Cypress Test Runner opens up, you can execute your test which will show results similar to this below:

You can see all the Cypress commands listed below such as visit, URL & title
All your successful assertions will show in Green and failed assertions in Red.

<img src="https://i.imgur.com/F97ooaD.png"/>
<img src="https://i.imgur.com/jfmBLuk.png"/>