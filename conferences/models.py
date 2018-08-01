import datetime
import os.path

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from utils.slugify import slugify

section_CHOICES = (
    ('Природничі науки', 'Природничі науки'),
    ('Інформаційні технології', 'Інформаційні технології'),
    ('Механічна інженерія', 'Механічна інженерія'),
    ('Електрична інженерія', 'Електрична інженерія'),
    ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'),
    ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'),
    ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'),
    ('Виробництво та технології', 'Виробництво та технології'),
    ('Архітектура та будівництв о', 'Архітектура та будівництво'),
    ('Цивільна безпека', 'Цивільна безпека'),
    ('Транспорт', 'Транспорт'),
)


def get_upload_path(instance, filename):
    if isinstance(instance, Conference):
        print(os.path.join(
                'docs/{0}-{1}/{2}'.format(instance.get_number_of_conference(), instance.slug, filename)))
        return os.path.join(
                'docs/{0}-{1}/{2}'.format(instance.get_number_of_conference(), instance.slug, filename))
    elif isinstance(instance, Thesis):
        return os.path.join(
            'theses/{0}-{1}/{2}'.format(instance.conference.get_number_of_conference(), instance.conference.slug,
                                          filename))


class Conference(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Тема конференції'
    )
    title_eng = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Тема конференції_англ.'
    )
    slug = models.SlugField(blank=True, editable=False)
    level = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        verbose_name='Рівень конференції'
    )
    date_start = models.DateField(
        verbose_name='Дата початку конференції',
        default=datetime.date.today
    )
    date_end = models.DateField(
        verbose_name='Дата завершення конференції',
        default=datetime.date.today
    )
    place = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name='Місце проведення'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Статус конференції (проведена/непроведена)'
    )
    information_message = models.FileField(
        upload_to=get_upload_path,
        blank=True,
        null=True,
        verbose_name='Інформаційне повідомлення'
    )
    thesis_file = models.FileField(
        upload_to=get_upload_path,
        blank=True,
        null=True,
        verbose_name='Збірка доповідей'
    )

    def get_number_of_participants(self):
        participants = self.participant_set.all()
        return ''.join(str(len(participants)))

    get_number_of_participants.short_description = 'Кількість учасників'

    def get_number_of_thesises(self):
        thesises = self.thesis_set.all()
        return ''.join(str(len(thesises)))

    class Meta:
        verbose_name = 'Конференція'
        verbose_name_plural = 'Конференції'
        ordering = ('-date_start',)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('conference:conference_detail', args=[self.id, self.slug])

    def get_number_of_conference(self):
        try:
            conferences = sorted(list(Conference.objects.all()), key=lambda x: x.date_start)
            return conferences.index(self) + 1
        except ValueError:
            return None

    def __str__(self):
        return str(self.get_number_of_conference()) + ' ' + str(self.title)


# Participant Model ###########################################
class UserProfile(models.Model):
    academic_status_CHOICES = (
        ('Доц.', 'Доцент'),
        ('Проф.', 'Професор'),
        ('Ст. наук. співробітник', 'Старший науковий співробітник')
    )
    degree_CHOICES = (
        ('к.н.', 'кандидат наук'),
        ('д.н.', 'доктор наук'),
        ('Ph.D', 'доктор філософії'),
    )
    lastname = models.CharField(
        max_length=30,
        verbose_name='Прізвище'
    )
    firstname = models.CharField(
        max_length=30,
        verbose_name='Ім\'я'
    )
    middlename = models.CharField(
        max_length=30,
        default='--',
        verbose_name='По-батькові'
    )
    academic_status = models.CharField(
        max_length=30,
        choices=academic_status_CHOICES,
        default=None,
        null=True,
        blank=True,
        verbose_name='Вчене звання'
    )
    degree = models.CharField(
        max_length=30,
        choices=degree_CHOICES,
        default=None,
        null=True,
        blank=True,
        verbose_name='Науковий ступінь'
    )
    job_position = models.CharField(
        max_length=70,
        verbose_name='Посада'
    )
    organisation = models.CharField(
        max_length=90,
        verbose_name='Організація'
    )
    country = models.CharField(
        max_length=50,
        verbose_name='Країна'
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Місто'
    )
    phone = models.CharField(
        max_length=13,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        verbose_name='Електронна пошта'
    )
    filling_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата заповнення'
    )

    def conferences(self):
        conferences = [participant.conference for participant in self.participant_set.all()]
        return ', '.join(conference.__str__() for conference in conferences)

    conferences.short_description = 'Конференції'

    def get_number_of_conferences(self):
        conferences = [participant.conference for participant in self.participant_set.all()]
        return str(len(conferences))

    get_number_of_conferences.short_description = 'Кількість конференцій'

    class Meta:
        verbose_name_plural = 'Профілі учасників'
        verbose_name = 'Профіль учасника'
        unique_together = ('lastname', 'firstname', 'middlename')

    def __str__(self):
        return self.lastname + ' ' + self.firstname


class Participant(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='Профіль учасника')
    conference = models.ForeignKey(Conference, verbose_name='Конференція')

    def __str__(self):
        return str(self.user)

    def get_sections(self):
        sections_list = self.sections.get_queryset()
        return ', '.join([section.title for section in sections_list])

    get_sections.short_description = 'Секції'

    class Meta:
        ordering = ('user',)
        verbose_name = 'Учасник'
        verbose_name_plural = 'Учасники'
        unique_together = (('conference', 'user'),)


class Section(models.Model):
    title = models.CharField(
        max_length=100,
        choices=section_CHOICES,
        null=False,
        blank=False,
        verbose_name='Назва секції'
    )
    participant = models.ForeignKey(Participant, verbose_name='Учасник', related_name='sections')

    class Meta:
        verbose_name = 'Секція'
        verbose_name_plural = 'Секції'
        unique_together = (('title', 'participant'),)

    def __str__(self):
        return self.title


# Thesis Model ############################################
class Thesis(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Назва доповіді'
    )
    section = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=section_CHOICES,
        verbose_name='Назва секції'
    )
    thesis = models.FileField(
        upload_to=get_upload_path,
        verbose_name='Файл доповіді'
    )
    conference = models.ForeignKey(
        Conference,
        verbose_name='Конференція'
    )

    def get_authors(self):
        authors_list = self.author_set.get_queryset()
        return ', '.join(
            [author.participant.user.lastname + ' ' + author.participant.user.firstname
             for author in authors_list])

    get_authors.short_description = 'Автори'

    class Meta:
        verbose_name_plural = 'Доповіді'
        verbose_name = 'Доповідь'
        unique_together = (('title', 'conference'),)

    def __str__(self):
        return self.title


class Author(models.Model):
    participant = models.ForeignKey(Participant, verbose_name='Учасник конференції')
    thesis = models.ForeignKey(Thesis, verbose_name='Доповідь')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'

    def clean(self, *args, **kwargs):
        """Validate author by sections: if participant didn't register to thesis.section
            he can't be an author of this thesis
        """
        if self.thesis.section not in [section.title for section in self.participant.sections.all()]:
            raise ValidationError('Автори повинні бути зареєстровані в секції на яку \
                                   подається доповідь')
        super(Author, self).clean()

    def __str__(self):
        return self.participant.user.lastname
