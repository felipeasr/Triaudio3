from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('dash.html', views.dash, name = "dash"),
    path('account/login.html', views.login, name="login"),
    path('Profissional.html', views.profissional, name="Profissional"),
    path('salvarprof/',views.salvarprof,name="salvarprof"),
    path('cadatrogeral.html', views.cadastrogeral,name="cadastrogeral"),
    path('novopaciente.html', views.novopaciente, name= "novopaciente"),
    path('salvarpac/',views.salvarpac,name="salvarpac"),
    path('teste.html',views.teste,name="teste"),
    path('reteste.html',views.reteste,name="reteste"),
    path('medidasacusticas.html',views.medidasacusticas,name="medidasacusticas"),
    path('Audmetria.html',views.Audiometria,name="Audiometria"),
    path('PEATEintegridade.html',views.Peate,name="Peate"),
    path('Peatefrequenciaespecifica.html',views.PeateFrequencia,name="Peatefrequencia"),
    path('conclusoes.html',views.conclusao,name="conclusao"),
    path('Agenda.html',views.agenda,name="agenda"),
    path('Audiometriacondicionada.html',views.audiometriacondicionada,name="audiometriacondicionada"),
    path('AvaliacoesORL.html',views.avaliacoesORL,name="avaliacoesORL"),
    path('Avaliacoesmedicas.html',views.avaliacoesmedicas,name="avaliacoesmedicas"),
    path('emissoesOtoacusticas.html',views.emissoesOtoacusticas,name="EmissoesOtoacusticas"),
    path('Dicas.html',views.dicas,name="dicas"),
]

