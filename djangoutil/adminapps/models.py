from django.db import models

# Create your models here.

"""
Django Admin后台相关的模型类
"""


class Menu(models.Model):
    """
    菜单模型
    """
    menuName = models.CharField(verbose_name='菜单名字', max_length=20)
    menuUrl = models.CharField(verbose_name='菜单Url地址', max_length=50, null=True, blank=True, default='',
                               help_text='设置菜单Url跳转地址，没有则为空')
    menuPriority = models.IntegerField(verbose_name='菜单显示优先级', null=True, blank=True, default=-1,
                                       help_text='菜单显示优先级顺序，优先级越大显示越靠前')
    menuPermissionId = models.IntegerField(verbose_name='菜单权限Id', help_text='给菜单设置权限Id，用于菜单权限控制',
                                           error_messages={'field-menuPermissionId': '只能输入数字'})

    def __str__(self):
        return self.menuName

    class Meta:
        db_table = "adminapps_menu_info"
        verbose_name = "菜单"
        verbose_name_plural = verbose_name
        ordering = ["-menuPriority", "id"]

    objects = models.Manager()


class SubMenu(models.Model):
    """
    子菜单模型
    """
    subMenuName = models.CharField(verbose_name='子菜单名字', max_length=20)
    parentMenu = models.ForeignKey("Menu", verbose_name='父级菜单', null=True, blank=True,
                                      help_text='添加子菜单，请选择父级菜单', on_delete=models.SET_NULL)
    subMenuShow = models.BooleanField(verbose_name='是否显示', default=False, help_text='子菜单是否显示，默认添加不显示')
    subMenuUrl = models.CharField(verbose_name='子菜单Url地址', max_length=50, null=True, blank=True,
                                  default='javascript:void(0)',
                                  help_text='设置子菜单Url跳转地址')
    subMenuPriority = models.IntegerField(verbose_name='子菜单显示优先级', null=True, blank=True, default=-1,
                                          help_text='子菜单显示优先级顺序，优先级越大显示越靠前')
    subMenuPermissionId = models.IntegerField(verbose_name='子菜单权限Id', help_text='给子菜单设置权限Id，用于菜单权限控制',
                                              error_messages={'field-subMenuPermissionId': '只能输入数字'})

    def __str__(self):
        return self.subMenuName

    class Meta:
        db_table = "adminapps_submenu_info"
        verbose_name = "子菜单"
        verbose_name_plural = verbose_name
        ordering = ["-subMenuPriority", "id"]

    objects = models.Manager()
