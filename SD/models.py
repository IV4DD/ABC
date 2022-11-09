from django.db import models
from django.urls import reverse
from django.utils import timezone


DEPARTMENTS = [
    ('DD¹', 'DD¹'),
    ('DD²', 'DD²'),
    ('DD³', 'DD³'),
    ('DD⁴', 'DD⁴'),
    ('DD⁵', 'DD⁵'),
    ('SD', 'SD'),
    ('Marketing Team', 'Marketing Team'),
    ('Call Center', 'Call Center'),
    ('DT', 'DT'),
    ('DM', 'DM'),
    ('Снабжение', 'Снабжение'),
    ('Офис', 'Офис'),
    ('Другое...', 'Другое...'),
]

STATUSES = [
    ('На рассмотрении', 'На рассмотрении'),
    ('Утвержден', 'Утвержден'),
    ('Отклонен', 'Отклонен'),
]

TYPES_OF_SALARY = [
    ('Оклад', 'Оклад'),
    ('Процент', 'Процент'),
]

# POSITIONS = [
#     ('Врач', 'Врач'),
#     ('Ассистент врача', 'Ассистент врача'),
#     ('Администратор', 'Администратор'),
#     ('Оператор', 'Оператор'),
#     ('Медсестра', 'Медсестра'),
#     ('ММП', 'ММП'),
#     ('Сотрудник отдела маркетинга', 'Сотрудник отдела маркетинга'),
#     ('Бухгалтер', 'Бухгалтер'),
# ]



class Coworker(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    middle_name = models.CharField(max_length=20, verbose_name="Отчество")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    phone = models.CharField(max_length=15, unique=True, verbose_name="Номер сотового")
    department = models.CharField(max_length=30, verbose_name="Филиал/Отдел", choices=DEPARTMENTS, default='SD', null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, verbose_name="E-mail")
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Дата рождения")
    comment = models.TextField(max_length=300, blank=True, null=True, verbose_name="Дополнительная информация")
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True, verbose_name="Фото", upload_to="photos_coworkers")
    status = models.CharField(max_length=30, verbose_name="Статус", choices=STATUSES, default='На рассмотрении', null=True, blank=True)
    type_of_salary = models.CharField(max_length=20, verbose_name="Тип зароботной платы", choices=TYPES_OF_SALARY, default='Оклад', null=True, blank=True)
    salary = models.CharField(max_length=20, verbose_name="Оплата за смену", null=True, blank=True)
    position = models.CharField(max_length=50, verbose_name="Позиция", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["-date_created"]

    # Capitalization of Input
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.surname = self.surname.capitalize()
        self.email = self.email.lower()

    def get_absolute_url(self):
        return reverse('coworker_detail', args=[str(self.id)])
    def FIO(self):
        return self.surname + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'
    def __str__(self):
        return self.surname + ' ' + self.first_name + ' ' + self.middle_name

class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя пациента")
    surname = models.CharField(max_length=30, verbose_name="Фамилия пациента")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество пациента")

    phone = models.CharField(max_length=30, verbose_name="Номер сотового", unique=True)
    iin = models.CharField(max_length=30, verbose_name="ИИН", unique=True)

    gender = models.CharField(max_length=1, verbose_name="Пол пациента", blank=True, null=True)
    age = models.CharField(max_length=7, verbose_name="Возраст пациента", blank=True, null=True)

    note = models.TextField(max_length=500, blank=True, null=True, verbose_name="Необязательный комментарий")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения", editable=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Patient, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
        ordering = ["-date_created"]

    # Capitalization of Input
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.surname = self.surname.capitalize()

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.surname

class Doctor(models.Model):
    surname = models.CharField(max_length=60, verbose_name="Фамилия врача")
    first_name = models.CharField(max_length=60, verbose_name="Имя врача")
    middle_name = models.CharField(max_length=60, verbose_name="Отчество врача")
    phone = models.CharField(max_length=15, unique=True, verbose_name="Номер сотового")

    percent = models.IntegerField(verbose_name="Процент", default='30', blank=False, null=False)
    department = models.CharField(max_length=50, verbose_name="Департамент", default='SD', null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name="E-mail")
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения", editable=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Doctor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ["-date_created"]

    def FIO(self):
        return self.surname + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'
    def __str__(self):
        return self.surname + ' ' + self.first_name + ' ' + self.middle_name

    def get_absolute_url(self):
        return reverse('home')

class Procedur(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование процедуры")
    price = models.PositiveBigIntegerField(verbose_name="Стоимость")
    category = models.CharField(max_length=20, verbose_name="Категория")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения", editable=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Procedur, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Payment(models.Model):
    income = models.PositiveIntegerField(verbose_name="Сумма")
    payment_method = models.CharField(max_length=100,
                                      verbose_name="Способ оплаты",
                                      blank=False,
                                      default='Наличными')
    technical_cost = models.PositiveIntegerField(verbose_name="Тех. затраты", default=0)
    evening_shift = models.BooleanField(default=False,
                                        verbose_name="Вечерняя смена")
    patient = models.ForeignKey(Patient, verbose_name="Пациент",
                                null=True,
                                on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, verbose_name="Врач",
                               null=True,
                               on_delete=models.SET_NULL)
    procedurs = models.ForeignKey(
        Procedur,
        verbose_name="Процедуры",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения", editable=True)

    # дата создания платежа и изменения
    def save(self, *args, **kwargs):
          if not self.id:
                self.date_created = timezone.now()
          self.date_modified = timezone.now()
          return super(Payment, self).save(*args, **kwargs)

    class Meta:
          verbose_name = "Оплата"
          verbose_name_plural = "Оплаты"
          ordering = ["-date_created"]

    def __str__(self):
        return str(self.patient) + ' ' + ' ' + str(self.income)

    def get_absolute_url(self):
        return reverse('home')
