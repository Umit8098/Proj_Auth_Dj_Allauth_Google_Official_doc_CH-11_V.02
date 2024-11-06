## Dj All Auth - GoogleProvider

### Baştan proje kurulumu ->

```bash
- python -m venv env
- ./env/Scripts/activate
- pip install django
- django-admin --version
- python.exe -m pip install --upgrade pip
- pip freeze
- pip install python-decouple
- pip freeze > requirements.txt
- django-admin startproject main .
- py manage.py runserver
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
- py manage.py startapp users
```

### Secure your project

### .gitignore

.gitignore
```py
# Environments
.env
.venv
env/
venv/
```

### python-decouple

- Create .env file on root directory. We will collect our variables in this file.

.env
```py
SECRET_KEY = django-insecure-9p72pxko$)cm=wwzt81kg*6u-%#j*iyxhens02^96bw&iq2idn
```

settings.py
```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

- From now on you can send you project to the github, but double check that you added a .gitignore file which has .env on it.

- Run the server and see the initial setup:
 
```bash
py manage.py runserver  # or;
python manage.py runserver  # or;
python3 manage.py runserver
```

///////////////////////////////////////////////////
#### GİTHUB REPODAN clone bir projeyi ayağa kaldırma ->

```bash
- python -m venv env
- ./env/Scripts/activate
- pip install -r requirements.txt
- python.exe -m pip install --upgrade pip
- pip install python-decouple
- pip freeze > requirements.txt
```

- create .env and inside create SECRET_KEY 

```bash
- python manage.py migrate
- python manage.py runserver
```

///////////////////////////////////////////////////

- Projeyi ve app imizi oluşturduk, .gitignore ve .env dosyalarımızı da oluşturup SECRET_KEY imizi ve env ımızı içerisine koyduk.
- app imizi settings.py daki INSTALLED_APPS e ekliyoruz.
  
settings.py
```py
  INSTALLED_APPS = [
    ...
    # myApps
    'users',
    # 3rd_party_package
]
```

#### urls configurasyonu yapalım;

main/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
```

users/urls.py
```py
from django.urls import path

urlpatterns = [
]
```

#### templates-views-urls;

- başlangıç olarak user app'imizde kullanacağımız base.html, home.html templates lerini oluşturalım; 
    users/templates/users
klasör yapısını oluşturuyoruz.

##### base.html oluşturma;
- base.html oluşturup, onun içinde navbar oluşturacağız ve bu bizim temel template'imiz olacak ve diğerlerini bundna extends edeceğiz.
- users app'imizde başlangıçta kullanacağımız templates'leri oluşturalım;
 - base.html
 - home.html


##### bootstrap5 ekleme;
- base.html template'imizde bootstrap5 cdn ile kullanacağız. bootstrap5'i popper'sız kullanacağız.
- bootstrap5 cdn kodlarını alıp sayfada ilgili kısımlara yerleştiriyoruz.

##### navbar ekleme;
- base.html template'imizde navbar oluşturacağız. bootstrap ve css ile de stillendireceğiz.

##### block content ekleme;


users/templates/users/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- bootstrap5, CSS-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Google Auth App</title>
</head>
<body>

    <nav class="navbar navbar-expand-lg bg-warning">
        <div class="container-fluid">
            
            <!-- Navbar'ı mobilde açılabilir yapmak için buton -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    {% comment %}{% url 'home' %}{% endcomment %}
                    <a class="nav-link active" aria-current="page" href="#">Google-Auth</a>
                </div>               
                    
                    {% if request.user.is_authenticated %}

                        {% if request.user.is_superuser %}
                        <ul class="navbar-nav me-auto">
                            <li class="nav-item active">
                                <a class="nav-link" target="blank" href="/admin">Admin Panel</a>
                            </li>
                        </ul>
                        {% endif %}
                    
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item active">
                                <a class="nav-link" href="">{{ request.user | capfirst}}</a>
                            </li>
                        
                            <li class="nav-item active">
                                {% comment %}{% url 'user_logout' %}{% endcomment %}
                                <a class="nav-link" target="blank" href="#">Logout</a>
                            </li>
                        </ul>
                    
                    {% else %}
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item active">
                                {% comment %}{% url 'user_login' %}{% endcomment %}
                                <a class="nav-link" target="blank" href="#">Login</a>
                            </li>

                            <li class="nav-item active">
                                {% comment %}{% url 'register' %}{% endcomment %}
                                <a class="nav-link" target="blank" href="#">Register</a>
                            </li>

                        </ul>
                    {% endif %}
            </div>
        </div>
    </nav>
    
        <!-- For messages -->
    <div class="messages">
        {% if messages %}
            {% for message in messages %}
            <p class="message text-center alert alert-{{ message.tags }}">
                {% if message.level == messages.ERROR %}Important: {% endif %}
                {{ message }}
            </p>
            {% endfor %}
        {% endif %}
    </div>

    {% block content %}

    {% endblock content %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</body>
</html>
```


users/templates/users/home.html
```html
{% extends 'users/base.html' %}

{% block content %}

<div class="container pt-4">
    <div class="row mt-2 p-0">
        <div class="col-lg-4 mx-auto p-0">
            <div class="alert alert-warning text-center">
                <h2>Google Authentication</h2>
            </div>
        </div>
    </div>
</div>

{% endblock content %}
```

- base ve home template'lerimizi yazdık. Şimdi bunları render edecek view ve urls yazacağız.

users/wiews.py
```py
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'users/home.html')
```

users/urls.py
```py
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home")
]
```

- Test edelim, projemizi runserver edip çalıştırıyoruz;

```bash 
- py manage.py runserver
``` 

- Evet çalıştı.

- base ve home templatelerimiz hazır. Şimdi login, register ve logout işlemleri

##### register;

- register işlemi için user'ın "username" ve "email" gibi bilgilerini alacağımız bir form düzenliyoruz.
- users/forms.py oluşturuyoruz.
- Bu formu user create ederken kullanacağımız için djangonun defalt formlarından UserCreationForm unu kullanıyoruz. Bu form bizi password işlemlerinden kurtararak kendisi default olarak yapıyor. Biz sadece model ve field belirtiyoruz. 
- Model olarak da djangonun default User modelini kullanacağız.

users/forms.py
```py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
```

- bu formu kulanarak register view'imizi yazıyoruz.
- kullanıcı register olur olmaz da login ediyoruz.

users/views.py
```py
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login

...

def register(request):
    form_user = UserForm
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('home')
    context = {
        'form_user': form_user
    }
    return render(request, 'users/register.html', context)
```

- view'imizi çalıştıracak urls/endpoint'imizi yazalım.

users/urls.py
```py
...
from .views import home, register

urlpatterns = [
    ...
    path("register/", register, name="register"),
]
```

- Şimdi register template'imizi yazalım.

users/templates/users/register.html
```html
{% extends 'users/base.html' %}

{% block content %}

<h1>Registration Page</h1>
<form action="" method="POST">
    
    {% csrf_token %}
    
    {% if form.errors %}
        <p>There is something wrong with what you entered.</p>
    {% endif %}
    
    {{ form_user.as_p }}
    
    {{ form_profile.as_p }}

    <input type="submit" value="Register">
        
</form>

{% endblock content %}
```


- Test edelim. Önce base.html'deki "register" buttonunu aktif hale getirelim;
users/templates/users/base.html

```html 
...
  <li class="nav-item active">
      {% comment %}{% url 'register' %}{% endcomment %}
      <a class="nav-link" target="blank" href="{% url 'register' %}">Register</a>
  </li>
...
``` 

- Evet çalıştı. Register formunu doldurduktan sonra bizi login ediyor ve home page'e redirect ediyor. Kullanıcı adımızı da navbarda görüyoruz.

##### login;

- Login olurken de yine aynı şekilde forms.py'da register olurken oluşturduğumuz UserForm'u inherit ederek kullandığımız djangonun default formlarından UserCreationForm gibi burada da djangonun default formlarından AuthenticationForm 'unu kullanıyoruz. 

users/views.py
```py
...
from django.contrib.auth.forms import AuthenticationForm

...
def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user() #! formdan gelen user bilgileri alıyoruz.
        login(request, user) #! Gelen user bilgileri ile login isteği yapıyoruz.
        messages.success(request, "You have been logged in.")
        return redirect('home')
    return render(request, 'users/login.html', {"form": form})
    #! context içindeki veriyi buradan da gönderebiliriz.
```

- view'imizi çalıştıracak urls/endpoint'imizi yazalım.

users/urls.py
```py
...
from .views import (
    home, 
    register,
    user_login
)

urlpatterns = [
    ...
    path("login/", user_login, name="login"),
]
```

- Şimdi login template'imizi yazalım.

users/templates/users/login.html
```html
{% extends 'users/base.html' %}

{% block content %}

<h1>Login</h1>

<form action="" method="POST">

    {% csrf_token %}
    
    {{ form.as_p }}

    <button type="submit">Login</button>

</form>

{% endblock content %}
```


- Test edelim. Önce base.html'deki "login" buttonunu aktif hale getirelim;
users/templates/users/base.html

```html 
...
<li class="nav-item active">
    {% comment %}{% url 'user_login' %}{% endcomment %}
    <a class="nav-link" target="blank" href="{% url 'user_login' %}">Login</a>
</li>
...
``` 

- Evet çalıştı. Login formunu doldurduktan sonra bizi login ediyor ve home page'e redirect ediyor. Kullanıcı adımızı da navbarda görüyoruz.


##### logout;

- Loout olurken sadece logout() methodunu içine request göndererek yapabiliyoruz.
- Ardından home page'e redirect ediyoruz.

users/views.py
```py
...
from django.contrib.auth import login, logout

...
def user_logout(request):
    messages.success(request, "You have been logged out.")
    logout(request)
    return redirect('home')
    # return render(request, 'users/logout.html')
```

- view'imizi çalıştıracak urls/endpoint'imizi yazalım.

users/urls.py
```py
...
from .views import (
    ...,
    user_logout,
)

urlpatterns = [
    ...
    path("logout/", user_logout, name="user_logout"),
]
```

- Şimdi normalde user'ı logout edince home page'e redirect ediyoruz. Ancak bir logout template'i istenirse şöyle birşey yazılabilir.

users/templates/users/logout.html
```html
{% extends 'users/base.html' %}

{% block content %}

<h3>You have been logged out.</h3>

<a href="{% url 'user_login' %}">Log in again</a>

{% endblock content %}
```


- Test edelim. Önce base.html'deki "logout" buttonunu aktif hale getirelim;

users/templates/users/base.html
```html 
...
<li class="nav-item active">
    {% comment %}{% url 'user_logout' %}{% endcomment %}
    <a class="nav-link" target="blank" href="{% url 'user_logout' %}">Logout</a>
</li>
...
``` 

- Evet çalıştı. User Logout edilip, home page'e redirect edildi.

##### statics;

- users app'inde static files' lar kullanacağız. Mesela logo, picture, image, css, js file gibi. Bunlar için şu klasör yapısını kullanacağız;
- users app'inin altında şu klasör yapısını oluşturuyoruz; 
    users/static/users

- bu klasör yapısı altında oluşturduğumuz images, css, js klasörlerinin içinde files'larımızı baındıracağız.
    users/static/users/images
                   .../css
                   .../js


- copy cw_logo to this folder
(cw_logo resmini kopyala bu klasöre yapıştır.)

- static folder ın altındaki users folder ının altında css, image, js folderları daha önceden oluşturulmuştur. Bunları copy-paste ile kullanıyoruz. 
  - css altına 
    - style.css, bootstrap.min.css 
  - image ın altına 
    - cw_logo resmi 
  - js  nin altına 
    - timeout.js 
  eklenmiştir.  


- cw_logo ve avatar resimlerini kopyalayıp image klasörünüm içine yapıştırıyoruz.

- static folder ın altındaki users folder ının altında css, image, js folderları daha önceden oluşturulmuştur. Bunları copy-paste ile kullanıyoruz. 
  - css altına 
    - style.css, bootstrap.min.css 
  - image ın altına 
    - cw_logo resmi 
  - js  nin altına 
    - timeout.js 
  eklenmiştir.  


- static_url, static_root ve media_url, media_root ayarlarını yapalım,

main/urls.py
```py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Template'lerde {% load static %} tag'ini kullanalım;

- navbar'a logo ve isim ekleyelim;
base.html
```html
...
<a class="navbar-brand ms-3 " href="{% url 'home' %}">
    <img src="{% static 'users/images/cw_logo.jpg' %}" alt="CLARUSWAY_LOGO" class="img-fluid rounded-3" style="max-height: 40px;"/> Umit Developer</a>
...
```

##### js ekleme (timeout.js);

- static/users/js/timeout.js dosyası oluşturup içine kodumuzu yazıyoruz.
- Ardından script tag'imizle js kodumuzu base template'imize body'nin bitiminin hemen üstüne ekliyoruz.

users/static/users/js/timeout.js
```js
let element = document.querySelector('.message');

setTimeout(function() {
    element.style.display = 'none';
}, 1000);
```

users/templates/users/base.html
```html
...
    <script src="{% static 'users/js/timeout.js' %}"></script>
</body>
</html>
```

- Test ediyoruz; çalıştı.


##### crispy_forms & bootstrap5;

- formlar düzgün görünsün diye crispy form ve bootstra5 ekleyip, formlarımızda kullanalım.

- https://django-crispy-forms.readthedocs.io/en/latest/install.html#

- https://github.com/django-crispy-forms/crispy-bootstrap5

```bash
- pip install django-crispy-forms
- pip install crispy-bootstrap5
- pip freeze > requirements.txt
```

settings.py
```py
  INSTALLED_APPS = [
    ...
    # myApps
    'users',
    'myapp',
    # 3rd_party_package
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
```

- login template'imizde kullanacağımız formlar düzgün görünsün diye de crispy paketini template'te kullanalım.

users/templates/users/login.html
```html
{% extends 'users/base.html' %}

{% block content %}

{% load crispy_forms_tags %}

<div class="container mt-4">
    <div class="row justify-content-center">
        <div class="col-md-3">
            <h3 class="text-center custom-border-radius">Please Login</h3>

            <form action="" method="post" class="bg-secondary text-light mt-3 mb-5 p-2 custom-border-radius">
                {% csrf_token %}
                {{ form | crispy }}
                <p class="text-center">
                    <button type="submit" class="btn btn-danger">Login</button>
                </p>
            </form>

        </div>
    </div>
</div>

{% endblock content %}
```


- register template'imizde kullanacağımız formlar düzgün görünsün diye de crispy paketini template'te kullanalım.

users/templates/users/register.html
```html
{% extends 'users/base.html' %}

{% block content %}

{% load crispy_forms_tags %}

<div class="container mt-4">
    <div class="row justify-content-center">
        <div class="col-md-3">
            <h3 class="text-center custom-border-radius">Please Login</h3>

            <form action="" method="post" class="bg-secondary text-light mt-3 mb-5 p-2 custom-border-radius">
                {% csrf_token %}
                {{ form | crispy }}
                <p class="text-center">
                    <button type="submit" class="btn btn-danger">Login</button>
                </p>
            </form>

        </div>
    </div>
</div>

{% endblock content %}
```


##### style css;

- style.css dosyasında logi ve register templateleri için stil verelim;
- style.css dosyasını base.html'de link ile bootstrap5 linkinin altında tanımlayalım
  
users/templates/users/base.html
```html
<!-- bootstrap5 -->
...
<!-- CSS -->
<link rel="stylesheet" href="{% static 'users/css/style.css' %}">
```

users/static/users/css/style.css
```css
* {
    /* margin: 0;
    padding: 0; */
    box-sizing: border-box;
}

body {
    background-image: url(https://cdn.pixabay.com/photo/2017/01/24/03/53/plant-2004483__480.jpg);
    background-size: cover;
    background-repeat: no-repeat;
}

h3 {
    background-color: #d3af2e;
    color: #ffffff; /* İstediğin rengi buraya gir */
}

h2 {
    background-color: #d3af2e;
    color: #ffffff; /* İstediğin rengi buraya gir */
}

.custom-border-radius {
    border-radius: 10px; /* İstediğiniz değer */
    /*background-color: rgba(0, 0, 0, 0.5); /* Arka plan rengi eklemek isteyebilirsiniz */
    padding: 10px; /* İç boşluk */
}
```

users/templates/users/home.html
```html
...
<div class="text-center">
    <h2 class="custom-border-radius">Google Authentication</h2>
</div>
...
```



### Dj_All_Auth - GoogleProvider google account ile login/register;

- Bunun işlemi django-allauth paketi ile yapıyoruz.

- https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html

- Öncelikle django-allauth paketinin kurulumunu yapıyoruz.
- Eğer social account işlemleri yapmayacaksak kurulumu sadece şekilde yapıyoruz;

```bash
- pip install django-allauth
- pip freeze > requirements.txt
```

- Fakat social account işlemleri de yapacaksak kurulumu şu şekilde yapıyoruz;

```bash
- pip install "django-allauth[socialaccount]"
- pip freeze > requirements.txt
```

- settings.py'daki INSTALLED_APPS' e hangi social account ile giriş yapacaksak onun kodu ile birlikte şunları ekliyoruz;
- Burada dikkat edilmesi gereken husus şu kodun -> 'django.contrib.sites', olması/eklenmesi gerektiği dokümanda belirtilmiyor ama bu kod mutlaka eklenmesi gerekiyor.

settings.py
```py
...
INSTALLED_APPS = [
    ...,
    # social_accounts
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]
...
```

- settings.py'daki TEMPLATES kısmında, OPTIONS içinde, context_processors içinde şunu kontrol et! yoksa ekle!  Genelde oluyor, fakat bazı eski sürümlerde olmayabiliyor. Eğer yoksa ekliyoruz; 
    'django.template.context_processors.request',

settings.py
```py
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                # `allauth` needs this from django
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]
```


- settings.py'a AUTHENTICATION_BACKENDS kodlarını ekle!

settings.py
```py
...
# for social_accounts
AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]
...
```

- settings.py'daki MIDDLEWARE kısmına "allauth.account.middleware.AccountMiddleware",  kodunu ekle! (Bunu dokümana bakarak yapıyoruz. Instractor bunu eklemedi. Ancak son sürümde gelmiş olabilir.)

settings.py
```py
...
MIDDLEWARE = [
    ...
    # for social accounts Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]
...
```


- BU KISIMA DİKKAT!!
 
- settings.py'a SOCIALACCOUNT_PROVIDERS  ekle. Eğer bunu eklemezsek, o an browser'daki google hesabı hangisi ise, hiç sormadan direkt o an açık olan hesap ile sisteme login/giriş yapıyor. Bunu ekleyerek hangi google hesabı ile giriş/login olmak istediğimizi seçebilmemizi sağıyoruz.
- Normalde dokümanda bu şekilde eklenmesi belirtiliyor. client_id ve secret value'larının google'dan alınarak buraya eklenmesi gerekiyor. Bu kısmın da secret veri içerdiğinden güvenlik için .env'de gizlenmesi gerekiyor.
- Fakat instractor farklı bir kod kullandı, client_id ve secret value'larını admin panelden social account içine ekledi.
- Burada olması gereken şekli ile (V.02) yapılacak.

- V.02

settings.py
```py
...
# # Provider specific settings, instractor'ın yaptığı şekil V.01;
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

## Gemini AI;
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type':'online',
#         },
#         'CLIENT_ID':'123456789',
#         'SECRET_KEY':'123456789',
#     }
# }

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123456789',
            'secret': '123456789',
            'key': ''
        }
    }
}

...
```


- settings.py'a SOCIALACCOUNT_PROVIDERS  ekle. Eğer bunu eklemezsek, o an browser'daki google hesabı hangisi ise, hiç sormadan direkt o an açık olan hesap ile sisteme login/giriş yapıyor. Bunu ekleyerek hangi google hesabı ile giriş/login olmak istediğimizi seçebilmemizi sağıyoruz.

settings.py
```py
...
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123456789',
            'secret': '123456789',
            'key': ''
        }
    }
}

# Gemini AI;
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type':'online',
#         },
#         'CLIENT_ID':'123456789',
#         'SECRET_KEY':'123456789',
#     }
# }

...
```

- Bu kısmın da secret veri içerdiğinden güvenlik için .env'de gizliyoruz;

settings.py
```py
...
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_SECRET'),
            'key': ''
        }
    }
}
...
```

.env
```py
...
GOOGLE_CLIENT_ID=123456789
GOOGLE_SECRET=123456789
...
```



- !!!!! Bu kısım da dokümanda geçmiyor. Fakat bu kodun da eklenmesi gerekiyor.

- settings.py'a SITE_ID = 1 (example.com)
- Bu SITE_ID = 1 bazen çalışmayabiliyor. django default olarak otomatik bir site tanımlıyor çünkü. example.com gibi bir tanımlama yapıyor. 2 veya 3 de yapabilirsiniz. eğer example.com gibi kalsın, editlemek istemiyorum derseniz bunu 2 yapacaksınız.
- Admin panelden bakarak, orada django site için id olarak ne belirlemişse, kodun çalışması için onu yazacağız buraya.
- Bu değeri, admin panelinde oluşturduğunuz sitenin ID'si ile eşleştirin.

settings.py
```py
...
# for soccial accounts. Dokümanda geçmiyor.
# SITE_ID = 1 # Bu değeri, admin panelinde oluşturduğunuz sitenin ID'si ile eşleştirin.
# SITE_ID = 2
SITE_ID = 3
...
```


- urls patternimize de path('accounts/', include('allauth.urls')),  path'ini ekliyoruz. main/urls.py'a gidip;

main/urls.py
```py
...
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
] ...
```


- daha sonra migrate işlemlerini yapıyoruz.

```bash
- py manage.py migrate
```

- Ek olarak, google account ile login olduktan sonra redirect edilecek bir url lazım. Normalde default olarak allauth'dan gelen default page'e gidiyor. Biz oraya değil de login olduğunda home page'e git!!
- Bunun için settings.py'da LOGIN_REDIRECT_URL = 'home'  belirtiyoruz.

settings.py
```py
...
LOGIN_REDIRECT_URL = 'home'
...
```

- !!!!!! Bu kısım çok gerekli mi anlayamadım. !!!!!
- settings.py ve urls.py'da yazmamız gereken kodları yazdık.
- Admin panele gidip bakalım, SITES ve SOCIAL ACCOUNTS kısmlarımızı kontrol edelim.
- SITES içinde example.com var mı? , onu açtığımızda url'de bize gösterdiği adresteki id numarası ile settings.py'da bizim yazdığımız SITE_ID numarası eşleşiyor mu kontrol edelim.
   http://127.0.0.1:8000/admin/sites/site/2/change/



#### Google Developer Console'da Uygulama Oluşturma

https://console.cloud.google.com/home/dashboard?project=model-cirrus-440721-s1

- Google Cloud Platform'a gidin ve yeni bir proje oluşturun.
  - Projeye isim veriyoruz. -> Create

- Projeniz için OAuth consent screen'i yapılandırın.
  - External -> Create
  - App information -> App name veriyoruz, email kısmından bağlı olan email seçiyoruz, Developer contact information kısmına ikinci bir email yazıyoruz -> Save and Continue, Save and Continue, 
- Creadentials kısmında -> CREATE CREDENTIALS -> OAuth clint ID -> Application type -> Web Application seçiyoruz, 
  - Authorized JavaScript origins -> ADD URL -> Url1 ->
     Şuan için localde çalıştığımız için local linkini veriyoruz; http//127.0.0.1.8000 ve ADD URL -> Url2 -> http//localhost:8000
  - Authorized redirect URLs -> Url1 -> http//127.0.0.1.8000/accounts/google/login/callback/
    ADD URL -> Url2 -> http//localhost:8000/accounts/google/login/callback/

- (Projeyi deploye ettikten sonra url'de yazdığımız localhost yerine mesela http://pythonanywhere.com ekleyeceğiz.)
  
- CREATE
    
- OAuth 2.0 client ID'si ve client secret'ini oluşturun. Oluşturduğumuz bu client ID'si ve client secret ile;

- settings.py dosyasındaki SOCIALACCOUNT_PROVIDERS bölümündeki CLIENT_ID ve SECRET_KEY ayarlarını oluşturduğunuz değerlerle güncelleyin. (V.02'de yapıyoruz.)



#### all-auth template uygulaması;

- Tekrar dokümana dönüyoruz; 
  
  https://django-allauth.readthedocs.io/en/latest/socialaccount/templates.html

- template'imizde link vermek istiyorsak, şu template tag'ini kullanmalıyız;
    {% load socialaccount %}

- Mesela login.html'de user'ın google account'u ile login olabilmesi için bir button vereceğiz.
  login.html
  ```html
  {% load socialaccount %}
  <a href="{% provider_login_url 'google' %}">Google</a>
  ```


##### google accounts default sayfasını pass geçme;

- Fakat bu link ile bizi default bir sayfa olan Sign In Via Google  page'ine yönlendiriyor. 
- Biz bu sayfaya yönlendirsin istemiyoruz.
- Bunun için all-auth paketinin env klasöründeki yerini bulup, templates -> socialaccounts -> login.html  inceliyoruz, bir form var ve post isteği ile continue atıyor. Bizim bir form ile post isteği atmamız gerekiyor, ama nereye buradaki default login.html'e ki o da user'ın google accounts'larını seçebilmesi için ilgili sayfaya yönlendirsin.
- Bunun için all-auth paketinin default page'indeki formu alıp override edip kendi login page'imize ekleyerek, all-auth'un default page'ini pass geçip bizi login etmesi için google account seçme sayfasına yönlendirmesini sağlıyoruz. Bunu da nasıl yapıyoruz; form'un action kısmında bu formun nereye atıf yapmasını belirtiyoruz.
- Peki action kısmında default login.html'in url'ini vereceğiz. Peki buna nereden ulaşıyoruz? dokümanın verdiği url'den yani {% provider_login_url 'google' %}   'den ulaşabiliyoruz.  formun action kısmına yazıyoruz.
 
- Bunun için template'imizde {% load socialaccount %}  tag'ini de kullanarak;

login.html
```html
{% load socialaccount %}
{% comment %} override ederek redirect home page {% endcomment %}
<form action="{% provider_login_url 'google' %}" method="post" class="bg-secondary text-light custom-border-radius text-center">
    {% csrf_token %}
        <button type="submit" class="btn btn-danger text-center">Login with Google</button>
</form>
```

- Evet artık Sign In Via Google page'ine hiç uğramadan direkt olarak google account seçme sayfasına yönleniyoruz.

- Bunun için template'imizde {% load socialaccount %}  tag'ini kullanarak, dokümanda belirttiği şekilde a tag'iyle link verebiliriz.

users/login.html
```html
{% extends 'users/base.html' %}

{% block content %}

{% load socialaccount %}

{% load crispy_forms_tags %}

<div class="container mt-4">
    <div class="row justify-content-center">
        <div class="col-md-3">
            <h3 class="text-center custom-border-radius">Please Login</h3>

            <div class="d-grid gap-2">

                <form action="" method="post" class="bg-secondary text-light mt-3 mb-5 p-2 custom-border-radius">
                    {% csrf_token %}
                    {{ form | crispy }}
                    <p class="text-center">
                        <button type="submit" class="btn btn-danger">Login</button>
                    </p>
                </form>

                {% comment %} override ederek redirect home page {% endcomment %}
                <form action="{% provider_login_url 'google' %}" method="post" class="bg-secondary text-light custom-border-radius text-center">
                    {% csrf_token %}
                        <button type="submit" class="btn btn-warning text-center text-danger fw-bold custom-border-radius w-100">Login with Google</button>
                </form>

                {% comment %} default link verme {% endcomment %}
                <a class="btn btn-warning text-danger fw-bold custom-border-radius" href="{% provider_login_url 'google' %}">Login with Google Account</a>

            </div>
        </div>
    </div>
</div>

{% endblock content %}
```


- Aynısını register.html'e de yazıyoruz. Böylelikle hem register, hem login olurken google account ile giriş yapabiliyor kullanıcı.

users/register.html
```html
...
{% load socialaccount %}
...
{% comment %} override ederek redirect home page {% endcomment %}
<form action="{% provider_login_url 'google' %}" method="post" class="bg-secondary text-light custom-border-radius text-center">
    {% csrf_token %}
        <button type="submit" class="btn btn-warning text-center text-danger fw-bold custom-border-radius w-100">Register with Google Account</button>
</form>
...
```


#### all-auth template uygulaması ile user'ın image'ını alıp gösterme;

- social account ile login olan user'ın image'ını şu şekilde alabiliyoruz. 
- Biz bu projede çektiğimiz image'ı base.html'de navbarda user name ile birlikte gösteriyoruz.
 
     <img src="{{ user.socialaccount_set.all.0.get_avatar_url }}" alt="" class="rounded-5">

users/base.html
```html
...
<ul class="navbar-nav ms-auto">
    <li class="nav-item active d-flex align-items-center">
        <img src="{{ user.socialaccount_set.all.0.get_avatar_url }}" alt="" class="rounded-circle" width="50" height="50">
        <a class="nav-link" href="">{{ request.user | capfirst}}</a>
        <a class="nav-link" target="blank" href="{% url 'user_logout' %}">Logout</a>
    </li>
</ul>
...
```
