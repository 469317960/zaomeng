*** Settings ***
Library   pylib.lib_class.ClassLib
Suite Setup   add_class  1    1班   100
Suite Teardown  delete_class_byname   1班
