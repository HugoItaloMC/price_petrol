# . Documentação do Projeto
##### Este documento fornece uma visão geral da estrutura do projeto, detalhando as pastas, pacotes e seus respectivos conteúdos.


### Estrutura do Projeto
#### O projeto está organizado em diferentes diretórios que desempenham papéis específicos no ambiente de desenvolvimento e execução. A seguir, descrevemos cada um desses diretórios e seu conteúdo.

- `lib/` A pasta lib/ contém o ambiente Conda utilizado no projeto. Esse ambiente é criado com o seguinte comando:
   
    
     conda create --prefix lib/

As dependências necessárias, como pandas e selenium, são instaladas com o comando:



    conda install --prefix lib/ pandas selenium

### Após o ambiente criado e instalado as dependências execute o seguinte comando ativar o ambiente
    conda activate lib/

# Inicie o anaconda-project

 ````
    Com o ambiente conda iniciado e anaconda-project instalado no ambiente
 vamos iniciar o projeto para execucão dos scripts python, execute o comando:
    
    anaconda-project init -y
    
  Agora adicione os pacotes ao anaconda-project com os seguintes comandos:
    
    anaconda-project add-packages pkg1, pkg2
 ````

- `envs/` A pasta envs/ é gerada automaticamente no diretório do projeto após a execução do comando:


    anaconda-project add-command --type unix --support-http-options application "params to command"

- `tmp/:` Contém o arquivo file_response_html.html gerado pelo subprocesso "curl".


- `src/` A pasta src/ contém Objetos descritores e handlers Python do projeto:
  - `src/commons.py` Contém objetos descritores das tarefas executadas em app/apps.py
  - `src/handlers.py` Objetos controladores de objetos em toda aplicacão


- `app/` Contém módulos python responsável por tarefas da aplicacão
  - `app/pipe.py:` Possíveis funcionalidades relacionadas a processos de pipeline, se aplicável ao seu projeto.
  - `app/apps.py` Gerando aplicacões dos objetos contidos em pipe.py 


- `hooks.py:` Contém funções de apoio que são utilizadas pelos outros scripts.
- `main.py:` Implementa funcionalidades relacionadas a filas, se aplicável ao seu projeto.
- `run.py:` Este script é o ponto de entrada principal que executa as tarefas principais do programa.
- `.env:` Arquivo que contém variáveis de ambiente necessárias para a execução do programa.

- `anaconda-project.yml` O arquivo anaconda-project.yml contém as configurações padrão do ambiente do Anaconda, inicializado com o comando:
  
  
     anaconda-project init

