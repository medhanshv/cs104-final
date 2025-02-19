function validateName() {
    /*Check whether name is entered or not.
    Throw an error if name field is empty.
    Error message will be "Full name is required."*/
    if(document.getElementById("fullName").value==""){
        throw("Full name is required.");
    }
}

function validateEmail() {
    /*Check whether email is valid or not, as per the rules stated in problem statement.
    Use regex and test() function to validate the email address.
    Throw an error if email is invalid.
    Error message will be "Invalid Email Address."*/
    email=document.getElementById("email").value;
    let pattern=/^[a-z0-9]+@[a-z]+\.[a-z]{3}$/.test(email);
    console.log(pattern);
    if(!pattern){
        throw ("Error: Invalid Email Address.");
    }
}

function validatePassword() {
    /*Check whether password is made of atleast 8 characters.
    /If not, throw an error.
    Error message will be "Password must be at least 8 characters"*/
    password=document.getElementById("password").value;
    if(password.length<8){
        throw("Error: Password must be at least 8 characters");
    }
}

function ConfirmPassword() {
    /*Check whether the re-entered password is same as the password entered first.
    If not, throw an error.
    Error message will be "Passwords do not match"*/
    password=document.getElementById("password").value;
    repassword=document.getElementById("confirmPassword").value;
    if(password!==repassword){
        throw("Error: Passwords do not match.");
    }

}

function validateForm() {
    try {
        c1=(document.getElementById("fullName").value==="");
        c2=(document.getElementById("email").value==="");
        c3=(document.getElementById("password").value==="");
        c4=(document.getElementById("confirmPassword").value==="");
        if(c1||c2||c3||c4){
            throw("Error: All fields are required.");
        }

        validateName();
        validateEmail();
        validatePassword();
        ConfirmPassword();

        document.getElementById("feedback").innerHTML="<span style='color: green';>Registration successful!</span>";

        // Additional validation rules can be added here

        //After checking all the rules, if the program throws no error, it will reach this part of code.
        //Using "innerHTML" and "span" tag, give the message "Registration successful!" in GREEN colour to the div container "feedback" in index.html.
        //Your code here
    } catch (error) {
         document.getElementById("feedback").innerHTML=`<span style='color: red';>${error}</span>`
        //After checking all the rules, if the program throws an error, it will reach this part of code.
        //Using "innerHTML" and "span" tag, give the error message in RED colour to the div container "feedback" in index.html.
        //Your code here
    }
}
