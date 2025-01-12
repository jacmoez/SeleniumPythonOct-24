*** Settings ***
Library                 SeleniumLibrary

*** Variables ***
${url}                                   https://testautomationpractice.blogspot.com/
${data_btn}                              //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[8]/button
${img1}                                 C:\\Users\\DELL\\Pictures\\Screenshots\\Screenshot 2025-01-04 161705.png
${img2}                                 C:/Users/DELL/Pictures/Screenshots/Screenshot 2024-12-28 003144.png

*** Keywords ***
Data Picker
      Input Text                        id:datepicker                07/29/1997
      Sleep                             2
      Click Element                     id:datepicker                RETURN
      Sleep                             2
      Click Element                     id:txtDate
      Sleep                             2
      Click Element                     xpath:/html/body/div[5]/table/tbody/tr[3]/td[4]/a
      Sleep                             2
      Input Text                        id:start-date              07/29/1997
      Sleep                             2
      Input Text                        id:end-date                01/12/2025
      Sleep                             2
      Click Button                      ${data_btn}
      ${result}                         Get Text                    id:result
      Log                               ${result}
      #Click Element                     class:home-link

File Upload
       Choose File                          id:singleFileInput                  ${img1}
       Sleep                                2
       Click Button                         css:#singleFileForm button
       Sleep                                2
       Choose File                          id:multipleFilesInput                ${img1}\n${img2}
       Sleep                                2
       Click Button                         css:#multipleFilesForm button
       ${result}                            Get Text                               id:multipleFilesStatus
       Log                                  ${result}

Table Data
      Table Data By Name                   BookTable
      Table Data By ID                     taskTable

Table Data By Name
       [Arguments]                          ${table_name}
       ${cells}=                            Get WebElements                 xpath://table[@name="${table_name}"]//td
       FOR      ${cell}         IN          @{cells}
                ${text}=     Get Text       ${cell}
                Log                         ${text}
       END

       ${rows}=                             Get WebElements                 xpath://table[@name="${table_name}"]//tr
       FOR      ${row}          IN          @{rows}
                ${row_elements}=            Get WebElements                 ${row}
                ${text}=                    Get Text                        ${row_elements}
                Log                         ${text}
       END

*** Test Cases ***
Main
    Open Browser        ${url}              browser=Edge
    Maximize Browser Window
    Data Picker
    File Upload
    Table Data
    Sleep                                    5