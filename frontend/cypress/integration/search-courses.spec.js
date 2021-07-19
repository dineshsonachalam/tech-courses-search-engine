describe("Search courses", () => {
    it("Load search page", () => {
        cy.visit("http://localhost:3000");
        cy.wait(5000);
    });
    
    it("Type the course", () => {
        cy.get("#rc_select_0").type("rust").type("{enter}");
        cy.wait(5000);
    });
     
    it("Compare search result", () => {
        cy.wait(10000);
        let expected_courses = [
                        {
                            "title": "The Rust Programming Language",
                            "upvotes": "6",
                            "topic": "Rust"
                        },
                        {
                            "title": "Intro to the Rust programming language",
                            "upvotes": "5",
                            "topic": "Rust"
                        }
        ];
        for (var index=0; index < expected_courses.length; index++) {   
            const index_pos = index;
            cy.get(`:nth-child(${index_pos+1}) > .ant-list-item-meta > .ant-list-item-meta-content > .ant-list-item-meta-title > a`).then(($title_elem) => {
            }).contains("Rust");
            cy.get(`:nth-child(${index_pos+1}) > .ant-list-item-action > :nth-child(2) > .ant-tag > :nth-child(2)`).then(($topic_elem) => {
            }).contains("Rust");
        }
    });
})
