//function
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");
    const resultsContainer = document.getElementById("results");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        //Create a variable
        const name = document.getElementById("name").value;
        const age = document.getElementById("age").value;
        const city = document.getElementById("city").value;

        // Create a new paragraph element
        const paragraph = document.createElement("p");

        // Append the entered text to the paragraph
        paragraph.textContent = `Name: ${name}, Age: ${age}, City: ${city}`;

        // Append the paragraph to the results container
        resultsContainer.appendChild(paragraph);

        // Clear the form fields
        form.reset();
    });
});
