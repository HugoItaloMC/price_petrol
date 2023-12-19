import pandas as pd
from bokeh.plotting import figure, save, output_file
from bokeh.models import ColumnDataSource


class PipePlotting:

    def __init__(self, _frame: str):
        self._frame = pd.read_excel(_frame)
        self.base_munucipio: list = []
        self.base_preco_med: list = []
        self.base_preco_min: list = []
        self.base_preco_max: list = []

    async def _upload_data(self):
        _municipio = self._frame['Unnamed: 3']
        _preco_med = self._frame['Unnamed: 7']
        _preco_min = self._frame['Unnamed: 9']
        _preco_max = self._frame['Unnamed: 10']
        await self._slice_column(column=_municipio, op='municipio')
        await self._slice_column(column=_preco_med, op='preco_med')
        await self._slice_column(column=_preco_min, op='preco_min')
        await self._slice_column(column=_preco_max, op='preco_max')

    async def _slice_column(self, column, op: str):
        for line in range(0, len(column)):
            if op == 'municipio':
                self.base_munucipio.append(next(map(str, (line for line in column[line::-1]))))
            elif op == 'preco_med':
                self.base_preco_med.append(next(map(str, (line for line in column[line::-1]))))
            elif op == 'preco_min':
                self.base_preco_min.append(next(map(str, (line for line in column[line::-1]))))
            elif op == 'preco_max':
                self.base_preco_max.append(next(map(str, (line for line in column[line::-1]))))
            else:
                raise AttributeError('Attr not function')

    async def _push_data(self) -> tuple:
        _base: list = []
        await self._upload_data()
        for line in range(0, len(self.base_munucipio)):
            _base.append((self.base_munucipio[line], self.base_preco_med[line], self.base_preco_min[line], self.base_preco_max[line]))
        yield _base

    async def plot_data_view(self):
        datas_base = self._push_data()
        municipio_: set = set()
        preco_med: list = []
        preco_min: list = []
        preco_max: list = []
        municipio: list = []

        async for lines in datas_base:  # yield
            for line in lines:  # list
                if line[0] not in municipio_:
                    municipio_.add(line[0])
                    municipio.append(line[0])
                    preco_med.append(line[1])
                    preco_min.append(line[2])
                    preco_max.append(line[3])

        # Origin Data to Bokeh
        col_source_preco_med = ColumnDataSource(data=dict(municipios=municipio, preco_medio=preco_med))
        col_source_preco_min = ColumnDataSource(data=dict(municipios=municipio, preco_min=preco_min))
        col_source_preco_max = ColumnDataSource(data=dict(municipios=municipio, preco_max=preco_max))

        # Image data view bokeh
        _figure_preco_med = figure(y_range=municipio[1::],
                                   title='Preco Médio Gasolina',
                                   toolbar_location=None,
                                   tools='')

        _figure_preco_min = figure(y_range=municipio[1::],
                                   title='Preco Minimo Gasoline',
                                   toolbar_location=None,
                                   tools='')

        _figure_preco_max =  figure(y_range=municipio[1::],
                                    title='Preco Maximo Gasolina',
                                    toolbar_location=None,
                                    tools='')
        # Gerando Gráficos

        # Preco Médio
        _figure_preco_med.hbar(y='municipios',
                               right='preco_medio',
                               height=0.5,
                               source=col_source_preco_med,
                               color='skyblue')
        _figure_preco_med.xaxis.axis_label = 'Preco Médio Gasolina por Municipio'
        _figure_preco_med.yaxis.axis_label = 'Municipio'

        # Salvar o gráfico em HTML interativo Preco Médio
        output_file('templates/src/assets/preco_medio.html')
        save(_figure_preco_med)

        # Preco Min
        _figure_preco_min.hbar(y='municipios',
                               right='preco_min',
                               height=0.5,
                               source=col_source_preco_min,
                               color='skyblue')

        # Nomeando Gráfico
        _figure_preco_min.xaxis.axis_label = 'Preco Minimo Gasolina por Municipio'
        _figure_preco_min.yaxis.axis_label = 'Municipio'

        #  Salvando gráfico interativo preco minimo
        output_file('templates/src/assets/preco_min.html')
        save(_figure_preco_min)

        # Preco Max
        _figure_preco_max.hbar(y='municipios',
                               right='preco_max',
                               height=0.5,
                               source=col_source_preco_max,
                               color='skyblue')

        # Nomeando Gráfico
        _figure_preco_max.xaxis.axis_label = 'Preco Máximo Gasolina por Municipio'
        _figure_preco_max.yaxis.axis_label = 'Municipio'
        # Salvando Gráfico interativo HTML preco max
        output_file('templates/src/assets/preco_max.html')
        save(_figure_preco_max)
