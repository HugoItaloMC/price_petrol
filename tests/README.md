# Documentação de Testes Utilizando cProfile e SnakeViz

_Este documento descreve o processo de teste do projeto utilizando o módulo nativo do Python, cProfile, para realizar a análise de desempenho dos arquivos .py. Além disso, será utilizado o SnakeViz como visualizador para as informações geradas pelo cProfile.
Configuração do Ambiente de Testes_
 - `cProfile:` É um módulo da biblioteca padrão do Python que fornece um profiler de desempenho, ou seja, uma ferramenta que ajuda a medir e analisar o desempenho de um programa. O nome "cProfile" refere-se a "profiling em C", indicando que o módulo é implementado em C para minimizar o impacto no desempenho durante a coleta de estatísticas.
    - #### Principais Características do cProfile:
        - Medição de Tempo de Execução:
            
          _O cProfile mede o tempo de execução de cada função no código, fornecendo estatísticas detalhadas sobre quanto tempo cada função consome durante a execução do programa._

        - Hierarquia de Chamadas:
            
            _Além do tempo total, o cProfile gera uma hierarquia de chamadas, mostrando como as funções estão inter-relacionadas, ou seja, quais funções chamam outras e quanto tempo é gasto em cada uma delas._

        - Modo de Saída:
            
            _Pode ser executado em dois modos principais: em linha de comando, onde as estatísticas são impressas diretamente no console, ou em modo de arquivo, onde as estatísticas são salvas em um arquivo para análise posterior._



 - `snakeviz:` Utilizado para visualização de perfis cProfile.

__Certifique-se de que o ambiente de desenvolvimento esteja configurado com as dependências necessárias para os testes. Os requisitos específicos para os testes são:__

    

    $ pip install -r REQUIREMENTS.txt



## Execução dos Testes Unitários

Antes de iniciar a análise de desempenho, é recomendável executar os testes unitários individualmente para garantir que cada componente do projeto esteja funcionando conforme o esperado.



    $ python3 tests/test_pipe.py


## Análise de Desempenho com cProfile

Para realizar a análise de desempenho utilizando cProfile, execute os seguintes comandos para cada arquivo .py do projeto:

    $ python3 -m cProfile -o stats_test_pipe.profile tests/test_pipe.py

Esses comandos gerarão arquivos de perfil com extensão .profile, como `stats_test_pipe.profile`, contendo informações detalhadas sobre o desempenho de cada script.

## Visualização com SnakeViz
Utilize o SnakeViz para visualizar as informações geradas pelos arquivos .profile:
    

    # snakeviz stats_test_pipe.profile

__Isso abrirá uma interface gráfica no navegador padrão, permitindo uma análise interativa e detalhada do desempenho do código.__