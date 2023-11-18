import csv
import os
import pstats
import aiofiles



async def pool_queue(queue, _class):
    await queue.put(_class)


async def mk_csv_file(_urls: list):
    """
        Cria um arquivo CSV contendo URLs fornecidos.

        Parameters
        ----------
        _urls : list
            Lista de URLs a serem escritos no arquivo CSV.

        Returns
        -------
        None

        Esta corotina cria um arquivo CSV chamado 'file_url.csv' no modo de escrita e escreve os URLs fornecidos
        nesta lista. Utiliza a biblioteca aiofiles para operações assíncronas de E/S.

        Notes
        -----
        - O parâmetro '_urls' deve ser uma lista de URLs a serem escritos no arquivo CSV.
        - O arquivo CSV terá uma coluna chamada 'URL'.
        - Utiliza a biblioteca aiofiles para operações assíncronas de leitura/escrita de arquivos.

        Raises
        ------
        Any exceptions raised by the operations within the function will be propagated.

        Example
        -------
        ```python
        await mk_csv_file(['http://example.com/file1.xlsx', 'http://example.com/file2.xlsx'])
        ```
        Este método é utilizado para criar um arquivo CSV chamado 'file_url.csv' contendo os URLs fornecidos.
        ```
    """
    async with aiofiles.open('file_url.csv', 'w+', newline='') as csvfile:
        head_file: list = ['URL']
        write_csv = csv.DictWriter(csvfile, fieldnames=head_file)
        await write_csv.writeheader()

        for url in _urls:
            await write_csv.writerow({"URL": url})

