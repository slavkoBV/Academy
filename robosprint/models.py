from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class RoboSprintInfo(models.Model):
    class Meta:
        verbose_name = 'Про проект'
        verbose_name_plural = 'Про проект'

    title = models.TextField(
        verbose_name='Короткий опис проекту'
    )
    title_image = models.ImageField(
        upload_to='images',
        verbose_name='Титульний рисунок'
    )
    about = RichTextUploadingField(
        verbose_name='Про проект'
    )

    def __str__(self):
        return 'Інформація про проект'


class RoboSprintProject(models.Model):
    class Meta:
        verbose_name = 'Детальний опис'
        verbose_name_plural = 'Детальний опис'

    platform = RichTextUploadingField(
        verbose_name='Навчальна платформа'
    )
    model_requirements = RichTextUploadingField(
        verbose_name='Вимоги до моделі'
    )
    route_requirements = RichTextUploadingField(
        verbose_name='Вимоги до траси'
    )
    consulting = RichTextUploadingField(
        verbose_name='Консультації'
    )
    robocar_file = models.FileField(
        verbose_name='Бібліотека функцій керування',
        upload_to='files'
    )
    driver = models.FileField(
        verbose_name='Драйвер',
        upload_to='files'
    )

    def __str__(self):
        return 'Детальна інформація'


class Team(models.Model):
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команди'

    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to='teams'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Назва команди'
    )
    school = models.CharField(
        max_length=250,
        verbose_name='Навчальний заклад'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Населений пункт'
    )
    leader_fullname = models.CharField(
        max_length=200,
        verbose_name='Прізвище, ім\'я керівника'
    )
    leader_phone = models.CharField(
        max_length=15,
        verbose_name='Телефон керівника'
    )
    leader_email = models.EmailField(
        verbose_name='E-mail керівника'
    )
    captain = models.CharField(
        max_length=50,
        verbose_name='Капітан команди'
    )
    approved = models.BooleanField(
        verbose_name='Перевірено',
        default=False
    )

    @staticmethod
    def get_number_of_approved_teams():
        return len(Team.objects.filter(approved=True))

    def _get_number_of_team(self):
        try:
            teams = list(Team.objects.all())
            return teams.index(self)
        except ValueError:
            return 0

    def __str__(self):
        return ' '.join(['Команда №',
                         str(self._get_number_of_team() + 1),
                         self.title])


class Participant(models.Model):
    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Учасники'

    fullname = models.CharField(
        max_length=50,
        verbose_name='Учасник команди'
    )
    team = models.ForeignKey(
        Team,
        related_name='participants',
        verbose_name='Учасник'
    )

    def __str__(self):
        return self.fullname
