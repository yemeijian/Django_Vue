from django.test import TestCase

# Create your tests here.

import json
import re
import requests

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from apscheduler.schedulers.blocking import BlockingScheduler

# import logging
respose = requests.get("http://localhost:8000/api/fundinfo/")
print(respose.json())
#
#
# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.INFO)
#
#
# def getNetWorthIncrement():
#     """
#     获取每天的估算净值增量
#     :return:
#     """
#     # 通过基金编码获取估值
#     codeList = ['260108', '003095', '003096', '110011', '161028', '002190']
#     for code in codeList:
#         url = 'http://fundgz.1234567.com.cn/js/%s.js' % code
#         result = requests.get(url)  # 发送请求
#         data = json.loads(re.match(".*?({.*}).*", result.text, re.S).group(1))
#         # 基金详情 邮件内容
#         sendContent = '========基金详情========' + '\n' + '基金编码：%s' % data['fundcode'] + '\n' + '基金名称：%s' % data[
#             'name'] + '\n' + '净值日期：%s' % data['jzrq'] + '\n' + '单位净值：%s' % data['dwjz'] + '\n' + '估值时间：%s' % data[
#                           'gztime'] + '\n' + '估算净值：%s' % data['gsz'] + '\n' + '估算增量：%s%%' % data['gszzl'] + "\n"
#         # 如果估算净值增量小于0，则为跌，发送邮件通知
#         if int(str(data['gszzl']).split(".")[0]) <= 0 and str(data['gszzl']).split(".")[0][0] == "-":
#             # 调用发送邮件方法
#             sendMail(sendContent)
#             logging.info("时间：%s估值净值增量为跌！" % data['gztime'])
#         else:
#             logging.info("估算净值增量大于0，为涨！")
#         logging.info(sendContent)
#
#
# def sendMail(sendContent):
#     # 第三方 SMTP 服务
#     mail_host = "smtp.qq.com"  # 设置服务器
#     mail_user = "2447519717@qq.com"  # 用户名
#     mail_pass = "dgfxkcwccjfrebha"  # 口令
#
#     sender = mail_user
#     receivers = ['205007724@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
#     message = MIMEText(sendContent, 'plain', 'utf-8')
#     message['From'] = Header("某小健", 'utf-8')
#     message['To'] = Header("某某某", 'utf-8')
#
#     subject = '基金涨跌估算净值提醒'
#     message['Subject'] = Header(subject, 'utf-8')
#
#     try:
#         smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 465/25 为 SMTP 端口号
#         smtpObj.login(mail_user, mail_pass)
#         smtpObj.sendmail(sender, receivers, message.as_string())
#         logging.info("已成功发送邮件通知！")
#     except smtplib.SMTPException:
#         logging.error("Error: 无法发送邮件")
#
#
# scheduler = BlockingScheduler()
# # 在每天14点30分，运行一次
# scheduler.add_job(getNetWorthIncrement, 'cron', hour='21', minute='10', id="crontest")
# scheduler.start()
# # search = '景顺长城新兴成长混合'
# # url = 'http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx?m=1&key=' + search  #
# #
# # result = requests.post(url)  # 发送请求
# # print('##############查询结果##############')
# # print(result.json())  # 返回数据