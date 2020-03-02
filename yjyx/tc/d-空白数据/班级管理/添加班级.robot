*** Settings ***
Library   pylib.lib_class.ClassLib
Variables  cfg/cfg_spj1.py

*** Test Cases ***
添加班级1-tc000001
    ${class}     add_class  1    实验二班   50
    should be true   $class["retcode"]==0

    ${ret_1}    list_class  1
    ${ret_2}    evaluate   $ret_1["retlist"][0]
    should be true  $class["id"]==$ret_2["id"]
    should be true  $class["invitecode"]==$ret_2["invitecode"]
    should be true  $ret_2["name"]=='实验二班'
    should be true  $ret_2["studentlimit"]==50
    should be true  $ret_2["grade__name"]=='七年级'
    should be true  $ret_2["teacherlist"]==[]
    [Teardown]  delete_class  ${class["id"]}


