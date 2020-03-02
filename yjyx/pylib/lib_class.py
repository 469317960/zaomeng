import requests
from cfg.cfg_spj1 import VCODE
from cfg.cfg_spj1 import URL
from pprint import pprint

class ClassLib:
    def __init__(self):
        self.vcode = VCODE

    def add_class(self,grade,name,studentlimit):
        payload={
            'vcode': self.vcode,
            'action': 'add',
            'grade': grade,
            'name': name,
            'studentlimit': studentlimit
        }
        response = requests.post(URL,data=payload)
        body_dict = response.json()
        pprint(body_dict)
        return body_dict

    def modify_class(self,classid,name,studentlimit):
        payload={
            'vcode': VCODE,
            'action': 'modify',
            'name':name,
            'studentlimit':studentlimit
        }
        new_url=f'{URL}/{classid}'
        response = requests.put(new_url,data=payload)
        body_dict = response.json()
        pprint(body_dict)
        return body_dict

    def delete_class(self,classid):
        payload={
            'vcode':self.vcode,
        }
        new_url = f'{URL}/{classid}'
        response= requests.delete(new_url,data=payload)
        body_dict = response.json()
        return body_dict
    # 涉及后面继续调用，不打印回来

    def delete_class_byname(self,name):
        #先列出课程
        tmp = self.list_class()
        for one in tmp["retlist"]:
            if one['name'] == name:
                classid=one['id']
                self.delete_class(classid)
                break

            #再次列出课程,判断
        name_list=[]
        tmp = self.list_class()
        for one in tmp["retlist"]:
            name_list.append(one['name'])
        if name not in name_list:
            pass
        else:
            raise Exception("cannot delete school classes!!")


    def delete_all_class(self):
        #先列出课程
        tmp = self.list_class()
        for one in tmp["retlist"]:
            classid=one['id']
            self.delete_class(classid)

        #再次列出课程
        tmp = self.list_class()
        if tmp["retlist"] != []:
            raise Exception("cannot delete all school classes!!")


    def list_class(self,gradeid=None):
        if gradeid != None:
            payload = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
                'gradeid': int(gradeid)
            }
        else:
            payload = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
            }
        response = requests.get(URL,params=payload)

        # 把json数据转化为python格式的数据
        body_dict=response.json()
        pprint(body_dict)
        return body_dict



if __name__ == '__main__':

    a = ClassLib()
    print('-----------------------------------------')
    a.add_class('2', '实验二班', '90')
    print('-----------------------------------------')
    b = a.list_class()
    print('-----------------------------------------')
    a.delete_class_byname('实验二班')
    print('-----------------------------------------')
    b=a.list_class()
    # print('-----------------------------------------')
    # classid = b["retlist"][0]['id']
    # a.modify_class(classid,'实验修改班','100')
    # print('-----------------------'
    #       '------------------')
    # # a.delete_class('244716')
    # a.list_class()
    # print('-----------------------------------------')
    # a.delete_all_class()
    # print('-----------------------------------------')







