from django.contrib import admin
from adminapps.models import Menu, SubMenu


# Register your models here.

# 注册menu菜单模型


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # 菜单列表需要展示的字段
    list_display = ['menuName', 'menuUrl', 'menuPriority', 'menuPermissionId']
    # 设置哪些字段可以在编辑页面显示编辑
    fields = ['menuName', 'menuUrl', 'menuPriority', 'menuPermissionId']
    # 设置哪些列表字段点击后可以进入编辑
    list_display_links = ['menuName']
    # 菜单列表依据那个字段排序
    # ordering = ['menuPriority']
    # 设置列表可过滤筛选用的字段
    list_filter = ['menuName']


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    # 菜单列表需要展示的字段
    list_display = ['subMenuName', 'parentMenu', 'subMenuShow', 'subMenuUrl', 'subMenuPriority', 'subMenuPermissionId']
    # 设置哪些字段可以在编辑页面显示编辑
    fields = ['subMenuName', 'parentMenu', 'subMenuShow', 'subMenuUrl', 'subMenuPriority', 'subMenuPermissionId']
    # 设置哪些列表字段点击后可以进入编辑
    list_display_links = ['subMenuName']
    # 菜单列表依据那个字段排序
    # ordering = ['menuPriority']
    # 设置列表可过滤筛选用的字段
    list_filter = ['subMenuName', 'parentMenu']
