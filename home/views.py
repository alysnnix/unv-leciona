from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from home.models import Professor, Turma, Segmento, Periodo
from ocorrencia.models import Professor_Ausente, Professor_Substituto
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractIsoWeekDay
from django.utils import timezone
import datetime
import calendar
import json

class DashboardView(TemplateView):
    template_name = 'home/line_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Estatísticas Reais
        context['professores_count'] = Professor.objects.count()
        context['turmas_count'] = Turma.objects.count()
        context['segmentos_count'] = Segmento.objects.count()

        # 2. Lógica Gráfico de Barras (Faltas por Dia da Semana)
        # IsoWeekDay: 1=Segunda, 2=Terça, ..., 7=Domingo
        faltas_por_dia = Professor_Ausente.objects.annotate(
            dia_semana=ExtractIsoWeekDay('inicio')
        ).values('dia_semana').annotate(total=Count('id')).order_by('dia_semana')
        
        # Iniciar dicionário com todos os dias zerados
        dias_uteis = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} # Segunda a Sexta
        for f in faltas_por_dia:
            if f['dia_semana'] in dias_uteis:
                dias_uteis[f['dia_semana']] = f['total']
                
        context['bar_labels'] = json.dumps(["Segunda", "Terça", "Quarta", "Quinta", "Sexta"])
        context['bar_data'] = json.dumps(list(dias_uteis.values()))
        
        # 3. Lógica Gráfico de Rosca (Turmas por Período)
        turmas_por_periodo = Turma.objects.values('periodo__nome').annotate(total=Count('id'))
        
        pie_labels = []
        pie_data = []
        for t in turmas_por_periodo:
            nome_periodo = t['periodo__nome'] if t['periodo__nome'] else "Sem Período"
            pie_labels.append(nome_periodo)
            pie_data.append(t['total'])
            
        context['pie_labels'] = json.dumps(pie_labels if pie_labels else ["Sem Dados"])
        context['pie_data'] = json.dumps(pie_data if pie_data else [1])
        
        return context

class LineChartJSONView(BaseLineChartView):
    
    def get_months_data(self):
        # Pega o ano atual
        ano_atual = timezone.now().year
        
        # Faltas por mês no ano atual
        faltas = Professor_Ausente.objects.filter(inicio__year=ano_atual).annotate(
            mes=ExtractMonth('inicio')
        ).values('mes').annotate(total=Count('id')).order_by('mes')
        
        # Substituições por mês no ano atual
        subs = Professor_Substituto.objects.filter(inicio__year=ano_atual).annotate(
            mes=ExtractMonth('inicio')
        ).values('mes').annotate(total=Count('id')).order_by('mes')
        
        # Inicializa lista de 6 meses (Janeiro a Junho por ex, ou últimos 6)
        # Para simplificar, vamos mostrar do mês 1 ao 6 do ano atual, ou 6 meses dinâmicos
        mes_atual = timezone.now().month
        meses_lista = []
        labels = []
        
        # Calcula os últimos 6 meses até o atual
        for i in range(5, -1, -1):
            m = mes_atual - i
            if m <= 0:
                m += 12 # Corrige para o ano anterior se for o caso
            meses_lista.append(m)
            # Converte número do mês para nome em português
            nome_mes = {
                1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
            }.get(m, str(m))
            labels.append(nome_mes)
            
        # Preenche os dados
        dados_faltas = [0] * 6
        dados_subs = [0] * 6
        
        for f in faltas:
            if f['mes'] in meses_lista:
                idx = meses_lista.index(f['mes'])
                dados_faltas[idx] = f['total']
                
        for s in subs:
            if s['mes'] in meses_lista:
                idx = meses_lista.index(s['mes'])
                dados_subs[idx] = s['total']
                
        return labels, dados_faltas, dados_subs

    def get_labels(self):
        labels, _, _ = self.get_months_data()
        return labels

    def get_providers(self):
        return ["Faltas Registradas", "Substituições Realizadas"]

    def get_data(self):
        _, faltas, subs = self.get_months_data()
        return [
            faltas,
            subs
        ]

line_chart = DashboardView.as_view()
line_chart_json = LineChartJSONView.as_view()