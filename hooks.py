import aiofiles, csv


async def mk_csv_file(_urls: list):
    async with aiofiles.open('tmp/file_url.csv', "w+") as csvfilerr:
        head_file = ['URL']
        write_csv = csv.DictWriter(csvfilerr, fieldnames=head_file)
        await write_csv.writeheader()

        for url in _urls:
            await write_csv.writerow({"URL": url})
