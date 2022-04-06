# PRUEBA TECNICA LA HAUS

# Inicio IAC Cloud Formation
 
* Se inicia la creacion Infraestructura como codigo con la creacion de ECR.

![ResourcesInfra](https://user-images.githubusercontent.com/39314757/161884981-1f338ba8-1cf1-4589-a5b2-70200342896b.png)


![AzureInfra](https://user-images.githubusercontent.com/39314757/161885373-f9ccbfc2-fde2-4953-9773-d8cbf504188b.png)


![Cloud Formation](https://user-images.githubusercontent.com/39314757/161883807-f7420a27-fcf1-40f4-9451-cdc6bf990967.png)

# Cambios en el codigo

* Inicialmente se creo la tabla para la DB.

@app.before_first_request
def create_tables():
   db.create_all()
   
* Se agrega una linea para setear una variable.

os.environ['APP_SETTINGS']="config.DevelopmentConfig"

# Plataforma - Provedor de nube utilizado

* AWS

# Servicio disponible a través:

* Falto crear el Certificado-Dominio y asi poder exponer el API por servicio https.

* http://lahauslb-1955411172.us-east-1.elb.amazonaws.com/

![DNS](https://user-images.githubusercontent.com/39314757/161889168-8c443286-45ae-422a-b0e3-2b214982f119.png)

# CI - CD

![CI-CD](https://user-images.githubusercontent.com/39314757/161886125-96bfb6a6-c984-4e79-ba31-8a49a84e6533.png)

# Monitoreo

* CloudWatch Servicio

![Monitoreo](https://user-images.githubusercontent.com/39314757/161889702-9d0ba170-1e9c-4e32-8a37-ed799002ff72.png)

* Logs

![LogsServicio](https://user-images.githubusercontent.com/39314757/161889811-c6104c19-12a0-46df-bf76-400a806256a5.png)



