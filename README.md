# Python CLI Quickstart

Python CLI Quickstart es una plantilla para desarrollar aplicaciones de línea de comandos (CLI) en Python.

## Características

- **Estructura Modular**: Organiza el código en características planas, facilitando la navegación y el mantenimiento.
- **CLI Interactiva**: Utiliza Click para crear una interfaz de línea de comandos fácil de usar.
- **Pruebas Integradas**: Incluye un marco de pruebas utilizando pytest para garantizar la calidad del código.


## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone git@github.com:oswaldom-code/python-cli-quickstart.git
   cd python-cli-quickstart

   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python3 -m venv ENV
   source ENV/bin/activate  # En Linux/Mac
   ENV\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
python3 -m cli.main [comando] [opciones]
```

### Ejemplo

Para saludar a un usuario:

```bash
python -m cli.main hello --name Yoda
```

## Pruebas

Para ejecutar las pruebas, asegúrate de estar en el entorno virtual y ejecuta:

```bash
pytest -v

```
