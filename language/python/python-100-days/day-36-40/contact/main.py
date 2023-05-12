"""
-- 创建名为address的数据库
create database address default charset utf8;

-- 切换到address数据库
use address;

-- 创建联系人表tb_contacter
create table tb_contacter
(
conid int auto_increment comment '编号',
conname varchar(31) not null comment '姓名',
contel varchar(15) default '' comment '电话',
conemail varchar(255) default'' comment '邮箱',
primary key (conid)
);
"""

import pymysql

INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail)
values (%s, %s, %s)
"""
DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s
where conid=%s
"""
SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class Contacter(object):
    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email


def input_contacter_info():
    name = input('姓名：')
    tel = input('手机号：')
    email = input('邮箱：')
    return name, tel, email


def add_new_contacter(con):
    name, tel, email = input_contacter_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_CONTACTER, (name, tel, email)) == 1:
                print('添加联系人成功！')
    except pymysql.MySQLError as err:
        print(err)
        print('添加联系人失败！')


def delete_contacter(con, contacter):
    try:
        with con.cursor() as cursor:
            if cursor.execute(DELETE_CONTACTER, (contacter.id,)) == 1:
                print('联系人已经删除！')
    except pymysql.MySQLError as err:
        print(err)
        print('删除联系人失败！')


def edit_contacter_info(con, contacter):
    name, tel, email = input_contacter_info()
    contacter.name = name or contacter.name
    contacter.tel = tel or contacter.tel
    contacter.email = email or contacter.email

    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_CONTACTER, (contacter.name, contacter.tel, contacter.email, contacter.id)) == 1:
                print('联系人信息已更新！')
    except pymysql.MySQLError as err:
        print(err)
        print('更新类型信息失败！')


def show_contacter_detail(con, contacter):
    print('姓名：', contacter.name)
    print('手机号：', contacter.tel)
    print('邮箱：', contacter.email)
    choice = input('是否编辑联系人信息？（yes|no）')
    if choice == 'yes' or choice == 'y':
        edit_contacter_info(con, contacter)
    else:
        choice = input('是否删除联系人信息？（yes|no）')
        if choice == 'yes' or choice == 'y':
            delete_contacter(con, contacter)


def show_search_result(con, cursor):
    contacters_list = []

    for index, row in enumerate(cursor.fetchall()):
        contacter = Contacter(**row)
        contacters_list.append(contacter)
        print('[%d]: %s' % (index, contacter.name))

    if len(contacters_list) > 0:
        choice = input('是否查看联系人详情？（yes|no）')

        if choice == 'yes' or choice == 'y':
            index = int(input('请输入编号：'))
            if 0 <= index < cursor.rowcount:
                show_contacter_detail(con, contacters_list[index])

def find_all_contacters(con):
    page,size=1,5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total=cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_CONTACTERS,(size,(page-1)*size))
                show_search_result(con,cursor)
                if page * size<total:
                    choice=input('继续查看下一页？（yes|no）')
                    if choice.lower()=='yes' or choice.lower()=='y':
                        page+=1
                    else:
                        break
                else:
                    print('没有下一页记录！')
                    break
    except pymysql.MySQLError as err:
        print(err)
