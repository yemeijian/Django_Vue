# Generated by Django 3.1.6 on 2021-02-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuName', models.CharField(max_length=20, verbose_name='菜单名字')),
                ('menuUrl', models.CharField(blank=True, default='', help_text='设置菜单Url跳转地址，没有则为空', max_length=50, null=True, verbose_name='菜单Url地址')),
                ('menuPriority', models.IntegerField(blank=True, default=-1, help_text='菜单显示优先级顺序，优先级越大显示越靠前', null=True, verbose_name='菜单显示优先级')),
                ('menuPermissionId', models.IntegerField(error_messages={'field-subMenuPermissionId': '只能输入数字'}, help_text='给菜单设置权限Id，用于菜单权限控制', verbose_name='菜单权限Id')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'db_table': 'adminapps_menu_info',
                'ordering': ['-menuPriority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subMenuName', models.CharField(max_length=20, verbose_name='菜单名字')),
                ('subMenuShow', models.BooleanField(default=False, help_text='菜单是否显示，默认添加不显示', verbose_name='是否显示')),
                ('subMenuUrl', models.CharField(blank=True, default='javascript:void(0)', help_text='设置菜单Url跳转地址', max_length=50, null=True, verbose_name='菜单Url地址')),
                ('subMenuPriority', models.IntegerField(blank=True, default=-1, help_text='菜单显示优先级顺序，优先级越大显示越靠前', null=True, verbose_name='菜单显示优先级')),
                ('subMenuPermissionId', models.IntegerField(error_messages={'field-subMenuPermissionId': '只能输入数字'}, help_text='给菜单设置权限Id，用于菜单权限控制', verbose_name='菜单权限Id')),
                ('parentMenu', models.ForeignKey(blank=True, help_text='添加子菜单，请选择父级菜单', null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapps.menu', verbose_name='父级菜单')),
            ],
            options={
                'verbose_name': '子菜单',
                'verbose_name_plural': '子菜单',
                'db_table': 'adminapps_submenu_info',
                'ordering': ['-subMenuPriority', 'id'],
            },
        ),
        migrations.DeleteModel(
            name='Menus',
        ),
    ]
