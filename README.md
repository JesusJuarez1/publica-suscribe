# Arquitectura Publica-Suscribe

## Sistema de Monitoreo de Adultos Mayores (SMAM)

Existe un un lugar llamado Seten en el que viven un grupo de adultos mayores, parte del personal que trabaja en este lugar, entre otras tareas, se dedica a atender las necesidades de los adultos mayores y a monitorear su estado de salud.

La comunidad llamada Girls that Code in Python, que es una comunidad altruista en la región, decidió, a manera de donación, desarrollarles un sistema de cómputo para realizar las actividades de monitoreo del estado de salud de los adultos mayores de forma (semi-)automática. Para ello, la comunidad utilizó un conjunto de dispositivos “wearables” que portan cada uno de los adultos mayores. Mediante el envío de información sobre ritmo cardiaco, presión arterial y temperatura, estos dispositivos “wearables” permiten monitorear en tiempo real a cada uno de los adultos mayores y de esta forma ser más eficientes en la prevención de incidencias.

En la siguiente figura se muestra el diseño de la propuesta de solución del departamento de desarrollo para el SMAM.

![Vista de contenedores del SMAM](docs/context-view.png)

A continuación se muestra la vista de módulos del Sistema de Monitoreo de Adultos Mayores (SMAM) en el que se implementa en el distriburidor de mensajes la Tecnología utilizada que es ActiveMQ.

![Vista de contenedores del SMAM](docs/containers-view.png)

## Estructura del proyecto

Este repositorio contiene los siguientes directorios y archivos:

```bash
    ├── docs                                # carpeta de documentación
    │  ├── context-view.png                 # vista del contexto del sistema
    │  ├── smam.drawio                      # archivo editable de daiagramas del sistema
    ├── publicadores                        # publicadores del sistema
    |  ├── src                              # código fuente de los publicadores
    │     ├── devices                       # archivos de definición de dispositivos
    │        ├── accelerometer.py           # simulador del dispositivo de hardware acelerómetro
    │        ├── timer.py                   # simulador del dispositivo de hardware cronómetro
    │        ├── xiaomi_my_band.py          # simulador de dispositivo de hardware Xiaomi
    │     ├── helpers                       # archivos auxiliares del sistema
    │        ├── __init__.py                # indica la definición de módulo python
    │        ├── publicador.py              # archivo auxiliar de comunicación con el distribuidor de mensajes
    │     ├── __init__.py                   # indica la definición de módulo python
    │     ├── patient.py                    # representación de un adulto mayor en el sistema
    |  ├── main.py                          # archivo principal de ejecución de publicadores
    ├── suscriptores                        # suscriptores del sistema
    │  ├── monitor.py                       # suscriptor que muestra en pantalla las alertas del sistema
    │  ├── notifier.py                      # suscriptor que notifica a un(a) enfermero(a) en particular
    │  ├── record.py                        # suscriptor que actualiza el expediente de un adulto mayor en particular
    ├── .gitignore                          # exclusiones de git
    ├── README.md                           # este archivo
    ├── requirements.txt                    # dependencias del sistema
```

## Prerrequisitos

- Clonar el repositorio:
  ```shell
  $ git clone https://github.com/JesusJuarez1/publica-suscribe
  $ cd publica-subscribe
  ```
- Contar con python 3.8 o superior y pip3 (las pruebas fueron realizadas con la versión 3.8). Se recomienda utilizar [pyenv](https://github.com/pyenv/pyenv) como manejador de versiones de python; una vez instalado se pueden seguir los siguientes comandos para instalar la versión deseada de python, esto hay que realizarlo en la raíz del repositorio:

  ```shell
  $ pyenv install 3.8
  $ pyenv local 3.8
  ```

- Crear un ambiente virtual para manejar las dependencias ejecutando:

  ```shell
  $ python3 -m venv venv
  ```

  en Windows:

  ```shell
  $ python3 -m venv venv
  ```

  si no funciona el comando anterior, ejecutar el siguiente:

  ```shell
  $ py -3 -m venv venv
  ```

  Esto creará una carpeta llamada "venv" que representa nuestro ambiente virtual y donde instalaremos todas las dependencias.

- Activamos el ambiente virtual:

  ```shell
  $ source venv/bin/activate
  ```

  o en Windows:

  ```shell
  $ venv\Scripts\activate
  ```

- Instalamos las dependencias del sistema ejecutando:

  ```shell
  (venv)$ pip3 install -r requirements.txt
  ```

  Los paquetes que se instalarán son los siguientes:

  | Paquete | Versión | Descripción                                                                   |
  | ------- | ------- | ----------------------------------------------------------------------------- |
  | Faker   | 13.3.0  | Generador de datos falsos                                                     |
  | telepot | 12.7    | Api de Telegram                                                               |
  | stomp   | 8.1.0   | Protocolo de mensajería simple que proporciona la extensión de ActiveMQ       |

  _**Nota**: También puedes instalar estos prerrequisitos manualmente ejecutando los siguientes comandos:_

  > pip3 install stop== 8.1.0
  > pip3 install Faker==13.3.0
  > pip3 install telepot==12.7

## Instalación ActiveMQ

- docker run -it --rm --name activemq -p 61613:61613 -p 8161:8161 rmohr/activemq

## Ejecución

Sigue las siguientes instrucciones para ejecutar los diferentes componentes del sistema.

> **Nota:** Cada componente debe ser ejecutado en una terminal independiente

### Publicador

- Entramos a la carpeta `publicadores`:

  ```shell
  (venv)$ cd publicadores
  ```

- Ejecutamos el archivo `main.py`:
  ```shell
  (venv)$ python main.py
  ```

### Suscriptores

**Notificador de alertas**

- Entramos a la carpeta `suscriptores`:

  ```shell
  (venv)$ cd suscriptores
  ```

- Ejecutamos el archivo `notifier.py`:
  ```shell
  (venv)$ python notifier.py
  ```

**Log**

- Entramos a la carpeta `suscriptores`:

  ```shell
  (venv)$ cd suscriptores
  ```

- Ejecutamos el archivo `record.py`:
  ```shell
  (venv)$ python record.py
  ```

**Monitor**

- Entramos a la carpeta `suscriptores`:

  ```shell
  (venv)$ cd suscriptores
  ```

- Ejecutamos el archivo `monitor.py`:
  ```shell
  (venv)$ python monitor.py
  ```

## Versión

2.2.1 - Abril 2023

## Autores

- **Perla Velasco**
- **Yonathan Martínez**
- **Sergio Salazar**
- **Jorge Solis**

## Editores

- **Daniel Castillo**
- **Victor Silva**
- **Eric Castañeda**
- **Joseph Antuan**
- **Fernando Salinas**
- **Jesús Juárez**
