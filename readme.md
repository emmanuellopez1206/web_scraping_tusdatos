# Prueba desarrollador TusDatos

Versión de python - 3.9

## Configuración de proyecto
1. Clonar el repositorio por protocolo https:
```bash
https://github.com/emmanuellopez1206/web_scraping_tusdatos.git
```
2. Instalar virtualenv:
```bash
pip install virtualenv
```
3. Crear entorno virtual:
```bash
virtualenv venv
```
4. Activar entorno virtual en powershell:
```bash
.\venv\Scripts\activate.ps1
```
5. Instalar requerimientos:
```bash
pip install -r .\requirements.txt
```
6. Al completar los pasos anteriores puedes proceder a ejecutar el proyecto con el siguiente comando y acceder a usar la API en http://localhost:8001/docs:
```bash
uvicorn main:app --reload --port 8001
```
## Detalles del proyecto
Para el desarrollo de este proyecto decidí usar fastAPI debido a que este framework cuenta con múltiples beneficios como por ejemplo un excelente rendimiento por lo que permite manejar un alto número de solicitudes simultáneamente, lo cual es ideal para tareas de web scraping que pueden involucrar múltiples peticiones. Posee también soporte para operaciones asíncronas usanso "async" para tareas de I/O y su gran escalibidad puede ser aprovechable para futuras mejoras del proyecto. También usé Background Tasks de fastApi para lograr ejecutar tareas en segundo plano y así no tener que estar esperando a que se complete la operación antes de recibir la respuesta.
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/81779e52-6d3a-45ad-9929-583dd5b61aaa)


Para el modelo de la base de datos se realiza un análisas de la información que se necesita extraer y detecté que la información está segmentada por distintos grupos de listas, por lo que se crea una tabla para cada grupo y así se asegura recopilar toda la información suministrada por la página y mantener la integridad de la misma. Además, uso el ORM SQLAlchemy ya que simplifica la interacción con la base de datos y ofrece una capa de protección para evitar sql injection.
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/49b4c6cc-7295-4896-b3b2-3f24b33ecfe9)

Para el almacenamiento de la información usé la base de datos embedida SQLite debido a que su funcionamiento es muy práctico y no requiere configuración previa, lo que facilita el proceso de correr el proyecto y evaluar la prueba.
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/03a70fb2-b71b-48ff-a869-a8f9569a2090)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/c427f472-e295-476c-8dd8-35d6c3503106)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/0798736b-ac40-41cc-a5c7-0072c8b714e4)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/7786b8c5-65d2-445f-a978-8062d262395d)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/e295dcd2-c08b-49fa-8ddd-9a47f3c6b466)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/c54f1554-c6e9-4c83-9112-a0d7f4eb77ff)


Para los controladores intenté implementar el patrón de diseño llamado strategy creando la clase abstracta "ScrapperCreation" la cual define la estructura básica para algunos procesos de scrapeo, incluyendo el payload común y un atributo process_execute para diferenciar los tipos de procesos. Y las Clases Concretas "ScrapperActor" y "ScrapperDemandado" heredan de "ScrapperCreation" y definen estrategias específicas de scraping para actores y demandados.
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/3c0a1c28-a69e-4b01-be4e-26a65a3ed82e)

También, implementé un debbuger para facilitar el proceso de desarrollo logrando realizar las validaciones locales mediante una depuración paso a paso y así alcanzar una identificación rápida de errores. Agregando a lo anterior, se implementan una serie de logs para identificar en qué etapa se encuentra el proceso de scraping.
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/6bfb577c-ea7d-48da-9916-4ba8e5c88268)
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/df19719a-ec11-4eb4-8e58-8690837db849)


Por último se implementan distintos tests para garantizar el correcto funcionamiento del proyecto y verificar su rendimiento. Con el siguiente comando podrás ejecutar los tests:
```bash
pytest -vv
```
![image](https://github.com/emmanuellopez1206/web_scraping_tusdatos/assets/104656284/3f7cbf83-d604-4ad7-9d24-ffa41181e502)
