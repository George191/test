from email.mime.text import MIMEText
from subprocess import Popen, PIPE


def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


sender = 'robot@mimvp.com'
recevier = '674896488@qq.com'
subject = 'sendmail-subject'
html_content = 'hello mimvp.com'
send_mail(sender, recevier, subject, html_content)

# from PIL import Image
#
# img = Image.open(r"C:\Users\W9000210.ADC\Downloads\229_灰色商务网站模板\images\logo2.png")
#
# for i in range(4411):
#     for j in range(2136):
#         try:
#             r, g, b, alpha = img.getpixel((i, j))
#             if r == 58 and g == 58 and b == 58:
#                 r = 200
#                 g = 200
#                 b = 200
#                 img.putpixel((i, j), (r, g, b, alpha))
#         except Exception as e:
#             continue
# img.save('logo2.png')
