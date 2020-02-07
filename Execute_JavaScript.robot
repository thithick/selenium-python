# Is there a way to provide arguments to “Execute JavaScript” in Robot Framework?
# https://stackoverflow.com/questions/21256845/is-there-a-way-to-provide-arguments-to-execute-javascript-in-robot-framework

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_using_XPath_in_JavaScript#document.evaluate
https://stackoverflow.com/questions/10596417/is-there-a-way-to-get-element-by-xpath-using-javascript-in-selenium-webdriver
https://gist.github.com/gvasanka/64a16d564eea86dd931394d494696b59#file-robotjavascript
https://medium.com/@gvasanka/clicking-element-with-javascript-on-robot-framework-bdcf666ec4e2
https://medium.com/@menchukanton/validation-of-xpath-inside-google-chrome-console-994900c1c9b1


*** Settings ***
Library    OperatingSystem
Library    String
Library    SeleniumLibrary
# Library    Selenium2Library


*** Test Cases ***
Element Should Be in View Test
    [Documentation]     Test to validate that an element isn't view-able and then is view-able.
    ${argList}=    Create List    Sally    45
    Execute JavaScript    alert('Hello ${argList[0]}, you are ${argList[1]} years old');


Element Should Be in View Test
    ${argList}=    Create List    Sally    45
    ${s2l}=    Get Library Instance    SeleniumLibrary
    Call Method    ${s2l.driver}    execute_script    alert('Hello ' + arguments[0] + ', you are ' + arguments[1] + ' years old');    @{argList}

*** Keywords ***
Element Should Be In View
    [Documentation]     Partially Inspired by: https://stackoverflow.com/a/28709012/6152737
    [Arguments]    ${element}
    ${s2l}=     Get Library Instance    SeleniumLibrary
    ${js}=      Get File    IsInViewport.js
    ${visible}=    Call Method
    ...    ${s2l.driver}
    ...    execute_script    ${js} return isInViewport(arguments[0]);    ${element}
    [Return]    ${visible}