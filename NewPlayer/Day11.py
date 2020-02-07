import json

import requests


def main1():
    f = None
    try:
        f = open('1', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def main2():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    # dump - 将Python对象按照JSON格式序列化到文件中
    # dumps - 将Python对象处理成JSON格式的字符串
    # load - 将文件中的JSON数据反序列化成对象
    # loads - 将字符串的内容反序列化成Python对象
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


def main3():
    try:
        resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
        data_model = json.loads(resp.text)
        print(data_model)
        # error
        for news in data_model:
            print(news['title'])
    except:
        pass


if __name__ == '__main__':
    main1()
    main2()
    main3()
