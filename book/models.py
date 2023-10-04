from django.db import models

# Create your models here.
"""
1. ORM
    表 --> 类
    字段 --> 属性

2. 模型类需要继承自models.Model

3. django会为表创建自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后django不会再创建自动增长的主键列。
   默认创建的主键列属性为id，可以使用pk代替，pk全拼为primary key。

4. 属性名=models.属性类型(选项)

    属性名: 不要使用 python,mysql关键字
            不要使用 连续的下划线(__)，否则会与查询语法冲突
    属性类型: 和mysql的类型类似的
    选项: charfiled 必须设置 max_length
            varchar(M)
          null   是否为空
          unique 唯一
          default 设置默认值
          verbose_name 主要是admin后台显示
"""


"""
书籍表:
    id,name,pub_date,readcount,commentcount,is_delete
"""
class BookInfo(models.Model):

    # 创建字段
    # 属性名=models.属性类型(选项)
    name=models.CharField(max_length=10,unique=True,verbose_name='名字')
    pub_date=models.DateField(null=True,verbose_name='发布日期')
    readcount=models.IntegerField(default=0,verbose_name='阅读量')
    commentcount=models.IntegerField(default=0,verbose_name='评论量')
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')


    class Meta:
        # 模型类如果未指明表名，Django默认以小写app应用名_小写模型类名为数据库表名。
        # 可通过db_table指明数据库表名。
        db_table='bookinfo' # 指定数据库表名
        verbose_name='书籍信息' # 在admin站点中显示的名称


    def __str__(self):
        """
        定义每个数据对象的显示信息，比如：
            - 查询到某条记录后，打印该条记录就会显示这里设定的值
            - 站点管理查看数据时，每条记录显示的内容
        """
        return self.name
    


"""
人物列表信息的模型类
"""
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 书籍、人物为 1:n 的关系，外键定义在多的一方
    # 在设置外键时，需要通过on_delete选项指明主表删除数据时，对于外键引用表数据如何处理
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name