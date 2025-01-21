*** Settings ***
Library                 SeleniumLibrary


*** Variables ***
${url}                                   https://testautomationpractice.blogspot.com/
${hidden}                           xpath:/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[2]/a
${dowmload}                         //html/body/div[3]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[3]/a

${dowmload_pdf}                   //html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/button[3]
*** Keywords ***
Fnish
    Sleep                           3
    Click Element                   ${hidden}
    Sleep                           3
    Click Button                    id:toggleInput
    Sleep                           3
    ${result}=                      Get Text             id:statusLabel
    Log                             ${result}
    Click Button                    id:toggleCheckbox
    Sleep                           3
    ${result}=                      Get Text            id:statusLabel
    Log                             ${result}
    Click Button                    id:loadContent
    Sleep                           4
    ${result}=                      Get Text            id:ajaxContent
    Log                             ${result}
    Click Element                   ${dowmload}
    Sleep                           3
    Input Text                      id:inputText                Hello QA Tessting
    Sleep                           3
    Click Button                    id:generateTxt
    Sleep                           3
    Click Element                   id:txtDownloadLink
    Sleep                           3
    Click Button                    id:generatePdf
    Sleep                           3
    Click Element                   id:pdfDownloadLink
    Sleep                           3
    Click Button                    ${dowmload_pdf}


*** Test Cases ***
Main
    Open Browser            ${url}                  browser=Edge
    Maximize Browser Window
    Sleep                   5
    Fnish
    Sleep                   5

