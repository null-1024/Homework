'''
在线商城管理系统
1、用户登录
    1.1 商品浏览(所有和单独查询)
    1.2 商品的购买(加上一个时间)
    1.3 用户订单查询

2、管理员登录
    2.1 商品添加
    2.2 商品的查询
    2.3 商品的删除
    2.4 商品的修改
    2.5 可以查询订单    
最后退出
'''

import os
import json
import datetime

def main():
    # 1. 初始化配置
    init()

    # 2. 功能 : 增删改查
    user_or_manger=int(input("管理员登录(输入0)/用户登录(输入1):"))
    if user_or_manger in (0,1):
        if user_or_manger == 0:
            manger()
        elif user_or_manger == 1:
            user()
    else:
        print("login error")
    
    # 3. 如果数据改动, 更新数据
    global shop_is_change,orders_is_change
    if shop_is_change:
        with open(shops_file,"w",encoding="utf-8") as file:
            json.dump(shops_data, file,ensure_ascii=False,indent='\t')
    if orders_is_change:
        with open(orders_file,"w",encoding="utf-8") as file:
            json.dump(orders_data, file,ensure_ascii=False,indent='\t')

# 初始化配置 : 文件路径, 载入数据, 是否修改
def init():
    # 文件路径
    global shops_file,orders_file
    shops_file="shop.json"
    orders_file="orders.json"

    # 载入数据(字典)
    global shops_data,orders_data
    shops_data={}
    orders_data={}
    if not os.path.exists(shops_file):# 如果没有文件, 则创建
        print("shops_data file is not exist")
        with open(shops_file,"w",encoding="utf-8") as file :
            pass
    try:# 载入数据
        with open(shops_file,"rt",encoding="utf-8") as file :
            shops_data=json.load(file)
    except json.decoder.JSONDecodeError:
        shops_data={}
        print('shops_data is empty!')
    
    if not os.path.exists(orders_file):# 如果没有文件, 则创建
        print("orders_data file is not exist")
        with open(orders_file,"w",encoding="utf-8") as file :
            pass
    try:# 载入数据
        with open(orders_file,"rt",encoding="utf-8") as file :
            orders_data=json.load(file)
    except json.decoder.JSONDecodeError:
        orders_data={}
        print('orders_data is empty!')

    # 用变量记录是否修改数据, 如果没有修改, 退出前则不需重新写入
    global shop_is_change,orders_is_change
    shop_is_change=False
    orders_is_change=False

def manger():
    global shop_is_change
    while True:
        choice=int(input("0. exit\n1. 商品添加\n2. 商品查询\n3. 商品删除\n4. 商品修改\n5. 查询订单\n"))

        if choice in range(0,6):
            if choice==0:
                ensure=input("是否exit? Y/N\n")
                if ensure in ("Y","y"):
                    break
                else:
                    continue
            elif choice==1:
                change()
                shop_is_change=True
            elif choice==2:
                shop_search()
            elif choice==3:
                delete()
                shop_is_change=True
            elif choice==4:
                change()
                shop_is_change=True
            elif choice==5:
                orders_search()
        else :
            print("function error")

def change():
    while True:
        id=input("please input the id of shop : ")# 商品id (唯一标识)
        if not id:
            break
        name=input("please input the name of shop : ")# 商品名称 (可以重名)
        if not name:
            break

        try:
            price=int(input("please input the price of shop : "))
            num=int(input("please input the number of shop : "))
        except (TypeError,ValueError) : 
            print("input error")
            continue

        shops_data[id]={"name" : name,"price" : price,"number" : num}
        ensure=input("是否continue? Y/N\n")
        if ensure in ("Y","y"):
            continue
        else:
            break

def shop_search():
    while True:
        id=input("please input the id of shop : ")# 根据id查找
        if not id:
            break

        try:
            print(shops_data[id])
        except KeyError:
            print("no find")
        ensure=input("是否continue? Y/N\n")
        if ensure in ("Y","y"):
            continue
        else:
            break

def delete():
    while True:
        id=input("please input the id of shop : ")
        if not id:
            break

        try:
            del shops_data[id]
        except KeyError : 
            print("no find")
        ensure=input("是否continue? Y/N\n")
        if ensure in ("Y","y"):
            continue
        else:
            break

def orders_search():
    print(orders_data)

def user():
    global shop_is_change,orders_is_change
    while True:
        choice=int(input("0. exit\n1. 商品浏览\n2. 商品购买\n3. 订单查询\n"))

        if choice in range(0,4):
            if choice==0:
                ensure=input("是否exit? Y/N\n")
                if ensure in ("Y","y"):
                    break
                else:
                    continue
            elif choice==1:
                print(shops_data)
            elif choice==2:
                buy()
                shop_is_change=True
                orders_is_change=True
            elif choice==3:
                orders_search()
        else :
            print("function error")

def buy():
    while True:
        id=input("please input the id of shop : ")
        if not id:
            break

        try:
            buy_num=int(input("please input the number of buy : "))
        except TypeError / ValueError : 
            print("input error")
            continue
        
        if shops_data[id]["number"] < buy_num:
            print("数量不足")
            continue

        shops_data[id]["number"]=shops_data[id]["number"]-buy_num
        orders_data[len(orders_data)+1]={"id" : id,"number" : buy_num,"time":str(datetime.datetime.now())}

        ensure=input("是否continue? Y/N\n")
        if ensure in ("Y","y"):
            continue
        else:
            break

if __name__ =='__main__':
    main()