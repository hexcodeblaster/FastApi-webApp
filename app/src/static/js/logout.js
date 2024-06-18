$(document).ready(function() {
    $("#logout_button").click(function(){
        fetch('/logout')
            .then(response => response.json())
                .then(data => {
                  if (data === true){
                    location.assign("index.html")
                  }
                })
            .catch(error => {
                  console.error('Error:', error);
                });
        });
});
