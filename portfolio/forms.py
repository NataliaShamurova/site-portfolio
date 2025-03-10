from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        label='Введите Ваше имя',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя',
                   'class': 'form-control',
                   }
        )
    )
    email = forms.EmailField(
        label='Введите Ваш Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Адрес, на который прислать ответ',
                   'class': 'form-control',
                   }
            )

    )
    message = forms.CharField(
        label='Напишите сообщение',
        widget=forms.Textarea(
            attrs={'placeholder': 'Текст сообщения',
                   'class': 'form-control',
                   }
        )
    )
