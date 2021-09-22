from django.db import models
import datetime
from django.utils import timezone

# from abc import ABCMeta
# здесь мы создаем модели того, что будет в приложении
# конкретные элементы мы задаем полями в классах

class EmailSender(models.Model):
    '''
    This class will have fields for our EmailSender
    '''
    email_adress = models.EmailField()
    
    theme_of_message = models.CharField('Theme of message', max_length=100)
    
    message = models.TextField('Message')