from django.urls import path
from app_ibgeando import views


urlpatterns = [
    path("", views.home, name="home"),
    path("estadual", views.estadual, name="estadual"),
    path("capital", views.capital, name="capital"),

    path('acre/', views.index_acre, name='index_acre'),
    path('alagoas/', views.index_alagoas, name='index_alagoas'),
    path('amapa/', views.index_amapa, name='index_amapa'),
    path('amazonas/', views.index_amazonas, name='index_amazonas'),
    path('bahia/', views.index_bahia, name='index_bahia'),
    path('ceara/', views.index_ceara, name='index_ceara'),
    path('distritofederal/', views.index_distritofederal,
         name='index_distritofederal'),
    path('espiritosanto/', views.index_espiritosanto, name='index_espiritosanto'),
    path('goias/', views.index_goias, name='index_goias'),
    path('maranhao/', views.index_maranhao, name='index_maranhao'),
    path('matogrosso/', views.index_matogrosso, name='index_matogrosso'),
    path('matogrossodosul/', views.index_matogrossodosul,
         name='index_matogrossodosul'),
    path('minasgerais/', views.index_minasgerais, name='index_minasgerais'),
    path('para/', views.index_para, name='index_para'),
    path('paraiba/', views.index_paraiba, name='index_paraiba'),
    path('parana/', views.index_parana, name='index_parana'),
    path('pernambuco/', views.index_pernambuco, name='index_pernambuco'),
    path('piaui/', views.index_piaui, name='index_piaui'),
    path('riodejaneiro/', views.index_riodejaneiro, name='index_riodejaneiro'),
    path('riograndedonorte/', views.index_riograndedonorte,
         name='index_riograndedonorte'),
    path('riograndedosul/', views.index_riograndedosul,
         name='index_riograndedosul'),
    path('rondonia/', views.index_rondonia, name='index_rondonia'),
    path('roraima/', views.index_roraima, name='index_roraima'),
    path('santacatarina/', views.index_santacatarina, name='index_santacatarina'),
    path('saopaulo/', views.index_saopaulo, name='index_saopaulo'),
    path('sergipe/', views.index_sergipe, name='index_sergipe'),
    path('tocantins/', views.index_tocantins, name='index_tocantins'),

    path('estado_acre/', views.estado_acre, name='estado_acre'),
    path('estado_alagoas/', views.estado_alagoas, name='estado_alagoas'),
    path('estado_amapa/', views.estado_amapa, name='estado_amapa'),
    path('estado_amazonas/', views.estado_amazonas, name='estado_amazonas'),
    path('estado_bahia/', views.estado_bahia, name='estado_bahia'),
    path('estado_ceara/', views.estado_ceara, name='estado_ceara'),
    path('estado_distritofederal/', views.estado_distritofederal,
         name='estado_distritofederal'),
    path('estado_espiritosanto/', views.estado_espiritosanto,
         name='estado_espiritosanto'),
    path('estado_goias/', views.estado_goias, name='estado_goias'),
    path('estado_maranhao/', views.estado_maranhao, name='estado_maranhao'),
    path('estado_matogrosso/', views.estado_matogrosso, name='estado_matogrosso'),
    path('estado_matogrossodosul/', views.estado_matogrossodosul,
         name='estado_matogrossodosul'),
    path('estado_minasgerais/', views.estado_minasgerais,
         name='estado_minasgerais'),
    path('estado_para/', views.estado_para, name='estado_para'),
    path('estado_paraiba/', views.estado_paraiba, name='estado_paraiba'),
    path('estado_parana/', views.estado_parana, name='estado_parana'),
    path('estado_pernambuco/', views.estado_pernambuco, name='estado_pernambuco'),
    path('estado_piaui/', views.estado_piaui, name='estado_piaui'),
    path('estado_riodejaneiro/', views.estado_riodejaneiro,
         name='estado_riodejaneiro'),
    path('estado_riograndedonorte/', views.estado_riograndedonorte,
         name='estado_riograndedonorte'),
    path('estado_riograndedosul/', views.estado_riograndedosul,
         name='estado_riograndedosul'),
    path('estado_rondonia/', views.estado_rondonia, name='estado_rondonia'),
    path('estado_roraima/', views.estado_roraima, name='estado_roraima'),
    path('estado_santacatarina/', views.estado_santacatarina,
         name='estado_santacatarina'),
    path('estado_saopaulo/', views.estado_saopaulo, name='estado_saopaulo'),
    path('estado_sergipe/', views.estado_sergipe, name='estado_sergipe'),
    path('estado_tocantins/', views.estado_tocantins, name='estado_tocantins'),

    path('capital_acre/', views.capital_acre, name='capital_acre'),
    path('capital_alagoas/', views.capital_alagoas, name='capital_alagoas'),
    path('capital_amapa/', views.capital_amapa, name='capital_amapa'),
    path('capital_amazonas/', views.capital_amazonas, name='capital_amazonas'),
    path('capital_bahia/', views.capital_bahia, name='capital_bahia'),
    path('capital_ceara/', views.capital_ceara, name='capital_ceara'),
    path('capital_espiritosanto/', views.capital_espiritosanto,
         name='capital_espiritosanto'),
    path('capital_goias/', views.capital_goias, name='capital_goias'),
    path('capital_maranhao/', views.capital_maranhao, name='capital_maranhao'),
    path('capital_matogrosso/', views.capital_matogrosso,
         name='capital_matogrosso'),
    path('capital_matogrossodosul/', views.capital_matogrossodosul,
         name='capital_matogrossodosul'),
    path('capital_minasgerais/', views.capital_minasgerais,
         name='capital_minasgerais'),
    path('capital_para/', views.capital_para, name='capital_para'),
    path('capital_paraiba/', views.capital_paraiba, name='capital_paraiba'),
    path('capital_parana/', views.capital_parana, name='capital_parana'),
    path('capital_pernambuco/', views.capital_pernambuco,
         name='capital_pernambuco'),
    path('capital_piaui/', views.capital_piaui, name='capital_piaui'),
    path('capital_riodejaneiro/', views.capital_riodejaneiro,
         name='capital_riodejaneiro'),
    path('capital_riograndedonorte/', views.capital_riograndedonorte,
         name='capital_riograndedonorte'),
    path('capital_riograndedosul/', views.capital_riograndedosul,
         name='capital_riograndedosul'),
    path('capital_rondonia/', views.capital_rondonia, name='capital_rondonia'),
    path('capital_roraima/', views.capital_roraima, name='capital_roraima'),
    path('capital_santacatarina/', views.capital_santacatarina,
         name='capital_santacatarina'),
    path('capital_saopaulo/', views.capital_saopaulo, name='capital_saopaulo'),
    path('capital_sergipe/', views.capital_sergipe, name='capital_sergipe'),
    path('capital_tocantins/', views.capital_tocantins, name='capital_tocantins'),
]
