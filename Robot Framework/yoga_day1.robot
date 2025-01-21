*** Settings ***
Library                     SeleniumLibrary


*** Variables ***
${url}                      https://webfront-uat.yogamovement.com/

${close_alart}              //html/body/div/div/aside/div/div[2]/button
${register}                 //*[@id="header"]/div[2]/div/div/nav[1]/ul/li[1]/a
${singup_btn}               //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button
${male}                     //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[1]/label/div/div
${lastname}                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input


*** Keywords ***
Register User
        Sleep                3
        Click Button         ${close_alart}
        Sleep                3
        Click Element        ${register}
        Sleep                3
        Input Text           name:email                         soe@ams.com.mm
        Sleep                3
        Input Text           name:password                       soe123
        Sleep                3
        Click Button         ${singup_btn}
        Sleep                3
        Input Text          name:firstname                          QA
        Sleep                3
        Input Text          ${lastname}                             Soe
        Sleep                3
        Click Element       ${male}
        Sleep                3
        Click Element       class:css-egispl
        Sleep                2
        Click Element       xpath://img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]




*** Test Cases ***
Main
    Open Browser            ${url}              browser=Edge
    Maximize Browser Window
    Register User
    Sleep                   5