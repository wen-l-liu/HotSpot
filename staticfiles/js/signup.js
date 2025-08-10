document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById("signup_form");
    if (signupForm) {
        // Select all input, select, and textarea elements inside the signup form
        const fields = signupForm.querySelectorAll("input, select, textarea");
        fields.forEach(function(field) {
            // Only add to fields that are not type="hidden"
            if (field.type !== "hidden") {
                field.classList.add("form-control");
            }
        });
    }
});