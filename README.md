# MiniMarketPLUS: Sistema de Compras Automatizadas para reducir el tiempo de espera con Detección de Objetos para minimarkets de Lima Metropolitana

Este proyecto, denominado MinimarketPlus, tiene como objetivo principal desarrollar un sistema informático que reduzca el tiempo de espera de los clientes en minimarkets de Lima Metropolitana utilizando visión computacional para la detección de objetos.

## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Dataset](#dataset)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Licencia](#licencia)
7. [Contacto](#contacto)

## Descripción
MinimarketPlus es un sistema diseñado para minimizar el tiempo de espera de los clientes en minimarkets mediante el uso de tecnologías avanzadas como la visión computacional. Este sistema registrará todos los productos seleccionados por los clientes a través de una cámara, calculará el precio total y permitirá a los clientes realizar el pago de manera rápida y eficiente. El sistema está destinado a ser una solución eficiente para los minimarkets de Lima Metropolitana, especialmente durante las horas punta.

## Caracteristicas
- Detección de Objetos: Utiliza el algoritmo YOLOv8 para la detección precisa de productos.
- Sistema Automatizado: Reduce significativamente el tiempo de espera en la fila de pagos.
- Interfaz Intuitiva: Aplicación de escritorio fácil de usar para monitorear la detección de productos.
- Optimización del Tiempo de Espera: Dirigido a minimizar el tiempo de espera en minimarket.

## Dataset
- Dataset sin data augmentation lo encuentras en el siguiente link:
https://drive.google.com/file/d/1dbHa8Nr5OoW-bdLVWPpBoqctkAX9V-G0/view?usp=sharing
- Dataset con data augmentation:
https://drive.google.com/file/d/1u61yoQ1LT2lzjB7pMWEtJ2vlpiCIAbjQ/view?usp=sharing

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/proyecto.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd proyecto
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación de escritorio:
```bash
python main.py
```
2. Utiliza una cámara de celular para probar la detección de productos.
3. La aplicación registrará los productos y mostrará el precio total para su pago
   
## Licencia
Este proyecto está bajo la Licencia MIT. Mira el archivo LICENSE para más detalles.

## Contacto
Para más información o preguntas sobre el proyecto, puedes contactar a los autores:

- Sebastian Alonso Arana de Carpio
- Luis Gustavo Becerra Bisso
Correo electrónico: 
