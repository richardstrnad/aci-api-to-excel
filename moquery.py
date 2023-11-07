import aciClient
import logging
import os
import xlsxwriter

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CLASS = 'ethpmFcot'
FILTER = 'ne(ethpmFcot.guiCiscoPID,"")'
ATTRIBUTES = ['dn', 'guiCiscoPID', 'guiSN']

def login() -> aciClient.ACI:
    apic = os.getenv("APIC")
    apic_user = os.getenv("APIC_USER")
    apic_password = os.getenv("APIC_PASSWORD")

    if apic is None or apic_user is None or apic_password is None:
        logger.error("APIC, APIC_USER, and APIC_PASSWORD must be set in the environment")
        exit(1)

    aciclient = aciClient.ACI(apic, apic_user, apic_password, refresh=False)
    aciclient.login()

    return aciclient

def main():
    load_dotenv()

    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    aciclient = login()
    req = f'class/{CLASS}.json'
    if FILTER != '':
        req += f'?query-target-filter={FILTER}'

    result = aciclient.getJson(req)

    row = 0
    for r in result:
        data = r.get(CLASS).get("attributes")
        col = 0
        for attr in ATTRIBUTES:
            worksheet.write(row, col, data.get(attr))
            col += 1

        row += 1

    workbook.close()
    aciclient.logout()

if __name__ == "__main__":
    main()
