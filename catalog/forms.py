from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_product_title(self):
        cleaned_data = self.cleaned_data['product_title']

        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое слово в наименовании: "{word}"')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое слово в описании: "{word}"')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        # exclude = ('is_active', )
        fields = '__all__'

