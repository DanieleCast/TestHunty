# TestHunty
Test for Hunty

## Gracias por la prueba, me divertí mucho, lamento no haber tenido el tiempo para finalizarla, seguro la terminaré como ejercicio personal.

Para la parte 1 faltó afinar la data del **office_modality.json** en su columna **disponibility**. ya que el formato 
["ApplicationForm", "P2P"] se debe cambiar por "['ApplicationForm', 'P2P']".

La función `get_json_gcs`  obtiene la data del bucket y lista todos los archivos en él.

`make_data` por su parte organiza el json, obteniendo los headers y la data, poniéndolos en el formato aceptado por la API de Google Sheets.

Finalmente se hace uso de las librerías de la API para crear y escribir la data en el spreedsheet. 
