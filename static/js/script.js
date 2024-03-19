const filterButton = document.getElementById('filterButton');
const saveChanges = document.getElementById('saveChanges');
const updateForm = document.getElementById('updateForm');


saveChanges.addEventListener('click', function() {
    if (updateForm) {
        updateForm.submit();
    }
    });


filterButton.addEventListener('click', function() {

    let modal = document.getElementById('reviewModal');
    let bootstrapModal = new bootstrap.Modal(modal);
        bootstrapModal.show();
    });
    
