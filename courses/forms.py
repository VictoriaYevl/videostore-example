from django import forms
from .models import Course
#класс для отображ формы
class CourseAddForm(forms.ModelForm):
    slug = forms.CharField(
        label = 'Название URL*',
        required = True,
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите тему вашего письма'})
    )
    title = forms.CharField(
        label='Название курса*',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите тему вашего письма'})
    )
    description = forms.CharField(
        label='Введите описание курса',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите описание курса'})
    )
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )
    
    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']
