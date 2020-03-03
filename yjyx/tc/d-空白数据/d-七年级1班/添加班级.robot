*** Settings ***
Library   pylib.lib_class.ClassLib
Variables  cfg/cfg_spj1.py

*** Test Cases ***
添加班级2-tc000002
    ${class}     add_class  1    2班   50
    should be true   $class["retcode"]==0
    ${ret_1}    list_class  1
    ${ret_2}    evaluate   $ret_1["retlist"]
    should be true    {"name": "2班","grade__name": "七年级","invitecode":$class["invitecode"],"studentlimit": 50,"studentnumber": 0,"id": $class["id"],"teacherlist": []} in $ret2
    [Teardown]  delete_class  ${class["id"]}


添加班级3-tc000003
    ${before}    list_class  1
    ${class}     add_class  1    1班   100
    ${after}    list_class  1
    should be true   $class["retcode"]==1
    should be true   $class["reason"]=="duplicated class name"
    ${ret_1}    list_class  1
    ${ret_2}    evaluate   $ret_1["retlist"]
    should be true     $before==   $after
