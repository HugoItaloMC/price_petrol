import pstats

import csv, subprocess, os, shlex, asyncio
from dotenv import load_dotenv

from bs4 import BeautifulSoup

from test_helper import mk_csv_file


class ProcessAssets:

    # Tarefas no Sistema

    @staticmethod
    async def _mk_folder(path):
        """
        Corotina para criar um diretório se ele não existir.

        Parameters:
            - path (str): O caminho para o diretório que se deseja criar.

        Esta corotina verifica se o diretório especificado pelo caminho 'path' já existe.
        Se não existir, cria o diretório juntamente com todos os diretórios intermediários necessários.

        Notas:
            - Este método é estático e pertence à classe Core, e deve ser chamado como `Core._mk_folder(path)`.
            - Utiliza a função `os.makedirs()` para criar o diretório recursivamente.

        Args:
            - path: Uma string representando o caminho para o diretório a ser criado.

            Raises:
            - OSError: Se ocorrerem erros ao tentar criar o diretório.

            Exemplo de Uso:
            ```
            await Core._mk_folder('/caminho/para/novo/diretorio')
            ```

        Isso criará o diretório 'novo' dentro de 'diretorio' e todos os diretórios intermediários, caso ainda não existam.
        """

        if not os.path.exists(path):
            os.makedirs(path)

    async def _environ(self):
        """
          Criação de arquivos e pastas no sistema.

          Esta função executa uma série de ações para manipular o sistema de arquivos:
          1. Obtém o diretório base do usuário (home_dir) e define um diretório de trabalho (work_dir).
          2. Navega para o diretório de trabalho.
          3. Cria uma pasta temporária dentro do diretório de trabalho.
          4. Verifica a existência de um arquivo chamado 'response_body.html' na pasta temporária e o cria se não existir.
          5. Retorna a concatenação das variáveis de ambiente 'COMMAND' e 'URL'.

          Notas:
          - É importante que as variáveis de ambiente 'COMMAND' e 'URL' estejam configuradas no arquivo .env.
          - Esta função utiliza os módulos os, os.path e dotenv para manipular o sistema de arquivos e carregar variáveis de ambiente.

          Return:
          - Uma string que representa a concatenação das variáveis 'COMMAND' e 'URL', as quais serão utilizadas posteriormente.

          Raises:
          - KeyError: Se 'HOME' não estiver definido no ambiente ou se 'COMMAND' ou 'URL' não estiverem configurados no arquivo .env.
          - OSError: Se ocorrerem erros ao tentar manipular o sistema de arquivos, como criar pastas ou arquivos.
          """
        home_dir = os.environ['HOME']
        work_dir = os.path.join(home_dir, os.getcwd() + '/tests')
        os.chdir(work_dir)
        await ProcessAssets._mk_folder(os.path.join(work_dir, 'tmp'))
        os.chdir(work_dir + '/tmp')
        if not os.path.exists(os.path.join(os.getcwd(), 'response_body.html')):
            os.mknod(os.path.join(os.getcwd(), 'response_body.html'))

        os.chdir(work_dir)

        load_dotenv()

        COMMAND=os.getenv('COMMAND') + os.getenv('URL')
        return COMMAND

    async def _process(self):
        """
            Executa um subprocesso para realizar uma solicitação HTTP e buscar o código HTML de uma página web.

            Este método cria um subprocesso para executar um comando de shell com base na URL e no comando fornecidos
            pelas variáveis de ambiente. O objetivo é buscar o código HTML de uma página da web que contenha URLs
            de arquivos .xlsx.

            Returns:
            - None: Este método não retorna nenhum valor diretamente, mas executa o subprocesso para buscar o HTML.

            Notes:
            - O método utiliza a função `_environ()` para obter a concatenação das variáveis de ambiente que
            fornecem o comando a ser executado e a URL a ser consultada.
            - Utiliza as bibliotecas `asyncio` e `subprocess` para criar e executar o subprocesso.

            Raises:
            - OSError: Se ocorrerem erros durante a execução do subprocesso.

            Example:
            ```python
            await self._process()
            ```
            Isso inicia o subprocesso para realizar a solicitação HTTP e buscar o código HTML da página web.
            """
        COMMAND = shlex.split("%s" % await self._environ())
        _process = await asyncio.create_subprocess_exec(*COMMAND,
                                                        stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE)
        await _process.communicate()

    async def get_(self):
        """Método para acionar o processo de busca do código HTML de uma página web.

           Este método atua como um acionador para o processo de busca do código HTML de uma página da web que contém
           URLs de arquivos .xlsx. Ele chama internamente o método '_process()' para iniciar o subprocesso de busca.

           Returns:
           - None: Não retorna nenhum valor diretamente, mas inicia o processo de busca do código HTML.

           Example:
           ```python
           await self.get_()
           ```
           Este método é usado para iniciar o processo de busca do código HTML da página web.
           ```"""

        await self._process()



class ParserAssets:
    # Analisador do código html da página web requisitada

    async def _parser_html(self, _parser_file):
        """Extrai links de arquivos .xlsx de um arquivo HTML de uma página web.

        Parameters
        ----------
        _parser_file : str
            Arquivo HTML da página web contendo links para arquivos .xlsx.

        Returns
        -------
            None

        Esta corotina recebe o caminho para um arquivo HTML de uma página web e extrai os links associados aos arquivos
        .xlsx presentes nesse arquivo. Utiliza a biblioteca BeautifulSoup para fazer o parsing do HTML e identificar os
        links de interesse. Posteriormente, chama a função `mk_csv_file()` para criar um arquivo CSV a partir desses links.

        Notes
        -----
            - O parâmetro '_path_file' deve ser o caminho completo para o arquivo HTML da página web.
            - Utiliza a biblioteca BeautifulSoup para análise e extração dos links do HTML.
            - Chama a função `mk_csv_file()` para criar um arquivo CSV com os links extraídos.

        Raises
        ------
            Any exceptions raised by the operations within the function will be propagated.

        Example
        -------
        ```python
            await self._parse_html('/caminho/para/arquivo.html')
        ```
        Este método é utilizado para extrair links de arquivos .xlsx de um arquivo HTML da página web e criar um arquivo CSV
        com esses links.
        ``` """
        URL: list = []

        soup = BeautifulSoup(_parser_file, 'html.parser')
        _tag = soup.select('a.internal-link')

        for href in _tag:
            URL.append(href['href'])

        await mk_csv_file(URL)

    async def get_(self):
        if not os.path.exists(os.path.join(os.getcwd(), 'tests/tmp')):
            _process = ProcessAssets()
            await _process.get_()

        with open('tests/tmp/response_body.html', 'r+') as htmlfile:
            await self._parser_html(htmlfile)


class WorkFlow:

    def _process_assets(self):
        return ProcessAssets()

    def _parser_assets(self):
        return ParserAssets()

    def pipe(self, prompt):

        if prompt.lower() == 'process':
            try:
                return self._process_assets()
            except AttributeError:
                prompt = 'process'
                prompt.lower()

        elif prompt.lower() == 'parser':
            try:
                return self._parser_assets()
            except AttributeError:
                prompt = 'parser'
                prompt.lower()


if __name__ == '__main__':
    # Tests unitário objeto ParserAssets()
    # Buscar arquivo HTML: OK
    # Analisar arquivo, buscar seletores CSS: OK
    # Incurcionar entre ficheiros: OK
    # Gerar arquivo CSV no diretório principal e inserir dados no arquivo: OK
    parser = ParserAssets()
    asyncio.run(parser.get_())
