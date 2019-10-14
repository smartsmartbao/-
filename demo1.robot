# demo1.robot

*** Settings ***
Library    AppiumLibrary
Library    DebugLibrary

*** Variables ***
# Device Specific
${PLATFORM}         Android
${VERSION}          6.0.1
${DEVICENAME}       26c51f68

# App Specific
${PACKAGE}          com.kpmg.tax.prc.iit.employee.app
${ACTIVITY}         com.kpmg.tax.prc.iit.employee.app.MainActivity

*** Test Cases ***
open_app
    Open Application    http://localhost:4723/wd/hub    newCommandTimeout=30000    platformName=${PLATFORM}    platformVersion=${VERSION}    deviceName=${DEVICENAME}    appPackage=${PACKAGE}    appActivity=${ACTIVITY}
    Wait Until Page Contains Element    xpath=//android.widget.Button[@content-desc="测试连接 "]
    Click Element    xpath=//android.widget.Button[@content-desc="测试连接 "]