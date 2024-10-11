from django.forms import ModelForm

from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': '''
                    w-fit
                    text-xs
                    text-end
                    bg-transparent
                    text-black/40
                    dark:text-white/40
                    outline-none''',
            })    