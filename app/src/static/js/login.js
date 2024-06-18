$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    var formData = $(this).serialize(); // Serialize the form data
    fetch("/token",
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(response => {
            if (response === true) {
                location.assign("login_success.html");
            } else {
                alert("Invalid  credentials")
            }
        })
        .catch(error => {
            console.error(error);
        });
  });
});