from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from home.models import Professor, Turma, Segmento
import json

class DashboardView(TemplateView):
    template_name = 'home/line_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Estatísticas reais do banco (se estiver vazio, retorna 0)
        context['professores_count'] = Professor.objects.count()
        context['turmas_count'] = Turma.objects.count()
        context['segmentos_count'] = Segmento.objects.count()

        # Dados para o Gráfico de Barras (Ocorrências por Dia)
        context['bar_labels'] = json.dumps(["Segunda", "Terça", "Quarta", "Quinta", "Sexta"])
        context['bar_data'] = json.dumps([12, 19, 3, 5, 2])
        
        # Dados para o Gráfico de Rosca (Distribuição de Turmas por Período)
        context['pie_labels'] = json.dumps(["Manhã", "Tarde", "Integral"])
        context['pie_data'] = json.dumps([45, 35, 20])
        
        return context

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]

    def get_providers(self):
        return ["Faltas Registradas", "Substituições Realizadas"]

    def get_data(self):
        return [
            [12, 8, 4, 15, 9, 5],  # Faltas
            [10, 7, 3, 14, 8, 4]   # Substituições
        ]

line_chart = DashboardView.as_view()
line_chart_json = LineChartJSONView.as_view()