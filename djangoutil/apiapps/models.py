from django.db import models

# Create your models here.
from django.db import models


class FundInfo(models.Model):
    """
    基金信息
    """
    fundCode = models.CharField('基金代码', max_length=10, blank=True, null=True,
                                error_messages={'null': "不能为空", 'invalid': '格式错误'})
    fundName = models.CharField('基金名字', max_length=50)
    isMonitor = models.BooleanField('是否监控', default=True)

    class Meta:
        db_table = 'apiapps_fund_info'  # 自定义数据库表名
        verbose_name = '基金信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fundName

    objects = models.Manager()
