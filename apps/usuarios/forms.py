from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: Habacuque Gosch"
            }
        )
    )
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: Habacuque Gosch"
            }
        )
    )

    email = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: Habacuque312@gmail.com"
            }
        )
    )

    senha_cadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

    senha_confirma = forms.CharField(
        label="Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
    

    # def clean_senha_confirma(self):
    #     senha_1 = self.cleaned_data.get('senha_cadastro')
    #     senha_2 = self.cleaned_data.get('senha_confirma')

    #     if senha_1 and senha_2:
    #         if senha_1 != senha_2 :
    #             raise forms.ValidationError('As senhas não são iguais')
    #         else:
    #             return senha_2
             