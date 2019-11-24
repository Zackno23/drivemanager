# gmailを使ったメール送信のサンプルプログラム
# 実装のときはファイルのパスを調整する。


from smtplib import SMTP
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def sendGmailAttach(sub,body):
    sender, password = "chikara.f.yoshida@gmail.com", "Zackno213" # 送信元メールアドレスとgmailへのログイン情報
    to = 'chikara.f.yoshida@gmail.com'  # 送信先メールアドレス
    sub = sub #メール件名
    body = body  # メール本文
    host, port = 'smtp.gmail.com', 587

    # メールヘッダー
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = to

    # メール本文
    body = MIMEText(body)
    msg.attach(body)

    # 添付ファイルの設定
    attach_file = {'name': '運行管理表.xlsx', 'path': './運行管理表.xlsx'} # nameは添付ファイル名。pathは添付ファイルの位置を指定
    attachment = MIMEBase('application', 'octet-stream')
    file = open(attach_file['path'], 'rb+')
    attachment.set_payload(file.read())
    file.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
    msg.attach(attachment)

    # gmailへ接続(SMTPサーバーとして使用)z
    gmail=SMTP("smtp.gmail.com", 587)
    gmail.starttls() # SMTP通信のコマンドを暗号化し、サーバーアクセスの認証を通す
    gmail.login(sender, password)
    gmail.send_message(msg)


