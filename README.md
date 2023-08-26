# Configuración del backend bootcamp Gorillalogic 2023 Cali

# Crear la base de datos:

1. Definir la variable de entorno `FLASK_APP`:

   - En sistemas Unix/Linux/macOS:
     ```bash
     export FLASK_APP=main
     ```
   - En sistemas Windows (en CMD):
     ```bash
     set FLASK_APP=main
     ```

2. Librerías necesarias:

  ```bash
  virtualenv env
  cd env/Scripts
  activate
  cd ../..
  pip install -r requirements.txt
  ```

3-1. Importar y ejecutar el script de migración:

   ```bash
   flask shell
   from models import CheckList
   from config import db
   db.create_all()
   ```

   Si deseas realizar cambios, puedes borrar todas las tablas y ejecutar nuevamente:

   ```python
   db.drop_all()
   db.create_all()
   ```

   Sin embargo, esta acción borrará todas las tablas. Por eso, es recomendable trabajar con Flask-Migrate para migraciones más controladas. Puedes encontrar información en [este enlace](https://flask-migrate.readthedocs.io/en/latest/index.html).

3-2. Instalar Flask-Migrate y ejecutar los comandos:

   - Inicializa las migraciones:

     ```bash
     flask db init
     ```

   - Crea una nueva migración (esto generará un archivo con instrucciones SQL para aplicar los cambios):

     ```bash
     flask db migrate -m "Migración inicial."
     ```

   - Ejecuta la migración en la base de datos:
     ```bash
     flask db upgrade
     ```

4. Ejecutar proyecto:

  ```bash
   python main.py
  ```
5. Crear un archivo .env en el proyecto con este contenido:

  ```bash
   SECRET_KEY_OPENAI=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
   secret_key = os.environ.get("SECRET_KEY_OPENAI")
  ```
