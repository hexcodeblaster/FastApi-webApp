$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var validation_flag = true
        email_id = $("#email_id").val(),
        user_name = $("#user_name").val(),
        first_name = $("#first_name").val(),
        middle_name = $("#middle_name").val(),
        last_name = $("#last_name").val(),
        phone_no = $("#phone_no").val(),
        password = $("#password").val()
        confirm_password = $("#confirm_password").val()

        // Phone number validation
        const phoneRegex = /^\d{10}$/;
        if (!phoneRegex.test(phone_no)) {
            $('#phone_no').css('border', '2px solid red');
            $('#phone_no_error').text('Phone number must be exactly 10 digits and numeric only.');
            validation_flag = false;
        } else {
            $('#phone_no').css('border', '');
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email_id)) {
            $('#email_id').css('border', '2px solid red');
            $('#email_id_error').text('Please enter a valid email address.');
            validation_flag = false;
        } else {
            $('#email_id').css('border', '');
            $('#email_id_error').text('');
        }

        if (password !== confirm_password) {
            $("#confirm_password").css("border", "2px solid red")
            $("#confirm_password_error").text("password do not match")
            validation_flag = false;
        }
        else {
            $("#confirm_password").css("border", "")
        }

        const data = {
            email_id : $("#email_id").val(),
            user_name : $("#user_name").val(),
            first_name : $("#first_name").val(),
            middle_name : $("#middle_name").val(),
            last_name : $("#last_name").val(),
            phone_no : $("#phone_no").val(),
            password : $("#password").val()
        };

        if (validation_flag) {
            fetch("/customer/create_customer",
                {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(response => {
                    console.log("response: ", response)
                    if (response === true) {
                        location.assign("login_success.html");
                    } else {
                        alert("Invalid  credentials")
                    }
                })
                .catch(error => {
                    console.error(error);
                });
        }

    });
});