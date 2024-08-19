# Herramienta de Escaneo de Puertos

## Descripción

La **Herramienta de Escaneo de Puertos** es una aplicación web desarrollada en Flask que permite a los usuarios escanear puertos en una dirección IP específica. Esta herramienta está diseñada para ser utilizada por profesionales de ciberseguridad y administradores de sistemas para verificar qué puertos están abiertos y potencialmente vulnerables en sus redes.

## Objetivo

El objetivo de esta aplicación es proporcionar una interfaz web sencilla para realizar escaneos de puertos, facilitando la detección de servicios activos en una red. Este tipo de escaneo es fundamental para identificar posibles vectores de ataque y fortalecer la seguridad de los sistemas.

## Funcionamiento

1. **Interfaz de Usuario**: Los usuarios pueden ingresar una dirección IP y un rango de puertos a través de un formulario en la página principal.
2. **Escaneo de Puertos**: La aplicación realiza el escaneo de puertos utilizando la función `scan_ports` en el backend, que verifica si los puertos en el rango especificado están abiertos.
3. **Resultados**: Los resultados del escaneo se muestran en formato JSON, indicando qué puertos están abiertos.

## Tecnologías Utilizadas

- **Flask**: Framework web para Python, utilizado para crear la aplicación web.
- **Python**: Lenguaje de programación principal utilizado en el backend.
- **HTML/CSS**: Para el diseño y la presentación de la interfaz de usuario.
- **Socket**: Biblioteca de Python para realizar el escaneo de puertos.

## Instalación y Configuración

1. **Clona el Repositorio**:

    ```bash
    git clone https://github.com/FranJavacisco/Herramienta-de-Escaneo-de-Puertos.git
    ```

2. **Navega al Directorio del Proyecto**:

    ```bash
    cd Herramienta-de-Escaneo-de-Puertos
    ```

3. **Crea y Activa el Entorno Virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. **Instala las Dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Ejecuta la Aplicación**:

    ```bash
    python app.py
    ```

6. **Accede a la Aplicación**: Abre tu navegador y dirígete a `http://127.0.0.1:5000`.

## Mejoras Futuras

- **Autenticación de Usuarios**: Implementar un sistema de autenticación para restringir el acceso.
- **Mejora en la Interfaz**: Agregar una interfaz de usuario más interactiva y visualmente atractiva.
- **Escaneo de Puertos Avanzado**: Implementar técnicas de escaneo más avanzadas y opciones de configuración.

## Contribuciones

Las contribuciones son bienvenidas. Puedes contribuir de las siguientes maneras:

- **Reportar Bugs**: Abre un problema (issue) en GitHub si encuentras errores o tienes sugerencias.
- **Enviar Pull Requests**: Si tienes mejoras o correcciones, envía un pull request con tus cambios.

Por favor, asegúrate de seguir las [guías de contribución](CONTRIBUTING.md) y revisar las [normas de código](CODE_OF_CONDUCT.md) antes de contribuir.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

Si tienes preguntas adicionales, no dudes en abrir un problema en GitHub o contactarme directamente.

