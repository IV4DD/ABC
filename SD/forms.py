import datetime
from django import forms
from .models import Payment, Patient, Doctor, Procedur, Coworker
from django.forms import SelectDateWidget, ModelForm
from django.core.validators import RegexValidator
from django_select2 import forms as s2forms




# Capitalization of Input
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
class CapitalizeInputForm(forms.CharField):
    def to_python(self, value):
        return value.capitalize()



class CoworkerForm(forms.ModelForm):
    # Validations
    first_name = CapitalizeInputForm(
        label='Имя',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Иван',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    middle_name = CapitalizeInputForm(
        label='Отчество',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Ибрагимович',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    surname = CapitalizeInputForm(
        label='Ваша фамилия',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Ахметов',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )

    email = Lowercase(
        label='Адрес электронной почты',
        max_length=50,
        min_length=7,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                                   message="Проверьте правильность ввода E-Mail адресса!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'E-mail*',
            'style': 'font-size: 15px; text-transform: lowercase;'
        })
    )

    comment = forms.CharField(
        label=' Дополнительная информация',
        max_length=200,
        min_length=5,
        required=False,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.Textarea(
            attrs={'placeholder': 'Введите текст в произвольной форме',
                   'rows': 3})
    )

    salary = forms.CharField(
        label='Зарплата',
        required=False,
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[0-9]*$', message="Допустимы только цифры!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите сумму или процент',
            'style': 'font-size: 18px;'
        })
    )

    profile_pic = forms.ImageField(
        label='Ваше фото (не обязательно):',
        required=False,
    )

    class Meta:
        model = Coworker
        fields = '__all__'

        POSITIONS = (
            ('', 'Выберите должность'),
            ('Врач', 'Врач'),
            ('Ассистент', 'Ассистент'),
            ('Младший мед. персонал', 'Младший мед. персонал'),
            ('Ассистент', 'Ассистент'),
            ('Медсестра', 'Медсестра'),
            ('Администратор', 'Администратор'),
            ('Другое', 'Другое'),
        )


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

        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Телефон',
                    'data-mask': '(000) 000 00 00',
                }
            ),
            'department': forms.Select(
                choices=DEPARTMENTS,
                attrs={
                    'class': 'form-control',
                }
            ),
            'birthday': forms.DateInput(
                attrs={
                    'style': 'font-size: 15px; cursor: pointer;',
                    'type': 'date',
                    'min': datetime.date.today()-datetime.timedelta(days=23725),
                    'max': datetime.date.today()-datetime.timedelta(days=6570),
                }
            ),
            'date_created': forms.DateInput(
                attrs={
                    'style': 'font-size: 15px; cursor: pointer;',
                    'type': 'date',
                    'min': datetime.date.today()-datetime.timedelta(days=23725),
                    'max': datetime.date.today()-datetime.timedelta(days=6570),
                }
            ),
            'position': forms.Select(
                choices=POSITIONS,
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class DoctorForm(ModelForm):
        # Validations
        first_name = CapitalizeInputForm(
            label='Ваше имя:',
            max_length=20,
            min_length=2,
            validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Федор',
                    'style': 'font-size: 15px; text-transform: capitalize;'
                }
            )
        )
        middle_name = CapitalizeInputForm(
            label='Отчество',
            max_length=20,
            min_length=2,
            validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Худайбергенулы',
                    'style': 'font-size: 15px; text-transform: capitalize;'
                }
            )
        )
        surname = CapitalizeInputForm(
            label='Фамилия',
            max_length=20,
            min_length=2,
            validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Ахметов',
                    'style': 'font-size: 15px; text-transform: capitalize;'
                }
            )
        )

        email = Lowercase(
            label='Адрес электронной почты',
            max_length=50,
            min_length=7,
            validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                                       message="Проверьте правильность ввода E-Mail адресса!")],
            widget=forms.TextInput(attrs={'placeholder': 'E-mail*'})
        )

        birthday = forms.DateField(
            label='Выберите дату рождения:',
            widget=SelectDateWidget(years=range(1950, datetime.date.today().year + 1)),
            required=True
        )

        profile_pic = forms.ImageField(
            label='Ваше фото (не обязательно):',
            required=False,
        )

        class Meta:
            model = Doctor
            fields = [
                'first_name',
                'middle_name',
                'surname',
                'phone',
                'email',
                'department',
                'percent',
                'birthday',
                'profile_pic',
            ]

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

            widgets = {
                'phone': forms.TextInput(
                    attrs={
                        'placeholder': 'Телефон',
                        'data-mask': '(000) 000 00 00',
                    }
                ),
                'department': forms.Select(
                    choices=DEPARTMENTS,
                    attrs={
                        'class': 'form-control',
                    }
                ),
                'percent': forms.TextInput(
                    attrs={
                        'placeholder': 'Введите процент Врача',
                        'minlength': '2',
                        'maxlength': '2',
                    }
                ),
            }

class ProcedurForm(ModelForm):

    class Meta:
        model = Procedur
        fields = ['name', 'price', 'category', 'description']

        CATEGORIES = [
            ('Терапия', 'Терапия'),
            ('Профилактика', 'Профилактика'),
            ('Эндодонтия', 'Эндодонтия'),
            ('Хирургия', 'Хирургия'),
            ('Имплантация', 'Имплантация'),
            ('Ортопедия', 'Ортопедия'),
            ('Ортодонтия', 'Ортодонтия'),
            ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название процедуры',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Введите стоимость процедуры',
                }
            ),
            'category': forms.Select(
                choices=CATEGORIES,
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Введите описание процедуры',
                    'rows': 3
                }
            )
        }

class PatientForm(ModelForm):
    # Validations
    first_name = CapitalizeInputForm(
        label='Имя',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Абдумажит',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    middle_name = CapitalizeInputForm(
        label='Отчество',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Абдукадырович',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    surname = CapitalizeInputForm(
        label='Фамилия',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Касымов',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )

    note = forms.CharField(
        label=' Дополнительная информация:',
        max_length=200,
        min_length=5,
        required=False,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.Textarea(
            attrs={'placeholder': 'Введите текст в произвольной форме',
                   'rows': 2}
        )
    )

    class Meta:
        model = Patient
        exclude = [
            'date_created',
            'date_modified',
            ]

        AGES = (
            ('до 10', 'до 10'),
            ('10 - 20', '10 - 20'),
            ('20 - 30', '20 - 30'),
            ('30 - 40', '30 - 40'),
            ('40 - 50', '40 - 50'),
            ('50 - 60', '50 - 60'),
            ('60+', '60+'),
        )
        GENDERS = (
            ('М', 'М'),
            ('Ж', 'Ж'),
        )

        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Телефон',
                    'data-mask': '(000) 000 00 00',
                }
            ),
            'iin': forms.TextInput(
                attrs={
                    'placeholder': 'ИИН',
                    'data-mask': '0000 0000 0000',
                }
            ),
            'gender': forms.Select(
                choices=GENDERS,
                attrs={
                    'class': 'form-control',
                }
            ),
            'age': forms.Select(
                choices=AGES,
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def label_from_instance(self, obj):
        return obj.name

class PaymentForm(ModelForm):

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        label='Выберите пациента',
        widget=s2forms.ModelSelect2Widget(
            attrs={'class': 'form-control'},
            model=Patient,
            search_fields=['first_name__icontains',
                           'phone__icontains',
                           'surname__icontains',
                           'middle_name__icontains',
                           'iin__icontains'],
            max_results=5,
        )
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        label='Выберите врача',
        widget=s2forms.ModelSelect2Widget(
            attrs={'class': 'form-control'},
            model=Doctor,
            search_fields=['first_name__icontains',
                           'surname__icontains',
                           'middle_name__icontains',
                           'phone__icontains',
            ],
            max_results=5,
        )
    )

    procedurs = forms.ModelChoiceField(
        queryset=Procedur.objects.all(),
        label='Выберите оказанную процедуру',
        widget=s2forms.ModelSelect2Widget(
            attrs={
                'class': 'form-control',
                'data-placeholder': 'Оказанные процедуры'
            },
            model=Procedur,
            search_fields=['name__icontains'],
            max_results=5,
        )
    )




    class Meta:
        model = Payment
        fields = ['income', 'payment_method', 'technical_cost', 'evening_shift', 'patient', 'doctor', 'procedurs']

        PAYMENT_METHODS = [
            ('Наличными', 'Наличными'),
            ('Картой', 'Картой'),
            ('Перевод', 'Перевод'),
            ('KaspiRed', 'KaspiRed'),
            ('Kaspi Рассрочка', 'Kaspi Рассрочка'),
            ('Бартер с ВВ', 'Бартер с ВВ'),
            ('Бартер без ВВ', 'Бартер без ВВ'),
        ]
        SHIFTS = [
            ('Дневная', 'Дневная'),
            ('Вечерняя', 'Вечерняя'),
        ]

        widgets = {
            'income': forms.TextInput(
                attrs={
                    'placeholder': 'Введите сумму',
                }
            ),
            # technical_cost
            'technical_cost': forms.TextInput(
                attrs={
                    'placeholder': 'Введите сумму затрат',
                }
            ),
            'payment_method': forms.Select(
                choices=PAYMENT_METHODS,
                attrs={
                    'class': 'form-control',
                },
            ),
        }
