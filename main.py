# -*- coding: utf-8 -*-
import requests
import re


def save_website_title(url, filename):
    """获取某个地址的网页标题，然后将其写入到文件中

    :returns: 如果成功保存，返回 True，否则打印错误，返回 False
    """
    try:
        resp = requests.get(url)
        obj = re.search(r'<title>(.*)</title>', resp.text)
        if not obj:
            print('save failed: title tag not found in page content')
            return False

        title = obj.grop(1)
        with open(filename, 'w') as fp:
            fp.write(title)
            return True
    except Exception:
        print(f'save failed: unable to save title of {url} to {filename}')
        return False


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')


if __name__ == '__main__':
    main()
