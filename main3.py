import io
import sys
from typing import Generator

import requests
from lxml import etree


class Post:

    def __init__(self, title: str, link: str, points: str, comments_cnt: str):
        self.title = title
        self.link = link
        self.points = int(points)
        self.comments_cnt = int(comments_cnt)


class HNTopPostsSpider:

    ITEMS_URL = 'https://news.ycombinator.com/'
    FILE_TITLE = 'Top news on HN'

    def __init__(self, fp: io.TextIOBase, limit: int = 5):
        self.fp = fp
        self.limit = limit

    def fetch(self) -> Generator[Post, None, None]:
        resp = requests.get(self.ITEMS_URL)

        html = etree.HTML(resp.text)
        items = html.xpath(
            '//table/tbody/tr[@class="athing"]')

        for item in items[:self.limit]:
            node_title = item.xpath(
                './td[@class="title"]/span[@class="titleline"]/a')[0]
            node_detail = item.getnext()
            points_text = node_detail.xpath('.//span[@class="score"]/text()')
            comments_text = node_detail.xpath('.//td/a[last()]/text()')[0]

            yield Post(
                title=node_title.text,
                link=node_title.get('href'),

                points=points_text[0].split()[0] if points_text else '0',
                comments_cnt=comments_text.split()[0]
            )

    def write_to_file(self):

        self.fp.write(f'# {self.FILE_TITLE}\n\n')

        for i, post in enumerate(self.fetch(), 1):
            self.fp.write(f'> TOP {i}: {post.title}\n')
            self.fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
            self.fp.write(f'> 地址：{post.link}\n')
            self.fp.write('------\n')


def main():

    # with open('/tmp/hn_top5.txt') as fp:
    #     crawler = HNTopPostsSpider(fp)
    #     crawler.write_to_file()

    # 因为 HNTopPostsSpider 接收任何 file-like 的对象，所以我们可以把 sys.stdout 传进去
    # 实现往控制台标准输出打印的功能
    crawler = HNTopPostsSpider(sys.stdout)
    crawler.write_to_file()


if __name__ == '__main__':
    main()
