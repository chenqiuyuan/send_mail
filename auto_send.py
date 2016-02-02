try:
    import shibor_csv_file
    import qq_mail
except ImportError:
    from mpython.send_mail import shibor_csv_file
    from mpython.send_mail import qq_mail

shibor_csv_file.file()
qq_mail.send('380133194@qq.com')
qq_mail.send('henry.duye@gmail.com')
qq_mail.send('ycbillows@qq.com')
