# Laboratorio

El sistema incluye un chatbot para mejorar la comunicación.

## Calculadora sencilla

Calculadora de consola con suma, resta, multiplicación y división.

### Crear el entorno virtual

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### Ejecutar la aplicación

```bash
python .\calculadora.py
```

### Ejecutar las pruebas

```bash
python -m unittest -v .\test_calculadora.py
```

### Ejecutar linting

```bash
ruff check .
```

### Integración continua

El workflow de [GitHub Actions](.github/workflows/test_and_build.yml) ejecuta las pruebas
automáticamente en cada `push` de cualquier rama y en los `pull request` cuyo
destino sea `main`. Crea su propio entorno virtual
para mantener aislado el entorno de CI e instala las dependencias definidas en
[requirements.txt](requirements.txt).
