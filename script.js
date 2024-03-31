document.addEventListener("DOMContentLoaded", function() {
    const skillsForm = document.getElementById('skillsForm');
    const skillsInput = document.getElementById('skills');
    const questionsTextarea = document.getElementById('questions');

    skillsForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const skills = skillsInput.value.trim();
        if (skills !== '') {
            // Store the skills
            storeSkills(skills);

            // Clear the skills input
            skillsInput.value = '';

            // Update questions related to skills (you can customize this part)
            const questions = generateQuestions(skills);
            questionsTextarea.value = questions;
        }
    });

    function storeSkills(skills) {
        // You can store the submitted skills data as needed (e.g., in local storage, send to server, etc.)
        // For demonstration purpose, let's just log it to the console
        console.log('Submitted skills:', skills);
    }

    function generateQuestions(skills) {
        // This function generates questions related to the entered skills
        // You can customize this part based on your requirements
        // For demonstration purpose, let's just return a static set of questions
        const skillList = skills.split(',').map(skill => skill.trim());
        let questions = '';
        skillList.forEach(skill => {
            questions += `Q: What are some applications of ${skill}? \n`;
            questions += `Q: How would you rate your proficiency in ${skill}? \n`;
            questions += `Q: Can you provide an example of when you have used ${skill}? \n\n`;
        });
        return questions.trim();
    }
});
