from django.db import models
from django.utils.translation import ugettext_lazy as _


class NewestLogFileContent(models.Model):
    '''
    Моедль создана для логирования ошибок приложения
    '''
    log_filename = models.CharField(max_length=200, verbose_name=_('название файла логера'))
    content = models.TextField(verbose_name=_('Запись файла'), null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.log_filename

    class Meta:
        verbose_name = _('Последние записи логов по файлам')
        verbose_name_plural = _('Последние записи логов по файлам')
