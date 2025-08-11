document.addEventListener('DOMContentLoaded', function () {
        // Handle "All" checkbox logic
        function handleAllCheckbox(allCheckbox, filterCheckboxes) {
            allCheckbox.addEventListener('change', function () {
                if (this.checked) {
                    filterCheckboxes.forEach(cb => cb.checked = false);
                }
            });

            filterCheckboxes.forEach(checkbox => {
                checkbox.addEventListener('change', function () {
                    if (this.checked) {
                        allCheckbox.checked = false;
                    }
                    // If no filter checkboxes are checked, check "All"
                    const anyChecked = filterCheckboxes.some(cb => cb.checked);
                    if (!anyChecked) {
                        allCheckbox.checked = true;
                    }
                });
            });
        }

        // Brand checkboxes
        const allBrandsCheckbox = document.getElementById('allBrands');
        const brandCheckboxes = document.querySelectorAll('input[name="brand"]');
        handleAllCheckbox(allBrandsCheckbox, brandCheckboxes);

        // Heat checkboxes
        const allHeatCheckbox = document.getElementById('allHeat');
        const heatCheckboxes = document.querySelectorAll('input[name="heat"]');
        handleAllCheckbox(allHeatCheckbox, heatCheckboxes);

        // Flavour checkboxes
        const flavourTypes = ['fruit', 'garlic', 'sweet', 'smoke', 'salt', 'vinegar'];
        flavourTypes.forEach(flavour => {
            const allFlavourCheckbox = document.getElementById(`all${flavour.charAt(0).toUpperCase() + flavour.slice(1)}`);
            const flavourCheckboxes = document.querySelectorAll(`input[name="${flavour}"]`);
            if (allFlavourCheckbox && flavourCheckboxes.length > 0) {
                handleAllCheckbox(allFlavourCheckbox, flavourCheckboxes);
            }
        });

        // Auto-submit form when checkboxes change (optional)
        const filterCheckboxes = document.querySelectorAll('.filter-checkbox');
        filterCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function () {
                // Uncomment the line below if you want auto-submit on checkbox change
                // document.getElementById('filterForm').submit();
            });
        });
    });