import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def read_sheets(CREDENTIALS_FILE):
    """Функция чтения данных из Google Sheets."""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
                                                                   'https://www.googleapis.com/auth/spreadsheets', 
                                                                   'https://www.googleapis.com/auth/drive'
                                                                   ])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheetId = '12LmlEuUAS96BQ2-QH0cA88vtanNCxI_FB79Xgfi3XHc'
    ranges = ["Лист номер один!A2:Z999"]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    return sheet_values
