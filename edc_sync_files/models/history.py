from django.db import models
from django.utils import timezone

from edc_base.model.models import BaseUuidModel


class HistoryManager(models.Manager):
    def get_by_natural_key(self, filename, sent_datetime):
        return self.get(filename=filename, sent_datetime=sent_datetime)


class History(BaseUuidModel):

    filename = models.CharField(
        max_length=100,
        unique=True)

    hostname = models.CharField(
        max_length=100
    )

    sent_datetime = models.DateTimeField(default=timezone.now)

    acknowledged = models.BooleanField(
        default=False,
        blank=True,
    )

    ack_datetime = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True)

    ack_user = models.CharField(
        max_length=50,
        null=True,
        blank=True)

    objects = HistoryManager()

    def __str__(self):
        return '</{}.{}>'.format(self.filename, self.hostname)

    def natural_key(self):
        return (self.filename, self.hostname)

    class Meta:
        app_label = 'edc_sync_files'
        ordering = ('-sent_datetime', )
        verbose_name = 'Sent History'
        verbose_name_plural = 'Sent History'
        unique_together = (('filename', 'hostname'),)