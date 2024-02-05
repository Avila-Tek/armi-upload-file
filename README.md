# Guía para carga masiva de productos via archivos CSV

## Requesitos

Para utilizar este script es necesario contar con:

- [python](https://www.python.org/downloads/) versión `>= 3.7`,
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) ultima versión
- [pip](https://pip.pypa.io/en/stable/installation/)
<!-- - [boto3](https://aws.amazon.com/es/sdk-for-python/) -->

## Primeros pasos

Una vez instalado las herramientas de trabajo (python, venv y pip), entonces podrá activar el ambiente virtual que esta dentro de este proyecto utilizando el siguiente comando:

### Activar venv

> En Linux o en MacOS ejecute en una ventana de terminal

```bash
source armi/bin/activate
```

> En windows ejecute en una ventana de powershell

```ps
.\armi\Scripts\activate
```

Para asegurarse que todo ha funcionado correctamente ejecute:

```bash
which python3
```

Debería ver algo asi com resultado:

```text
/Users/zoomelectrico/Documents/avilatek/armi-auto/armi/bin/python3
```

### Instalar librerias

Para instalar las librerias necesarias deberá ejecutar el siguiente comando

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

Abra en el editor de código de su preferencia el archivo .env (si no existe creelo) y agrege las variables que fueron sumistradas por correo y/o las variables necesarias para lograr la conexión con su base de datos.

```config
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_REGION="nyc3"
AWS_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com"
S3_BUCKET_NAME="armi"
ARMI_STORE_ID=""
# BASE DE DATOS
DATABASE_TYPE=""
DBAPI=""
ENDPOINT=""
DBUSER=""
DBPASSWORD=""
PORT=""
DATABASE=""
```

Las variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `AWS_ENDPOINT_URL`,`S3_BUCKET_NAME` y `ARMI_STORE_ID` fueron enviadas por correo eléctronico a su persona. Por favor, sea cuidados con estas variables porque son secretos de ambiente, no las publique en ningún repositorio público.

Con respecto a las variables restantes a continuación una tabla de descripción:

|    Nombre     | Descripción                                                                          | Posibles Valores  |
| :-----------: | :----------------------------------------------------------------------------------- | ----------------- |
| DATABASE_TYPE | Este es el nombre del motor de base de datos que se utilice                          | postgresql, mssql |
|     DBAPI     | Este es el nombre del driver de python utilizado para conectarse con la db           | psycopg2, pyodbc  |
|   ENDPOINT    | Este es el url coneción para conectarse con la db                                    |                   |
|    DBUSER     | Este es el nombre de usuario de la db                                                |                   |
|  DBPASSWORD   | Este es la contraseña del usuario de la db, debe encodearse los caracteres especiale |                   |
|     PORT      | Este es el puerto que escucha la base de datos                                       |                   |
|   DATABASE    | Este es el nombre del puerto de la db                                                |                   |

Puede revisar mas información sobre el tipo de base de datos y el driver [acá](https://docs.sqlalchemy.org/en/20/dialects/index.html)

## Uso del script

Para usar el script, es necesario entonces ir a la linea 49 y cambiar el valor de la variables `sql_query` por el query de sql que se vaya a ejecutar, de manera que el programa pueda conectarse a la base de datos y crear un archivo de csv para subir al bucket de s3.

## Ejecución del script

Para ejecutar el script, solamente es necesario ejecutar el comando:

```bash
python3 ./upload-products.py
```

Dentro de la carpeta raiz para que entonces el script se puede conectar a la db producir el csv y subirlo a s3 de esta manera es posible cumplir el objetivo

## Ejecución periodica

Puedes utilizar la herramienta `crontab` para crear un cronjob que se ejecute cada hora, para ellos consulte [crontab guru](https://crontab.guru/) para revisar su expresión y utilice [python-crontab](https://pypi.org/project/python-crontab/) para configurar un script que se encargue de ejecutar periodicamente el script `upload-products.py`
