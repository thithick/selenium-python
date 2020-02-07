*** SETTINGS ***
Library    OperatingSystem
Library           OperatingSystem
Library    String
# Library           SeleniumLibrary
# Test Teardown     Close All Browsers
Resource    ../module/Resource.robot
# Library     DebugLibrary
# Suite setup    locator setup

# Setup/Tear Down
# Suite Setup
# Test Setup  Setup Browser   ${platform}  ${env}
Test Teardown   Close Browser

*** VARIABLES ***

${urllink}   https://excelmaster.co/compounding/

${excelfile}    //p[11]/a[text()="calculating_interest_correctly"]

${FILENAME}    calculating_interest_correctly1.xlsx

${JSESSIONID}    https://excel2007master.files.wordpress.com/2015/04/calculating_interest_correctly1.xlsx
# ${JSESSIONID}

*** Test Cases ***

Download excel
    # create unique folder
    ${now}    Get Time    epoch
    ${download_directory}    Join Path    ${OUTPUT DIR}    downloads_${now}
    Create Directory    ${download directory}
    ${chrome options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    # list of plugins to disable. disabling PDF Viewer is necessary so that PDFs are saved rather than displayed
    # ${disabled}    Create List    Chrome PDF Viewer
    # ${prefs}    Create Dictionary    download.default_directory=${download directory}    plugins.plugins_disabled=${disabled}
    ${prefs}    Create Dictionary    download.default_directory=${download directory}
    Call Method    ${chrome options}    add_experimental_option    prefs    ${prefs}
    Create Webdriver    Chrome    chrome_options=${chrome options}
    # Goto    chrome://downloads/
    Goto    ${urllink}
    Click Link    ${excelfile}    # downloads a file
    # wait for download to finish
    ${file}    Wait Until Keyword Succeeds    1 min    2 sec    Download should be done    ${download directory}

download file
    Setup Browser   ${platform}  ${env}
    Goto    ${urllink}
    Download File   ${JSESSIONID}    ${urllink}   ${FILENAME}

*** Keywords ***
Download should be done
    [Arguments]    ${directory}
    [Documentation]    Verifies that the directory has only one folder and it is not a temp file.
    ...
    ...    Returns path to the file
    ${files}    List Files In Directory    ${directory}
    Length Should Be    ${files}    1    Should be only one file in the download folder
    Should Not Match Regexp    ${files[0]}    (?i).*\\.tmp    Chrome is still downloading a file
    ${file}    Join Path    ${directory}    ${files[0]}
    Log    File was successfully downloaded to ${file}
    [Return]    ${file}


Download File
    [Arguments]  ${COOKIE}  ${URL}  ${FILENAME}
    ${COOKIE_VALUE} =  Get Cookie   ${COOKIE}
    Run and Return RC  wget  --cookies=on --header "Cookie: ${COOKIE}=${COOKIE_VALUE}" -O ${OUTPUT_DIR}${/}${FILENAME} ${URL}



