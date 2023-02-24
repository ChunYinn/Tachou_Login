function validate() {
    var name = document.forms["form1"]["username"].value;
    var pass = document.forms["form1"]["password"].value;
    if (name=="" || pass=="") {
        alert("Please input a Value");
    }
}   