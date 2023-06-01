from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
import json
from lxml import html


def home(request):
    dados = {
        'pop': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N1[all]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1298/periodos/2010/variaveis/614?localidades=N3[all]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,
    }
    return render(request, 'index.html', dados)


def index_acre(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ac.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[12]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ac/rio-branco.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ac.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ac/rio-branco.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ac/rio-branco.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',

    }
    return render(request, 'index/acre.html', dados)


def index_alagoas(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/al.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[27]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/al/maceio.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/al.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/al/maceio.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/al/maceio.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/alagoas.html', dados)


def index_amapa(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ap.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[16]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ap/macapa.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ap.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ap/macapa.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ap/macapa.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/amapa.html', dados)


def index_amazonas(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/am.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[13]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/am/manaus.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/am.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/am/manaus.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/am/manaus.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/amazonas.html', dados)


def index_bahia(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ba.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[29]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ba/salvador.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ba.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ba/salvador.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ba/salvador.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/bahia.html', dados)


def index_ceara(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ce.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[23]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ce/fortaleza.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ce.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ce/fortaleza.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ce/fortaleza.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/ceara.html', dados)


def index_distritofederal(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/df.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[53]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/df/brasilia.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/df.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,
    }
    return render(request, 'index/distritofederal.html', dados)


def index_espiritosanto(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/es.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[32]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/es/vitoria.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/es.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/es/vitoria.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/es/vitoria.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/espiritosanto.html', dados)


def index_goias(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/go.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[52]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/go/goiania.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/go.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/go/goiania.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/go/goiania.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/goias.html', dados)


def index_maranhao(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ma.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[21]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ma/sao-luis.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ma.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ma/sao-luis.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ma/sao-luis.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/maranhao.html', dados)


def index_matogrosso(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/mt.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[51]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mt/cuiaba.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mt.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/mt/cuiaba.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mt/cuiaba.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/matogrosso.html', dados)


def index_matogrossodosul(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ms.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[50]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ms/campo-grande.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ms.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ms/campo-grande.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ms/campo-grande.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/matogrossodosul.html', dados)


def index_minasgerais(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/mg.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[31]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mg/belo-horizonte.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mg.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/mg/belo-horizonte.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/mg/belo-horizonte.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/minasgerais.html', dados)


def index_para(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pa.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[15]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pa/belem.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pa.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pa/belem.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pa/belem.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/para.html', dados)


def index_paraiba(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pb.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[25]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pb/joao-pessoa.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pb.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pb/joao-pessoa.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pb/joao-pessoa.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/paraiba.html', dados)


def index_parana(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pr.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[41]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pr/curitiba.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pr.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pr/curitiba.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pr/curitiba.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/parana.html', dados)


def index_pernambuco(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pe.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[26]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pe/recife.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pe.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pe/recife.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pe/recife.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/pernambuco.html', dados)


def index_piaui(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pi.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[22]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pi/teresina.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pi.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/pi/teresina.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/pi/teresina.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/piaui.html', dados)


def index_riodejaneiro(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rj.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[33]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rj/rio-de-janeiro.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rj.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rj/rio-de-janeiro.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rj/rio-de-janeiro.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/riodejaneiro.html', dados)


def index_riograndedonorte(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rn.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[24]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rn/natal.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rn.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rn/natal.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rn/natal.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/riograndedonorte.html', dados)


def index_riograndedosul(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rs.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[43]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rs/porto-alegre.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rs.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rs/porto-alegre.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rs/porto-alegre.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/riograndedosul.html', dados)


def index_rondonia(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ro.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[11]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ro/porto-velho.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ro.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/ro/porto-velho.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/ro/porto-velho.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/rondonia.html', dados)


def index_roraima(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rr.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[14]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rr/boa-vista.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rr.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/rr/boa-vista.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/rr/boa-vista.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/roraima.html', dados)


def index_santacatarina(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/sc.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[42]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sc/santa-catarina.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sc.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/sc/santa-catarina.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sc/santa-catarina.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/santacatarina.html', dados)


def index_saopaulo(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/sp.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[35]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/sao-paulo.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sp.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/sao-paulo.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/sao-paulo.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/saopaulo.html', dados)


def index_sergipe(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/se.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[28]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/se.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/sergipe.html', dados)


def index_tocantins(request):
    dados = {
        'pop_est': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_est': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/to.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_est': json.loads(requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades=N3[17]").text)[0]['resultados'][0]['series'][0]['serie']['2010'].replace(".", ",") + ' hab/km²',

        'alf': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/to/palmas.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[4]/div/p')[0].text.replace(" ", "") + '%',

        'sal': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/to.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[8]/div/p')[0].text,

        'pop_cap': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),

        'ter_cap': BeautifulSoup(requests.get('https://www.ibge.gov.br/cidades-e-estados/to/palmas.html').text, "html.parser").select_one("#responseMunicipios > div.pure-g > div.pure-u-1.pure-u-lg-14-24 > ul > li:nth-child(1) > div > p").get_text().replace("[2022]", ""),

        'dens_cap': html.fromstring(requests.get('https://www.ibge.gov.br/cidades-e-estados/to/palmas.html').content).xpath('//*[@id="responseMunicipios"]/div[2]/div[2]/ul/li[3]/div/p')[0].text.replace(" ", "") + ' hab/km²',
    }
    return render(request, 'index/tocantins.html', dados)


def estadual(request):
    return render(request, 'estadual.html')


def estado_acre(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[12]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/acre.html', dados)


def estado_alagoas(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[27]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/alagoas.html', dados)


def estado_amapa(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[16]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/amapa.html', dados)


def estado_amazonas(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[13]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/amazonas.html', dados)


def estado_bahia(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[29]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/bahia.html', dados)


def estado_ceara(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[23]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/ceara.html', dados)


def estado_distritofederal(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[53]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/distritofederal.html', dados)


def estado_espiritosanto(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[32]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/espiritosanto.html', dados)


def estado_goias(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[52]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/goias.html', dados)


def estado_maranhao(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[21]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/maranhao.html', dados)


def estado_matogrosso(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[51]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/matogrosso.html', dados)


def estado_matogrossodosul(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[50]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/matogrossodosul.html', dados)


def estado_minasgerais(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[31]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/minasgerais.html', dados)


def estado_para(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[15]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/para.html', dados)


def estado_paraiba(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[25]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/paraiba.html', dados)


def estado_parana(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[41]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/parana.html', dados)


def estado_pernambuco(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[26]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/pernambuco.html', dados)


def estado_piaui(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[22]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/piaui.html', dados)


def estado_riodejaneiro(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[33]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/riodejaneiro.html', dados)


def estado_riograndedonorte(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[24]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/riograndedonorte.html', dados)


def estado_riograndedosul(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[43]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/riograndedosul.html', dados)


def estado_rondonia(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[11]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/rondonia.html', dados)


def estado_roraima(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[14]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/roraima.html', dados)


def estado_santacatarina(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[42]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/santacatarina.html', dados)


def estado_saopaulo(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[35]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/saopaulo.html', dados)


def estado_sergipe(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[28]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/sergipe.html', dados)


def estado_tocantins(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N3[17]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'estados/tocantins.html', dados)


def capital(request):
    return render(request, 'capital.html')


def capital_acre(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1200401]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/acre.html', dados)


def capital_alagoas(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2704302]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/alagoas.html', dados)


def capital_amapa(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1600303]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/amapa.html', dados)


def capital_amazonas(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1302603]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/amazonas.html', dados)


def capital_bahia(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2927408]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/bahia.html', dados)


def capital_ceara(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2304400]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/ceara.html', dados)

def capital_espiritosanto(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[3205309]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/espiritosanto.html', dados)


def capital_goias(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[5208707]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/goias.html', dados)


def capital_maranhao(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2111300]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/maranhao.html', dados)


def capital_matogrosso(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[5103403]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/matogrosso.html', dados)


def capital_matogrossodosul(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[5002704]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/matogrossodosul.html', dados)


def capital_minasgerais(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[3106200]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/minasgerais.html', dados)


def capital_para(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1501402]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/para.html', dados)


def capital_paraiba(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2507507]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/paraiba.html', dados)


def capital_parana(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[4106902]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/parana.html', dados)


def capital_pernambuco(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2611606]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/pernambuco.html', dados)


def capital_piaui(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2211001]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/piaui.html', dados)


def capital_riodejaneiro(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[3304557]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/riodejaneiro.html', dados)


def capital_riograndedonorte(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2408102]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/riograndedonorte.html', dados)


def capital_riograndedosul(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[4314902]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/riograndedosul.html', dados)


def capital_rondonia(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1100205]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/rondonia.html', dados)


def capital_roraima(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1400100]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/roraima.html', dados)


def capital_santacatarina(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[4205407]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/santacatarina.html', dados)


def capital_saopaulo(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[3550308]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/saopaulo.html', dados)


def capital_sergipe(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[2800308]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/sergipe.html', dados)


def capital_tocantins(request):
    dados = {
        'pop_2021': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2021']):,}".replace(',', '.'),
        'pop_2020': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2020/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2020']):,}".replace(',', '.'),
        'pop_2019': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2019/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2019']):,}".replace(',', '.'),
        'pop_2018': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2018/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2018']):,}".replace(',', '.'),
        'pop_2017': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2017/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2017']):,}".replace(',', '.'),
        'pop_2016': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2016/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2016']):,}".replace(',', '.'),
        'pop_2015': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2015/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2015']):,}".replace(',', '.'),
        'pop_2014': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2014/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2014']):,}".replace(',', '.'),
        'pop_2013': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2013/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2013']):,}".replace(',', '.'),
        'pop_2012': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2012/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2012']):,}".replace(',', '.'),
        'pop_2011': f"{int(requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2011/variaveis/9324?localidades=N6[1721000]').json()[0]['resultados'][0]['series'][0]['serie']['2011']):,}".replace(',', '.')
    }
    return render(request, 'capitais/tocantins.html', dados)
