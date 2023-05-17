import io


class PostsWriter:
    """负责将帖子列表写入到文件
    """

    def __init__(self, fp: io.TextIOBase, title: str):
        self.fp = fp
        self.title = title

    def write(self, posts: List[Post]):
        self.fp.write(f'# {self.title}\n\n')
        # enumerate 接收第二个参数，表示从这个数开始计数（默认为 0）
        for i, post in enumerate(posts, 1):
            self.fp.write(f'> TOP {i}: {post.title}\n')
            self.fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
            self.fp.write(f'> 地址：{post.link}\n')
            self.fp.write('------\n')


class HNTopPostsSpider:
    FILE_TITLE = 'Top news on HN'

    def write_to_file(self, fp: io.TextIOBase):
        """以纯文本格式将 Top 内容写入文件

        实例化参数文件对象 fp 被挪到了 write_to_file 方法中
        """
        # 将文件写入逻辑托管给 PostsWriter 类处理
        writer = PostsWriter(fp, title=self.FILE_TITLE)
        writer.write(list(self.fetch()))
