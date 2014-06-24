*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=.5
Resource  keywords.txt
Suite Setup  Start browser
#Suite Teardown  Close All Browsers

*** Test Cases ***

Just a test
    [Documentation]  Quick test that at least one client was loaded from test.xlsx

    Log in           test_labmanager  test_labmanager

    Go to                      http://localhost:55001/plone/clients/client-1


*** Keywords ***

Start browser
    Open browser         http://localhost:55001/plone/
    Set selenium speed   0.2
