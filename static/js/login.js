document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login_form");
    if (loginForm) {
        // Select all input, select, and textarea elements inside the login form
        const fields = loginForm.querySelectorAll("input, select, textarea");
        fields.forEach(function(field) {
            // Only add to fields that are not type="hidden"
            if (field.type !== "hidden") {
                if (field.type !== "checkbox") {
                field.classList.add("form-control");
                }
            }
        });
    }
});