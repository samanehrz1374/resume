const rmCheck = document.getElementById("rememberMe"),
    textInput = document.getElementById("username");

if (localStorage.checkbox && localStorage.checkbox !== "") {
  rmCheck.setAttribute("checked", "checked");
  textInput.value = localStorage.username;
} else {
  rmCheck.removeAttribute("checked");
  textInput.value = "";
}

function lsRememberMe() {
  if (rmCheck.checked && textInput.value !== "") {
    localStorage.username = textInput.value;
    localStorage.checkbox = rmCheck.value;
  } else {
    localStorage.username = "";
    localStorage.checkbox = "";
  }
}