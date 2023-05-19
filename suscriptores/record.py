##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: record.py
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
#   y los almacena en un archivo de texto que simula el expediente de los pacientes
#
#   Este archivo también define el punto de ejecución del Suscriptor
#
#-------------------------------------------------------------------------
import json, time, stomp, sys, os

class Record:

    def __init__(self):
        try:
            os.mkdir('records')
        except OSError as _:
            pass
        self.topic = "record"
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.set_listener('', MyListener())

    def suscribe(self):
        print("Esperando datos del paciente para actualizar expediente...")
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
    record = Record()
    record.suscribe()
    input("Presione cualquier tecla para detener el record...")
    record.disconnect()