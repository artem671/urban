def send_email(message, recipient, *, sender="university.help@gmail.com"):
    
    if "@" in recipient and "@" in sender:
        verif_recipient=recipient.split("@")[1]
        if "." in verif_recipient:
            verif_recipient=verif_recipient.split(".")[1]
            if verif_recipient!="com":
                if verif_recipient!="ru":
                    if verif_recipient!="net":
                        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                        return 0
                        
        verif_sender=sender.split("@")[1]
        if "." in verif_sender:
            verif_sender=verif_sender.split(".")[1]
            if verif_sender!="com":
                if verif_sender!="ru":
                    if verif_sender!="net":
                        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                        return 0
                        
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return 0
                
                
    if sender==recipient:
        print("Нельзя отправить письмо самому себе!")
        return 0
    
    if sender=="university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return 0
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return 0

   
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')   
