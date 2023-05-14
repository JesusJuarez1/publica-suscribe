##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: record.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y los almacena en un archivo de texto que simula el expediente de los pacientes
#
#   Este archivo también define el punto de ejecución del Suscriptor
#
#   A continuación se describen los métodos que se implementaron en esta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |       __init__()       |  - self: definición de   |  - constructor de la  |
#           |                        |    la instancia de la    |    clase              |
#           |                        |    clase                 |                       |
#           +------------------------+--------------------------+-----------------------+
#           |       suscribe()       |  - self: definición de   |  - inicializa el      |
#           |                        |    la instancia de la    |    proceso de         |
#           |                        |    clase                 |    monitoreo de       |
#           |                        |                          |    signos vitales     |
#           +------------------------+--------------------------+-----------------------+
#           |        consume()       |  - self: definición de   |  - realiza la         |
#           |                        |    la instancia de la    |    suscripción en el  |
#           |                        |    clase                 |    distribuidor de    |
#           |                        |  - queue: ruta a la que  |    mensajes para      |
#           |                        |    el suscriptor está    |    comenzar a recibir |
#           |                        |    interesado en recibir |    mensajes           |
#           |                        |    mensajes              |                       |
#           |                        |  - callback: accion a    |                       |
#           |                        |    ejecutar al recibir   |                       |
#           |                        |    el mensaje desde el   |                       |
#           |                        |    distribuidor de       |                       |
#           |                        |    mensajes              |                       |
#           +------------------------+--------------------------+-----------------------+
#           |       callback()       |  - self: definición de   |  - escribe los datos  |
#           |                        |    la instancia de la    |    del adulto mayor   |
#           |                        |    clase                 |    recibidos desde el |
#           |                        |  - ch: canal de          |    distribuidor de    |
#           |                        |    comunicación entre el |    mensajes en un     |
#           |                        |    suscriptor y el       |    archivo de texto   |
#           |                        |    distribuidor de       |                       |
#           |                        |    mensajes [propio de   |                       |
#           |                        |    RabbitMQ]             |                       |
#           |                        |  - method: método de     |                       |
#           |                        |    conexión utilizado en |                       |
#           |                        |    la suscripción        |                       |
#           |                        |    [propio de RabbitMQ]  |                       |
#           |                        |  - properties:           |                       |
#           |                        |    propiedades de la     |                       |
#           |                        |    conexión [propio de   |                       |
#           |                        |    RabbitMQ]             |                       |
#           |                        |  - body: contenido del   |                       |
#           |                        |    mensaje recibido      |                       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import json, time, pika, sys, os

class Record:

    def __init__(self):
        try:
            os.mkdir('records')
        except OSError as _:
            pass
        self.topic = "record"

    def suscribe(self):
        print("Esperando datos del paciente para actualizar expediente...")
        print()
        self.consume(queue=self.topic, callback=self.callback)

    def consume(self, queue, callback):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            channel.queue_declare(queue=queue, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(on_message_callback=callback, queue=queue)
            channel.start_consuming()
        except (KeyboardInterrupt, SystemExit):
            channel.close()
            sys.exit("Conexión finalizada...")

    def callback(self, ch, method, properties, body):
        print("datos recibidos, actualizando expediente del paciente...")
        data = json.loads(body.decode("utf-8"))
        record_file = open (f"./records/{data['ssn']}.txt",'a')
        record_file.write(f"\n[{data['wearable']['date']}]: {data['name']} {data['last_name']}... ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        record_file.close()
        time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    record = Record()
    record.suscribe()