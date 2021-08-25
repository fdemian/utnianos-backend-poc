# Como correr el repositorio.

## Instalar paquetes.

El repositorio requiere instalados:

 - Python 3
 - PostgreSQL
 - Pipenv

 Asegurarse de que PostgreSQL este corriendo.

 ```
 sudo service postgresql start
 ```


## Crear base de datos.

1) Editar el archivo config.json y cambiar los parametros de la opción database de acuerdo a nuestro ambiente. Los mismos son:

- user: usuario de la base de datos (por defecto "postgres").
- name: nombre de la base de datos a utilizar/crear. (por defecto "utnianos").
- port: puerto donde correr la base de datos (por defecto 5432).
- password: contraseña de la base de datos (por defecto "postgres").



2) Instalar pipenv (manejador de paquetes de python)

```
python3 -m pip install pipenv
```

3) Instalar paquetes del programa.

```
pipenv shell
```

```
pipenv sync
```

4) Ejecutar el comando de setup. El mismo creara la base de datos y corre las migraciones.

```
python3 setup.py
```

Si no hubo errores, la base de datos fue creada y contiene todas las migraciones.

## Correr el programa

Ejecutar el siguiente comando:

```
pipenv run python3 main.py
```
