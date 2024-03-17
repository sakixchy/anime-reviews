const filterButton = document.getElementById('filterButton');


filterButton.addEventListener('click', function() {

    let modal = document.getElementById('reviewModal');
    let bootstrapModal = new bootstrap.Modal(modal);
        bootstrapModal.show();
    });
