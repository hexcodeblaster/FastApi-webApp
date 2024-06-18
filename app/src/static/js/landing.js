function myFunction() {
  console.log("out javascript")
  var cookieValue = document.cookie
  .split("; ")
  .find((row) => row.startsWith("access_token="));
  console.log("cookie value: ", cookieValue);
  if(typeof cookieValue === 'undefined'){
    console.log("cookie value null")
//    location.assign('login.html')
  }
  else{
//    console.log(cookieValue, typeof cookieValue)
    fetch(
        '/customer/authenticate',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain'
            },
            body: JSON.stringify(cookieValue)
        }
    ).then( response => response == "success")
    .then( () => {
        console.log("success from fetch method")
        location.href = "login_success.html"
    }
    )
    .catch(error => console.log("fetch error: ", error))
  }
}
myFunction()