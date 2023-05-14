##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: publicador.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Este archivo define la conexión del publicador hacia el el distribuidor de mensajes
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |        publish()       |  - queue: nombre de la   |  - publica el mensaje |
#           |                        |    ruta con la que se    |    en el distribuidor |
#           |                        |    vinculará el mensaje  |    de mensajes        |
#           |                        |    enviado               |                       |
#           |                        |  - data: mensaje que     |                       |
#           |                        |    será enviado          |                       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
#import pika

#def publish(queue, data):
 #   connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  #  channel = connection.channel()
   # channel.queue_declare(queue=queue, durable=True)
    #channel.basic_publish(exchange='', routing_key=queue, body=data, properties=pika.BasicProperties(delivery_mode=2))
    #connection.close()
    

import stomp

def publish(queue, data):
    conn = stomp.Connection(host_and_ports=[('localhost', 61613)])
    conn.connect()
    conn.send(body=data, destination=queue)
    conn.disconnect()
