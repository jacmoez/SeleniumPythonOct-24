*** Settings ***
Library                 SeleniumLibrary


*** Variables ***
${url}                                   https://testautomationpractice.blogspot.com/


*** Keywords ***
Table Data

    Table Data By Name                     BookTable
    Table Data By ID                       taskTable
    Get Pagination Table First Page
    Get Pagination Table All Page
    Pagination Table


Table Data By Name
     [Arguments]                           ${table_name}
     ${cells}=          Get WebElements      //table[@name='${table_name}']//td
     FOR                ${cell}            IN           @{cells}
                        ${text}=          Get Text      ${cell}
                        log                ${text}
     END
     ${rows}=          Get WebElements     //table[@name="${table_name}"]//tr
     FOR               ${row}              IN                       @{rows}
                       ${row_elements}=    Get WebElements          ${row}
                       ${text}=             Get Text                ${row_elements}
                       Log                  ${text}
     END

Table Data By ID
       [Arguments]                      ${table_id}
       ${rows}=            Get WebElements               //table[@id="${table_id}"]//tr
       FOR       ${row}                    IN            @{rows}
                 ${row_elements}=    Get WebElements     ${row}
                 ${text}=             Get Text            ${row_elements}
                 Log                  ${text}
       END


Pagination Table
            ${elements}=            Get WebElements       //ul[@id="pagination"]//li/a
             FOR                    ${element}          IN     @{elements}
                                    Click Element             ${element}
                                    Sleep                     3
             END

Get Pagination Table First Page
            ${rows}=                Get WebElements     //table[@id="productTable"]//tbody/tr
            FOR        ${row}       IN      @{rows}
                       ${row_elements}=    Get WebElements     ${row}
                       ${text}=            Get Text             ${row_elements}
                       Log                 ${text}
            END

Get Pagination Table All Page
       ${elements}=                Get WebElements         //ul[@id="pagination"]//li/a
       FOR    ${element}                IN                  @{elements}
                                    Click Element          ${element}
                                    Sleep                   2
      ${rows}=               Get WebElements       //table[@id="productTable"]//tbody/tr
       FOR        ${row}       IN      @{rows}
                                   ${row_elements}=    Get WebElements     ${row}
                                   ${text}=            Get Text             ${row_elements}
                                   Log                 ${text}
       END
       END

Click Checkbox For One Page
        FOR         ${i}        IN RANGE                1             6         2
                    Click Element               //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[${i}]/td[4]/input
                    Sleep                               2
        END

*** Test Cases ***
Main
    Open Browser        ${url}              browser=Chrome
    Maximize Browser Window
    Table Data
    Click Checkbox For One Page