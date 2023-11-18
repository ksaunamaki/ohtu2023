*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed

Register With Valid Username And Invalid Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Not Succeed

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Not Succeed

Login After Successful Registration
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Ohtu Page
    Click Button  Logout
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Ohtu Page Should Be Open

Login After Failed Registration
    Go To Register Page
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Not Succeed
    Go To Login Page
    Set Username  kalle
    Set Password  kalle
    Click Button  Login
    Login Page Should Be Open


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go To Register Page
    Go To Starting Page
    Click Link  Register new user
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Register Should Not Succeed
    Register Page Should Be Open

Submit Credentials
    Click Button  Register
