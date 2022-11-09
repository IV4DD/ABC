from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

STATUSES = [
    ('На рассмотрении', 'На рассмотрении'),
    ('Утвержден', 'Утвержден'),
    ('Отклонен', 'Отклонен'),
]


class MyAccountManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, first_name, middle_name, surname, email, username, dob, password=None):
        if not first_name:
            raise ValueError('Необходимо ввести имя!')
        if not middle_name:
            raise ValueError('Необходимо ввести отчество!')
        if not surname:
            raise ValueError('Необходимо ввести фамилию!')
        if not email:
            raise ValueError('Необходимо ввести номер телефона!')
        if not username:
            raise ValueError('Необходимо ввести пароль!')
        if not dob:
            raise ValueError('Необходимо ввести дату рождения!')


        user = self.model(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            username=username,
            dob=dob,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, middle_name, surname, email, username, dob, password):
        user = self.create_user(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            username=username,
            dob=dob,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name              = models.CharField(max_length=30, verbose_name="Имя")
    middle_name             = models.CharField(max_length=30, verbose_name="Отчество")
    surname                 = models.CharField(max_length=30, verbose_name="Фамилия")
    email                   = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    username                = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name="Номер сотового")
    dob                     = models.DateField(verbose_name="Дата рождения", null=True, blank=True)

    image                   = models.ImageField(default='default.jpg', upload_to='profile_pics')
    position                = models.CharField(max_length=1000, verbose_name="Должность", null=True)
    status                  = models.CharField(max_length=30, verbose_name="Статус", choices=STATUSES, default='На рассмотрении', null=True, blank=True)

    date_joined             = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='Дата авторизации', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'surname', 'email', 'dob',]

    objects = MyAccountManager()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        # return self.email
        return self.surname + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'

    def FIO(self):
        return self.surname + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
