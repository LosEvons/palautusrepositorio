*** Settings ***
Resource  resource.robot
Test Setup  Enter Registration

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Enter Registration
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Username can only contain letters

Register With Valid Username And Too Short Password
    Input Credentials  kallee  ka
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password can't be exclusively letters

*** Keywords ***
Enter Registration
    Input Register Command