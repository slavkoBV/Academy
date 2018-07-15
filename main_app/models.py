from django.db import models


class Contact(models.Model):
    address = models.CharField(
        max_length=100,
        verbose_name='Адреса'
    )

    class Meta:
        verbose_name = 'Контактна інформація'
        verbose_name_plural = 'Контактна інформація'

    def __str__(self):
        return self.address[:20]


class PhoneNumber(models.Model):
    provider = models.ImageField(
        blank=True,
        null=True,
        upload_to='contacts/',
        verbose_name='Логотип оператора'
    )
    number = models.CharField(
        max_length=13,
        verbose_name='Номер телефону'
    )
    contact = models.ForeignKey(
        Contact,
        related_name='phones',
        verbose_name='Номери телефонів'
    )

    class Meta:
        verbose_name = 'Номер телефону'
        verbose_name_plural = 'Номери телефонів'

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.EmailField(
        verbose_name='Електронна пошта'
    )
    contact = models.ForeignKey(
        Contact,
        related_name='emails',
        verbose_name='Електронні адреси'
    )

    class Meta:
        verbose_name = 'Електронна пошта'
        verbose_name_plural = 'Електронні адреси'

    def __str__(self):
        return self.email
