# Necessary libraries
from googleapiclient.discovery import build
from google.cloud import storage
import create
import json
import google.auth


credentials, project = google.auth.default()  
#List buckets using the default account on the current gcloud cli
client = storage.Client(credentials=credentials)
#buckets = client.list_buckets()

#for bucket in buckets:
#    print(bucket) 

#Reading data in json file
def get_json_gcs(bucket_name, file_name):
    # create storage client
    client = storage.Client()
    # get bucket with name
    BUCKET = client.get_bucket(bucket_name)
    # get the blob
    blob = BUCKET.get_blob(file_name)

    files = client.list_blobs(bucket_name)
    print(f'Tus archivos en el {bucket_name} son:')
    # Note: The call returns a response only when the iterator is consumed.
    for file_ in files:
        print(file_.name)
    print('')
    # load blob using json
    file_data = json.loads(blob.download_as_string())
    return file_data

#Transforming the data to Google Sheets API Values Format. 
def make_data(json_object):
    new_list = []
    headers = list(json_object[1].keys())
    new_list.append(headers)

    for i in range(len(json_object)):
        k = list(json_object[i].values())
        new_list.append(k)
    return new_list

bucket_name = "json_files_bucket"
file_name = "tamaño_empresas.json"
json_data = get_json_gcs(bucket_name, file_name)

data = make_data(json_data)
print(data)

spreadsheet = {
            'properties': {
                'title': "HuntySheet"
            }
        }


range_ = "A1:E6"
value_input_option = "USER_ENTERED"
value_range_body = {
  "range": "A1:E6",
  "majorDimension": "ROWS",
  "values": data,
}

service = build('sheets', 'v4', credentials=credentials)
spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
spreadsheet_id = spreadsheet.get('spreadsheetId')

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()
