// Confirm database reset
$('.reset-database').click(function () {
    confirmReset();
});

// Display window prompt
function confirmReset() {
    var result = confirm("Are you sure you want to reset the database?");
    if (result) {
        window.location.href = "reset_database/";
    }
};