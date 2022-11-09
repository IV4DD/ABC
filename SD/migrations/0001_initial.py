# Generated by Django 4.1 on 2022-10-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coworker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=20, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Номер сотового')),
                ('department', models.CharField(choices=[('DD¹', 'DD¹'), ('DD²', 'DD²'), ('DD³', 'DD³'), ('DD⁴', 'DD⁴'), ('DD⁵', 'DD⁵'), ('SD', 'SD'), ('Marketing Team', 'Marketing Team'), ('Call Center', 'Call Center'), ('DT', 'DT'), ('DM', 'DM'), ('Снабжение', 'Снабжение'), ('Офис', 'Офис'), ('Другое...', 'Другое...')], default='SD', max_length=30, verbose_name='Филиал/Отдел')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='E-mail')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('comment', models.TextField(blank=True, max_length=300, null=True, verbose_name='Дополнительная информация')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='photos_coworkers', verbose_name='Фото')),
                ('status', models.CharField(blank=True, choices=[('На рассмотрении', 'На рассмотрении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен')], default='На рассмотрении', max_length=30, null=True, verbose_name='Статус')),
                ('type_of_salary', models.CharField(blank=True, choices=[('Оклад', 'Оклад'), ('Процент', 'Процент')], default='Оклад', max_length=20, null=True, verbose_name='Тип зароботной платы')),
                ('salary', models.CharField(blank=True, max_length=20, null=True, verbose_name='Оплата за смену')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Позиция')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия врача')),
                ('first_name', models.CharField(max_length=60, verbose_name='Имя врача')),
                ('middle_name', models.CharField(max_length=60, verbose_name='Отчество врача')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Номер сотового')),
                ('percent', models.IntegerField(default='30', verbose_name='Процент')),
                ('department', models.CharField(blank=True, default='SD', max_length=50, null=True, verbose_name='Департамент')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='E-mail')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пациента')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия пациента')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество пациента')),
                ('phone', models.CharField(max_length=30, unique=True, verbose_name='Номер сотового')),
                ('iin', models.CharField(max_length=30, unique=True, verbose_name='ИИН')),
                ('gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='Пол пациента')),
                ('age', models.CharField(blank=True, max_length=7, null=True, verbose_name='Возраст пациента')),
                ('note', models.TextField(blank=True, max_length=500, null=True, verbose_name='Необязательный комментарий')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Procedur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование процедуры')),
                ('price', models.PositiveBigIntegerField(verbose_name='Стоимость')),
                ('category', models.CharField(max_length=20, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедуры',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.PositiveIntegerField(verbose_name='Сумма')),
                ('payment_method', models.CharField(default='Наличными', max_length=100, verbose_name='Способ оплаты')),
                ('technical_cost', models.PositiveIntegerField(default=0, verbose_name='Тех. затраты')),
                ('evening_shift', models.BooleanField(default=False, verbose_name='Вечерняя смена')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SD.doctor', verbose_name='Врач')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SD.patient', verbose_name='Пациент')),
                ('procedurs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SD.procedur', verbose_name='Процедуры')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
                'ordering': ['-date_created'],
            },
        ),
    ]
