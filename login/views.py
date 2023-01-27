from multiprocessing import context
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout, get_user_model 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


from .forms import CreateUserForm 
from .tokens import account_activation_token


def logoutUser(request): 
    logout(request)
    return redirect('login:cadastro')

def cadastroPage(request): 
    if not request.user.is_authenticated: 
        form = CreateUserForm();  

        if request.method == 'POST':

            if request.POST.get('realSignUp'): 
                form = CreateUserForm(request.POST)
                if form.is_valid(): 
                    user = form.save(commit=False)
                    user.is_active = False 
                    user.save() 
                    activateEmail(request, user, form.cleaned_data.get('email'))
            elif request.POST.get('realSignIn'):
                username = request.POST.get('username')      
                password = request.POST.get('password')      
                user = authenticate(request, username=username, password=password)

                if user is not None: 
                    login(request, user)
                    return redirect('livros:home-page')
                else:
                    messages.info(request, 'Senha ou usuário incorretos')
    else: return redirect('livros:home-page')

    context = {'form': form}
    return render(request, 'login/cadastro.html', context)

def ativar(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, f"Muito obrigado por confirmar seu email, {user.username}. Agora você pode acessar nosso acervo.")
    else:
        messages.error(request, "Link de ativação inválido!")

    return redirect('login:cadastro')

def activateEmail(request, user, to_email):
    mail_subject = "Ative sua conta"
    message = render_to_string("login/ativarconta.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Clique no email enviado para {to_email} e verifique sua conta.\nCaso não encontre, verifique a caixa de spam ou tente novamente.')
    else:
        messages.error(request, f'Problema ao enviar o email de verificação para {to_email}, veja se está digitado corretamente.')