*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start From Register Page

*** Test Cases ***
Register With Valid Username And Password
    Add Username  kalle
    Add Password  kalle123
    Add Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Add Username  ka
    Add Password  kalle123
    Add Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Add Username  kalle
    Add Password  kalle
    Add Password Confirmation  kalle
    Submit Register Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Add Username  kalle
    Add Password  kalle123
    Add Password Confirmation  kalle321
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Succesful Registration
    Add Username  kalle
    Add Password  kalle123
    Add Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Login With Valid Credentials  kalle  kalle123
    Main Page Should Be Open

Login After Failed Registration
    Add Username  ka
    Add Password  kalle123
    Add Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail
    Go To Login Page
    Login Page Should Be Open
    Login With Valid Credentials  ka  kalle123
    Login Page Should Be Open

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Login With Valid Credentials
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Password  password  ${password}
    Click Button  Login

Add Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Add Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Add Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Start From Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open