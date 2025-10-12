from django import forms

from .models import Cakes, Categorey, Flavours, Shapes, Weights, EggStatusChoices, Toppings

class AddCakeForm(forms.ModelForm):

    class Meta:

        model = Cakes

        # define fields
        
        # fields = ['name', 'weight', 'etc...']

        # if all feilds from html form then use all.

        fields = '__all__'

        exclude = ['uuid','active_status']

        # to apply styles

        widgets  = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'desciption': forms.Textarea(attrs={
                'class':'form-control',
                'required':'required',
                'rows': 3,
            }),
            'photo': forms.FileInput(attrs={
                'class':'form-control',
                # 'required':'required',
            }),
            'price': forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'is_available': forms.RadioSelect(choices=[(True, 'Yes'),(False, 'No')],attrs={
                'class':'form-check-input',
                'required':'required',
            })
        }

    categorey = forms.ModelChoiceField(queryset=Categorey.objects.all(), widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    flavour = forms.ModelChoiceField(queryset=Flavours.objects.all(), widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    shape = forms.ModelChoiceField(queryset=Shapes.objects.all(), widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    weight = forms.ModelChoiceField(queryset=Weights.objects.all(), widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    egg_sts = forms.ChoiceField(choices=EggStatusChoices.choices, widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    toppings = forms.ModelChoiceField(queryset=Toppings.objects.all(), widget=forms.Select(attrs={
        'class':'form-select',
        'required':'required',
    }))

    def __init__(self,*args,**kwargs):

        super(AddCakeForm,self).__init__(*args,**kwargs)

        if not self.instance:

            self.fields.get('photo').widget.attrs['required'] = 'required'