describe("Search courses", () => {
    it('Load search page', () => {
        cy.visit("http://localhost:3000")
        cy.wait(5000)
    })
    
    it('Type the course', () => {
        cy.get('#rc_select_0').type('Python').type('{enter}')
        cy.wait(5000)
    })
    
    it('Compare search result', () => {
        cy.wait(10000)
        let expected_courses = [
                        {
                            "title": "Google's Python Class",
                            "upvotes": "213",
                            "topic": "Python"
                        },
                        {
                            "title": "Complete Python Bootcamp",
                            "upvotes": "196",
                            "topic": "Python"
                        },
                        {
                            "title": "Automate the Boring Stuff with Python",
                            "upvotes": "93",
                            "topic": "Python"
                        },
                        {
                            "title": "Official Python Tutorial",
                            "upvotes": "74",
                            "topic": "Python"
                        },
                        {
                            "title": "Working with Strings in Python",
                            "upvotes": "4",
                            "topic": "Python"
                        },
                        {
                            "title": "Learn Python the Hard Way",
                            "upvotes": "293",
                            "topic": "Python"
                        }
        ];
        for (var index=0; index < 6; index++) {   
            const index_pos = index;
            cy.get(`:nth-child(${index_pos+1}) > .ant-list-item-meta > .ant-list-item-meta-content > .ant-list-item-meta-title > a`).then(($title_elem) => {
                let title = $title_elem.text();
                let expected_title = expected_courses[index_pos]["title"];
                expect(title).to.deep.eq(expected_title);
            })
            cy.get(`:nth-child(${index_pos+1}) > .ant-list-item-action > :nth-child(1) > .ant-space > :nth-child(2)`).then(($upvotes_elem) => {
                let upvotes = $upvotes_elem.text();
                let expected_upvotes = expected_courses[index_pos]["upvotes"];
                expect(upvotes).to.deep.eq(expected_upvotes);
            })
            cy.get(`:nth-child(${index_pos+1}) > .ant-list-item-action > :nth-child(2) > .ant-tag > :nth-child(2)`).then(($topic_elem) => {
                let topic = $topic_elem.text();
                let expected_topic = expected_courses[index_pos]["topic"];
                expect(topic).to.deep.eq(expected_topic)
            })
        }
    })
    
})
