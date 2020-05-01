from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=20)
    cover = models.TextField(verbose_name='文章封面')
    content = models.TextField(verbose_name='文章内容')
    markdown_content = models.TextField(verbose_name='文章内容（markdown）') # 保存markdown语法内容
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    read_times = models.IntegerField() # 阅读次数

    def __str__(self):
        return self.title