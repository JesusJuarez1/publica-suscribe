##!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Archivo: notifier.py
# Capitulo: Estilo Publica-Suscribe
#Editor(es): Víctor Ubaldo Silva Luna
#            Joseph Antuan Martínez Alvarado
#            Fernando Félix Salinas
#            Daniel Alejandro Morales Castillo
#            Jesús Manuel Juárez Pasillas
#            Eric Castañeda Estrada.

# Version: 4.0.0 Mayo 2023
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y lo notificará a un(a) enfermero(a) én particular para la atención del adulto mayor en
#   cuestión
#
#   Este archivo también define el punto de ejecución del Suscriptor
#
# -------------------------------------------------------------------------
import json
import time
import stomp
import sys
import telepot


class Notifier:

    def __init__(self):
        self.topic = "notifier"
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.set_listener('', MyListener())

    def suscribe(self):
        print("Inicio de gestión de notificaciones...")
        print()
        self.conn.connect('admin', 'admin', wait=True)
        self.conn.subscribe(destination=self.topic, id=1, ack='auto')

    def disconnect(self):
        self.conn.disconnect()
        print("Conexión finalizada...")

class MyListener(stomp.ConnectionListener):
    
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)
    
    def on_message(self, frame):
        print("enviando notificación de signos vitales...")
        data = json.loads(frame.body)
        print("ADVERTENCIA!!!")
        print(f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
        print(f"ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        print()
        time.sleep(1)


if __name__ == '__main__':
    notifier = Notifier()
    notifier.suscribe()
    input("Presione cualquier tecla para detener el notificador...")
    notifier.disconnect()
