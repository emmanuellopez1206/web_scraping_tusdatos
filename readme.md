# Prueba desarrollador TusDatos

Versión de python - 3.9

## Configuración de proyecto
1. Clonar el repositorio por protocolo https
```bash
https://github.com/emmanuellopez1206/web_scraping_tusdatos.git
```
2. Instalar virtualenv
```bash
pip install virtualenv
```
3. Crear entorno virtual
```bash
virtualenv venv
```
4. Activar entorno virtual en powershell
```bash
.\venv\Scripts\activate.ps1 
```
5. Instalar requerimientos
```bash
pip install -r requeriments.txt
```
6. Al completar los pasos anteriores puedes proceder a ejecutar el proyecto con el siguiente comando y acceder a usar la API en http://localhost:8001/docs
```bash
uvicorn main:app --reload --port 8001
```
## Detalles del proyecto
Para el desarrollo de este proyecto decidí usar fastAPI debido a que este framework cuenta con múltiples beneficios como por ejemplo un excelente rendimiento por lo que permite manejar un alto número de solicitudes simultáneamente, lo cual es ideal para tareas de web scraping que pueden involucrar múltiples peticiones. Posee también soporte para operaciones asíncronas usanso "async" para tareas de I/O y su gran escalibidad puede ser aprovechable para futuras mejoras del proyecto. También usé Background Tasks de fastApi para lograr ejecutar tareas en segundo plano y así no tener que estar esperando a que se complete la operación antes de recibir la respuesta.

Para el almacenamiento de la información usé la base de datos embedida SQLite debido a que su funcionamiento es muy práctico y no requiere configuración previa, lo que facilita el proceso correr el proyecto y evaluar la prueba. 

Para los controladores intenté implementar el patrón de diseño llamado strategy creando la clase abstracta "ScrapperCreation" la cual define la estructura básica para algunos procesos de scrapeo, incluyendo el payload común y un atributo process_execute para diferenciar los tipos de procesos. Y las Clases Concretas "ScrapperActor" y "ScrapperDemandado" heredan de "ScrapperCreation" y definen estrategias específicas de scraping para actores y demandados.

Para el modelo de la base de datos se realiza un análisas de la información que se necesita extraer y detecté que la información está segmentada por distintos grupos de listas, por lo que se crea una tabla para cada grupo y así se asegura recopilar toda la información suministrada por la página y mantener la integridad de la misma. Además, uso el ORM SQLAlchemy ya que simplifica la interacción con la base de datos y ofrece una capa de protección para evitar sql injection.

Además, implementé un debbuger para facilitar el proceso de desarrollo logrando realizar las validaciones locales mediante una depuración paso a paso y así alcanzar una identificación rápida de errores.
