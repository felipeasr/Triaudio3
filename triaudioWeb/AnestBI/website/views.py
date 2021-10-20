from django.shortcuts import render ,redirect
from website.forms import usuariofrom , pacienteform
from .models import paciente,usuario
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
def Index(request):
    return render(request, 'Index.html', {})

def conclusao(request):
    return render(request, 'conclusoes.html', {})


def dicas(request):
    return render(request, 'Dicas.html', {})


def agenda(request):
    return render(request, 'Agenda.html', {})

def audiometriacondicionada(request):
    return render(request, 'Audiometriacondicionada.html', {})

def avaliacoesORL(request):
    return render(request, 'AvaliacoesORL.html', {})

def avaliacoesmedicas(request):
    return render(request, 'Avaliacoesmedicas.html', {})
def emissoesOtoacusticas(request):
    return render(request, 'EmissoesOtoacusticas.html', {})

def dash(request):
    return render(request,'dash.html',{})

def Audiometria(request):
    return render(request,'Audiometria.html',{})
def Peate(request):
    return render(request,'PEATEintegridade.html',{})
def PeateFrequencia(request):
    return render(request,'Peatefrequenciaespecifica.html',{})

def teste(request):
    return render(request,'teste.html')

def reteste(request):
    return render(request,'reteste.html',{})

def medidasacusticas(request):
    return render(request, 'medidasacusticas.html',{})
def novopaciente(request):
        data = {}
        data['form'] = pacienteform 
        return render(request, 'novopaciente.html', data)

def salvarpac(request):
    if request.method == 'POST':
        form = pacienteform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dash')
def cadastrogeral(request):
    context = {'cadastrogeral' : paciente.objects.all()}
    return render(request,'cadastrogeral.html',context)

def login(request):
    return render(request,'account/login.html',{})

def profissional(request):
    data = {}
    data['form'] = usuariofrom
    return render(request,'Profissional.html',data)
def salvarprof(request):
     if request.method == 'POST':
        form = usuariofrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_signup')

    
#############################################################codigo exemplo#######################################
def cadio(request):
    ##<!--SCORE DE LEE-->
    if request.method == "POST":
        operacao_intraperitioneal_sim = request.POST.get('operacao-intraperitoneal-sim', 0)
        intratoracica = request.POST.get('intratoracica',0)
        hist_Doenca_Arter = request.POST.get('histDoencaArter',0)
        hist_Insuf_Card = request.POST.get('histInsufCard',0)
        hist_Cerebrovascular = request.POST.get('histCerebrovascular',0)
        diab_Com_Insuli = request.POST.get('diabComInsuli',0)
        creat_Pre_Op_2mg = request.POST.get('creatPreOp2mg',0)

        if operacao_intraperitioneal_sim == "sim":
            operacao_intraperitioneal_sim = 1
        else:
            operacao_intraperitioneal_sim = 0
       
        if intratoracica == "sim":
            intratoracica = 1
        else:
            intratoracica = 0
      
        if hist_Doenca_Arter == "sim":
            hist_Doenca_Arter = 1
        else:
            hist_Doenca_Arter = 0
    
        if hist_Insuf_Card == "sim":
            hist_Insuf_Card = 1
        else:
            hist_Insuf_Card = 0
     
        if hist_Cerebrovascular == "sim":
            hist_Cerebrovascular = 1
        else:
            hist_Cerebrovascular = 0
     
        if diab_Com_Insuli == "sim":
            diab_Com_Insuli = 1
        else:
            diab_Com_Insuli = 0
     
        if creat_Pre_Op_2mg == "sim":
            creat_Pre_Op_2mg = 1
        else:
            creat_Pre_Op_2mg = 0

        resultado = operacao_intraperitioneal_sim + intratoracica + hist_Doenca_Arter + hist_Insuf_Card + hist_Cerebrovascular + diab_Com_Insuli + creat_Pre_Op_2mg
        if resultado == int(0):
            resultado1 = "Risco baixo (0,4%)"
        elif resultado == int(1):
            resultado1 = "Risco baixo (0,9%)"
        elif resultado == int(2):
            resultado1 = "Risco moderado (6,6%)"
        elif resultado > int(2):
            resultado1 = "Risco alto (11%)\n Dosagem de trponina operatória e após 48h\n Dosagem de BNP\n Pós operatório imediato em UTI\nComplicações cardíacas maiores incluem: infarto do miocárdio, edema pulmonar, fibrilação ventricular ou parada cardíaca primária, e bloqueio cardíaco completo até o 5º dia pós-operatório."
        if diab_Com_Insuli == int(1):
            diab_Com_Insuli = "Manter glicemia perioperatória entre 80mg/dl - 180 mg/dl \n Não usar hipoglicemiante oral no dia da cirurgia \n Se utiliza insulina NPH, fazer metade da dose na manhã da cirurgia \n Monitorizar glicemia de 4/4Hs \n Sugerimos fazer testes de glicose sanguínea e HbA1c em pacientes com diagnóstico de diabetes mellitus e em pacientes agendados para cirurgia ortopédica ou vascular de grande porte \n Sugerimos fazer uma avaliação cuidadosa das vias aéreas em pacientes com diabetes de longa data."
    ## <!-- Cálculo de MET --> 
    if request.method == "POST":
        MET = request.POST.get('MET', 0)
        MET1 = request.POST.get('MET1',0)
        MET2 = request.POST.get('MET2',0)
        MET3 = request.POST.get('MET3',0)
        MET4 = request.POST.get('MET4',0)
        MET5 = request.POST.get('MET5',0)
        MET6 = request.POST.get('MET6',0)
        MET7 = request.POST.get('MET7', 0)
        MET8 = request.POST.get('MET8',0)
        MET9 = request.POST.get('MET9',0)
        MET10 = request.POST.get('MET10',0)
        MET11 = request.POST.get('MET11',0)

        if MET == "sim":
            MET = 2.7
        else:
            MET = 0

        if MET1 == "sim":
            MET1 = 1.75
        else:
            MET1 = 0

        if MET2 == "sim":
            MET2 = 2.75
        else:
            MET2 = 0

        if MET3 == "sim":
            MET3 = 5.5
        else:
            MET3 = 0

        if MET4 == "sim":
            MET4 = 8.0
        else:
            MET4 = 0

        if  MET5 == "sim":
            MET5 = 2.7
        else:
            MET5 = 0
        
        
        if  MET6 == "sim":
            MET6 = 3.5
        else:
            MET6 = 0
        
        if  MET7 == "sim":
            MET7 = 8.0
        else:
            MET7 = 0
        
        if  MET8 == "sim":
            MET8 = 4.5
        else:
            MET8 = 0
        
        if  MET9 == "sim":
            MET9 = 5.25
        else:
            MET9 = 0
        
        if  MET10 == "sim":
            MET10 = 6.0
        else:
            MET10 = 0
        
        if  MET11 == "sim":
            MET11 = 7.5
        else:
            MET11 = 0

        somaMet = MET + MET1 + MET2 +MET3 + MET4 + MET5 + MET6 + MET7 + MET8 + MET9 + MET10 + MET11
        VO2 = round(0.43*somaMet + 9.6)
        Mets = round (VO2/3.5)
        
        
    #Condições de alto risco perioperatório
    if request.method == "POST":
            sca = request.POST.get('sca', 0)
            igc = request.POST.get('igc', 0)
            ag = request.POST.get('ag', 0)
            vis = request.POST.get('vis', 0)
            hp = request.POST.get('hp', 0)
            ae = request.POST.get('ae', 0)
            fafc = request.POST.get('fafc', 0)
            pas = request.POST.get('pas', 0)
            saa = request.POST.get('saa', 0)

            if sca == "sim":
                sca = 1
            else:
                sca = 0
            if igc == "sim":
                igc = 1
            else:
                igc = 0
            if ag == "sim":
                ag = 1
            else:
                ag = 0
            if vis == "sim":
                vis = 1
            else:
                vis = 0
            if hp == "sim":
                hp = 1
            else:
                hp = 0        
            if ae == "sim":
                ae = 1
            else:
                ae = 0 
            if fafc == "sim":
                fafc = 1
            else:
                fafc = 0 
            if pas == "sim":
                pas = 1
            else:
                pas = 0 
            if saa == "sim":
                saa = 1
            else:
                saa = 0 

        
            carp = sca + igc + ag + vis + hp + ae + fafc + pas + saa
        # END Condições de alto risco perioperatório
        #AUB
    if request.method == "POST":
            AUBidade = request.POST.get('AUBidade', 0)
            AUBhemoglobina = request.POST.get('AUBhemoglobina',0)
            AUBcardiopatia = request.POST.get('AUBcardiopatia',0)
            AUBangina = request.POST.get('AUBangina',0)
            AUBvascular = request.POST.get('AUBvascular',0)
            AUBemergencia = request.POST.get('AUBemergencia',0)
        

            if AUBidade == "sim":
                AUBidade = 1
            else:
                AUBidade = 0
        
            if AUBhemoglobina == "sim":
                AUBhemoglobina = 1
            else:
                AUBhemoglobina = 0
        
            if AUBcardiopatia == "sim":
                AUBcardiopatia = 1
            else:
                AUBcardiopatia = 0
        
            if AUBangina == "sim":
                AUBangina = 1
            else:
                AUBangina = 0
        
            if AUBvascular == "sim":
                AUBvascular = 1
            else:
                AUBvascular = 0
        
            if  AUBemergencia == "sim":
                AUBemergencia = 1
            else:
                AUBemergencia = 0
            aub = AUBidade+AUBhemoglobina+AUBcardiopatia+AUBangina+AUBvascular+AUBemergencia
        
            ### Resolver 
            #if aub<= int(1):
             #aub = "RISCO BAIXO"
            #if aub== int(2) or aub== int(3):
             #aub ="RISCO INTERMEDIÁRIO"
            #if aub >= int(3):
             #aub = "RISCO ALTO" 
    ## END AUB
    ##<!-- delirium -->
    if request.method == "POST":
        idade60 = request.POST.get('idade60', 0)
        idade70 = request.POST.get('idade70', 0)
        idade80 = request.POST.get('idade80',0)
        atividades = request.POST.get('atividades', 0)
        auxilio = request.POST.get('auxilio', 0)
        alcool = request.POST.get('alcool',0)
        Delirium = request.POST.get('Delirium', 0)
        cirugia = request.POST.get('cirugia', 0)
        emergencia = request.POST.get('emergencia',0)
        proteina = request.POST.get('proteina',0)

        if idade60 == "sim":
            idade60 = 0
        else:
            idade60 = 1

        if idade70 == "sim":
            idade70 = 1
        else:
            idade70 = 0

        if idade80 =="sim":
            idade80 = 2
        else:
            idade80 = 0

        if atividades == "sim":
            atividades = 0
        else:
            atividades = 1

        if auxilio == "sim":
            auxilio = 1
        else:
            auxilio = 0

        if alcool == "sim":
            alcool =1
        else:
            alcool =0
        if Delirium == "sim":
            Delirium = 1
        else:
            Delirium = 0
        if cirugia == "sim":
            cirugia = 1
        else:
            cirugia = 0
        if emergencia == "sim":
            emergencia =1
        else:
            emergencia =0
        if proteina == "sim":
                proteina =1
        else:
            proteina =0

        FP = proteina+emergencia+cirugia+Delirium+alcool+auxilio+atividades+idade80+idade70+idade60
        if FP< int(6):
            delirium ="BAIXO RISCO"      
        if FP > int(5):
            delirium ="ALTO RISCO condutas pré-operatórias:	1-Evitar jejum prolongado de líquidos [6hs] 2- Avaliação geriátrica e otimização clínica Condutas intraoperatórias 1-anestesia multimodal poupadora de opióides (*uso de cetamina 0,2-05 mg/Kg não aumentou a incidência) 2- Evitar Hipotermia 3- uso de dexmedetomidina se possível 4- monitorização da consciência 5- uso de paracetamol e AINES Medicações que aumentam o risco de Delirium : Gabapentinóides, Anti depressivos triciclicos, benzodiazepínicos, anticolinérgicos (escopolamina) OUTRAS CONDIÇÕES que predispõe ao Delirium: {Cirurgia aberta, cirurgia de emergência e cirurgia abdominal}{desidratação, hipo/hipernatremia,hipotermia,dor pós operatória,doença cardiovascular,DM}"
 ##<!-- Risco Instrínsico da cirurgia -->
    if request.method == "POST":
        risco = request.POST.get('risco', 0)
        risco2 = request.POST.get('risco2', 0)
        risco3 = request.POST.get('risco3', 0)
        
        riscoR = ""
        if risco == "sim":
            riscoR = "RISCO BAIXO"
        if risco2 == "sim":
            riscoR ="RISCO ALTO"
        if risco == "nao" and risco2 == "nao" and risco3 == "sim": 
            riscoR ="RISCO MODERADO" 
        if risco == "nao" and risco2 == "nao" and risco3 == "nao": 
            riscoR ="RISCO MODERADO"   
    
    
                         

        return render(request, 'cadio.html', {'resultado':resultado,'riscoR':riscoR , 'diab_Com_Insuli': diab_Com_Insuli, 'somaMet': Mets, 'VO2': VO2,'carp':carp,'delirium':FP,'aub':aub})
    else:
        return render(request, 'cadio.html', {})

  
  
    ##    return render(request, 'cadio.html', {'Risco_result':Risco_result})
    ##else:
    ##    return render(request, 'cadio.html', {})  



    ## AUB-HAS2 
    



      
      ##  return render(request, 'cadio.html', {'somaMet':somaMet, 'VO2':VO2})
    ##else:
       ## return render(request, 'cadio.html', {})

def calculadoraQxMD(request):
    return render(request,'calculadoraQxMD.html',{})