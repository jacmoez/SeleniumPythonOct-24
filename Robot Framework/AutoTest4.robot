*** Settings ***
Library                 SeleniumLibrary


*** Variables ***
${url}                                   https://testautomationpractice.blogspot.com/
${mobile}                                //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[6]/div[1]/div/div/a[1]
${laptop}                               //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[6]/div[1]/div/div/a[2]

${copy_text}                           //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[7]/div[1]/button


*** Keywords ***
Mouse Hover
    Click Button                        class:dropbtn
    Sleep                               4
    Click Element                       ${mobile}
    Sleep                               4
    Click Button                        class:dropbtn
    Sleep                               4
    Click Element                       ${laptop}
    Sleep                               4
    Input Text                          id:field1               QA Testing
    Sleep                               4
    Double Click Element                ${copy_text}
    Sleep                               4
    ${text}=                            Get Value               id:field2
    Log                                 ${text}
    Drag and Drop                       id:draggable            id:droppable
    Sleep                               4
    #Slider
    Scroll Element Into View            //*[@id="slider-range"]/span[1]
    Drag And Drop By Offset             //*[@id="slider-range"]/span[1]       -75          0
    Sleep                               4
    Drag And Drop By Offset             //*[@id="slider-range"]/span[2]       -300         0
    Sleep                               4
    Input Text                          id:comboBox                         Item 10
    Sleep                               2
    Click Element                       id:apple
    Sleep                               2
    Execute JavaScript                  window.history.back()
    Sleep                               2
    Click Element                       id:lenovo
    Sleep                               2
    Execute JavaScript                  window.history.back()
    Sleep                               2
    Click Element                       id:dell
    Sleep                               2
    Execute JavaScript                  window.history.back()
    Sleep                               2
    FOR         ${i}                    IN RANGE                1               8
                Click Element           //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[12]/div[1]/div/div[3]/a[${i}]
                Sleep                   2
                ${title}=               Get Title
                Log                     ${title}
                Execute JavaScript      window.history.back()
                Sleep                   4
    END
Form
    ${elements}                     Create List                     QA      Tester        Developer
    FOR         ${i}                IN RANGE                         0        3
                ${count}=           Evaluate                         ${i} + 1
                Input Text          id:input${count}                  ${elements}[${i}]
                Sleep               3
                Click Button        id:btn${count}
                Sleep               3
    END



*** Test Cases ***
Main
    Open Browser        ${url}              browser=Chrome
    Maximize Browser Window
    Mouse Hover
    Form
