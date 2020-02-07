*** SETTINGS ***
Library    OperatingSystem
Library    String


*** VARIABLES ***


*** KEYWORDS ***
Write To Existing Or New File
    [Arguments]    ${filename}    @{details}
    ${Path}    Join Path    ${EXECDIR}    SitesFolder    ${file_name}
    :For    ${i}    IN    @{details}
    \    Append To File    ${Path}    ${i}${\n}

Open File & Read Contents
    [Arguments]    ${filename}
    ${Path}    Join Path    ${EXECDIR}    SitesFolder    ${file_name}
    ${items_in_file}    Get Binary File    ${Path}
    # Set Test Variable    ${items_in_file}
    [Return]    ${items_in_file}

Delete Files
    [Arguments]    @{filename}
    :For    ${file}    IN    @{filename}
    \    ${Path}    Join Path    ${EXECDIR}    SitesFolder    ${file}
    \    Remove File    ${Path}
    \    Sleep    0.5

Delete File Contents
    [Arguments]    ${filename}    ${content}
    ${file_contents}    Open File & Read Contents    ${filename}
    @{item_list}    Split To Lines    ${file_contents}
    Remove Values From List    ${item_list}    ${content}
    Delete Files    ${filename}
    Write To Existing Or New File    ${filename}    @{item_list}
