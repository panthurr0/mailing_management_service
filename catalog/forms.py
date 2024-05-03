from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    banned_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for i in self.banned_words:
            if i in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово {i}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for i in self.banned_words:
            if i in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово {i}')

        return cleaned_data
