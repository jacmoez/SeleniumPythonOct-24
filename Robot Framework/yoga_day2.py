*** Settings ***
Library                     SeleniumLibrary


*** Variables ***
${url}                      https://webfront-uat.yogamovement.com/

${close_alart}              //html/body/div/div/aside/div/div[2]/button
${register}                 //*[@id="header"]/div[2]/div/div/nav[1]/ul/li[1]/a
${singup_btn}               //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button
${male}                     //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[1]/label/div/div


${lastname}                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input

${country}                  //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div

${myanmar}                  //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]

${day}                      //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[3]/div[7]

${continue}                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button

${signin}                   //*[@id="header"]/div[2]/div/div/nav[1]/ul/li[2]/a

${signin_btn}               //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button

${class}                    //html/body/div/div/header/div[2]/div/div/nav[2]/ul/li[3]/a

${siginalert}               //html/body/div/div/aside/div/div[2]/button

${buy_aclass}               //html/body/div/div/header/div[2]/div/div/nav[2]/ul/li[3]/div/ul/li[2]/a

${all_access}               //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[2]/a

${all_access_class}        //html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[3]

${all_access_btn}          //html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[3]/div[4]/button

${order_next}              //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button

${choose_one}              //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/label/div/div/div/div[1]

${img}                     C:/Users/DELL/Pictures/flower1.jpg

${card_number}             //html/body/div/form/span[2]/div/div/div[2]/span/input

${card_exp_date}           //html/body/div/form/span[2]/div/span/input

${card_cvc}               //html/body/div/form/span[2]/div/span/input

${paynow}                //html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/button

*** Keywords ***
Register User
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
        Click Element       xpath://*[text()='Thailand']
        Sleep               3
        Click Element       ${country}
        Sleep               3
        Input Text         css:input[placeholder='Search']                 Myanmar
        Sleep               3
        Click Element       ${myanmar}
        Sleep               3

        Input Text          name:mobile                         977445533
        Sleep               3
        Click Element       id:dob
        Sleep               2
        Click Element       xpath://select[2]/option[@value='1997']
        Sleep               2
        Select From List By Value       xpath://select[2]       1997
        Sleep               2
        Select From List By Value       xpath://select[1]       6
        Sleep               5
        Click Element       ${day}
        Sleep               3
        Click Button        ${continue}

Singin
    Click Element                              ${signin}
    Sleep                                       3
    Input Text           name:email             aung10@yopmail.com
    Sleep                3
    Input Text           name:password          P@ssw0rd
    Sleep                 3
    Click Button         ${signin_btn}
    Sleep                 3
    Click Button         ${siginalert}
    Sleep                 3
    Click Element         ${class}
    Sleep                 3
    Click Element        ${buy_aclass}
    Sleep                 3
    Click Element         ${all_access}
    Sleep                 3
    Click Element         ${all_access_class}
    Sleep                 3
    Click Button          ${all_access_btn}
    Sleep                 3
    Click Button           ${order_next}
    Sleep                 3
    Click Element         ${choose_one}
    Sleep                 3
    Click Element         xpath://*[text()="East Coast"]
    Sleep                 3

    #Image
    Execute JavaScript   document.querySelector('input[type="file"]').classList.remove('d-none')
    Sleep                 3
    Choose File           xpath://input[@type='file']                         ${img}
    Sleep                 3

    #IFrame Payment
    Click Button          Change
    Sleep                 3

    Select Frame                        css:iframe[name^="__privateStripeFrame"][title="Secure card number input frame"]
    Sleep                  3

    Input Text            ${card_number}                        4111111111111111
    Unselect Frame

    Sleep                 3

    Select Frame                        css:iframe[name^="__privateStripeFrame"][title="Secure expiration date input frame"]
    Sleep                  3

    Input Text            ${card_exp_date}                        12/25
    Unselect Frame
    Sleep                 3

    Select Frame                        css:iframe[name^="__privateStripeFrame"][title="Secure CVC input frame"]
    Sleep                  3

    Input Text            ${card_cvc}                        123
    Unselect Frame
    Sleep                   3
    Click Button           ${paynow}
    Sleep                   5




*** Test Cases ***
Main
    Open Browser            ${url}              browser=Edge
    Maximize Browser Window
    Click Button         ${close_alart}
    #Register User
    Singin
    Sleep                   5
