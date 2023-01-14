from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.template import Template,Context
from .models import *
from django.views.generic import ListView
from ranking_tutoria.clasificadores import*



# Create your views here.
class inicio_sesion(ListView):
    model=dato_usuarios
    template_name = 'login_v2.html'
     
    #mediante la siguiente funcion pasaremos contexto
    def get_context_data(self, **kwargs):
        #creamos variable fecha para pasarla como parámetro a la plantilla respectiva
        fecha = datetime.today()
        #quitamos la hora
        fecha =fecha.date()
        context = super().get_context_data(**kwargs)
        context={"fecha":fecha}
        return context


def autenticar(request):
    print ("-----------------ta entrando------------------------")
    username=request.POST['username']
    password=request.POST['password']
    
    tutores = dato_tutores.objects.all()

    # Recupera todos los objetos de la tabla
    datos = dato_usuarios.objects.values('usuario','contrasenia')
    # Itera a través de los objetos
    contador=0
    for coordinador in datos:
        #--comprobante
        print ("usuario coordinador uuuuuuuu", coordinador['usuario'])
        print ("usuario coordinador", coordinador['contrasenia'])
        print ("tutores datasos", tutores[1].id) #forma correcta de ubicar 
        # Compara el campo "campo" con el elemento
        if (coordinador['usuario'] == username and coordinador['contrasenia'] == password):
            
            # Si el usuario y contraseña existen
            #return redirect('../elegir_accion/')

            #este código debe ejecutarlo el módulo previo al módulo de mostrar datos osea ranking.html

            #RANKING DE TUTORES 
            t_id=[]
            t_nro_tuto=[]
            t_ses_i=[]
            t_ses_g=[]
            t_ref=[]
            t_ate=[]
            t_cri=[]
            for i in tutores:
                t_id.append(i.id)
                t_nro_tuto.append(i.nro_tutorados)
                t_ses_i.append(i.ses_individuales)
                t_ses_g.append(i.ses_grupales)
                t_ref.append(i.referidos)
                t_ate.append(i.atendidos)
                t_cri.append(i.criterio)
            print("\n\n----- ides obtenidos",t_id)
            ranking_tutores=rank_tutores(t_id, t_nro_tuto, t_ses_i, t_ses_g, t_ref, t_ate, t_cri) #conexion inestable

            for i in ranking_tutores:
                (print("ranking de : ", i[0], "->", i[1]))
            
            for tuto in ranking_tutores:
                if (tuto[1]==0):
                    dato_tutores.objects.filter(id=tuto[0]).update(fk_ranking=5)
                if (tuto[1]==1):
                    dato_tutores.objects.filter(id=tuto[0]).update(fk_ranking=6)
                if (tuto[1]==2):
                    dato_tutores.objects.filter(id=tuto[0]).update(fk_ranking=7)
                if (tuto[1]==3):
                    dato_tutores.objects.filter(id=tuto[0]).update(fk_ranking=8)
                if (tuto[1]==4):
                    dato_tutores.objects.filter(id=tuto[0]).update(fk_ranking=9)

            #RANKING DE TUTORADOS
            tutorados = dato_tutorados.objects.all()
            tu_id=[]
            tu_ciclo=[]
            tu_beca=[]
            tu_moda=[]

            for i in tutorados:
                tu_id.append(i.id)
                tu_ciclo.append(i.ciclo)
                tu_beca.append(i.tipo_beca)
                tu_moda.append(i.modalidad)

            print("\n\n----- ides obtenidos",tu_id, tu_ciclo, tu_beca, tu_moda)
            ranking_tutorados=rank_tutorados(tu_id, tu_ciclo, tu_beca) #conexion inestable, ya estable:3 quitamos modalidad por el momento

            for i in ranking_tutorados:
                (print("ranking de : ", i[0], "->", i[1]))
            
            
            for tuto in ranking_tutorados:
                if (tuto[1]==0):
                    dato_tutorados.objects.filter(id=tuto[0]).update(fk_ranking=5)
                if (tuto[1]==1):
                    dato_tutorados.objects.filter(id=tuto[0]).update(fk_ranking=6)
                if (tuto[1]==2):
                    dato_tutorados.objects.filter(id=tuto[0]).update(fk_ranking=7)
                if (tuto[1]==3):
                    dato_tutorados.objects.filter(id=tuto[0]).update(fk_ranking=8)
                if (tuto[1]==4):
                    dato_tutorados.objects.filter(id=tuto[0]).update(fk_ranking=9)



            #datos que requiere ranking.html
            contexto={'nom_usuario':coordinador['usuario'], 'tutores':tutores, 't_rankings':ranking_tutores}
            return render(request, 'ranking.html', contexto)

        else:
            messages.error(request, "Nombre de usuario o Contraseña incorrecta")
            
            #devolvemos al inicio de sesi�n
            return redirect('login/',messages)
        """
        elif (contador==len(datos)-1):
            #mostramos error
            messages.add_message(request, messages.ERROR, 'nombre de usuario o contrasenia incorrectos')
            #devolvemos al inicio de sesión
            return redirect('login/')
        contador+=1"""

     
def mostrar(request):
    tutores = dato_tutores.objects.all()
    contexto={"tutores":tutores}
    return render(request,'ranking.html', contexto)

def subir_tutorados(request):
    return render(request,'ph1_accion.html',{})

def mostrar_tutorados(request):
    print ("entre--------------")
    ident=request.POST['idprueba']
    print("reconocio", type(ident),ident)
    
    #reservamos el código del tutor
    cod_tutor=''
    for char in ident:
        if char.isdigit():
          cod_tutor+=char
    
    print("el tutor respectivo es : ", cod_tutor)

    #print("op1 ",ident[1])
    tutores=dato_tutores.objects.all()
    tutorados=dato_tutorados.objects.filter(fk_dato_tutor=cod_tutor)
 
    contexto={'tutores':tutores,'tutorados':tutorados}

    return render(request, 'ranking.html', contexto)


def mostrar_tutorados_prueba(request):
    tutores = dato_tutores.objects.all()
    if request.method == 'POST':
        identificado = request.POST['identificador']
        print("el identificador para conseguir a sus tutorados es: ",identificado)
        # Get the image file for the item

        contexto = {"tutores":tutores}
        return render(request, 'ranking.html', contexto)
    #return render(request,'ph1_accion.html',{})
    #return render(request,'ph1_accion.html',{})