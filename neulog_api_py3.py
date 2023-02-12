# -*- coding: utf-8 -*-

'''
This Script allows you to connect to Neulog API and record electrodermal activity
'''

from urllib.request import urlopen
import json
import time
import ast

#import utils

scheme = 'http://localhost:'
PORT = str(22004)
command = 'NeuLogAPI?'
URL = scheme+PORT+'/'+command
#print URL


def get_server_status():
    URI = URL+'GetSeverStatus'
    print (URI)
    request = urlopen(URI)
    
    dict_str = request.read().decode("UTF-8")
    return ("STATUS" + dict_str)

def get_server_version():
    URI = URL+'GetServerVersion'
    print (URI)
    request = urlopen(URI)

    dict_str = request.read().decode("UTF-8")
    return ("S VERSION" + dict_str)

def set_sensor_id(id_num):
    URI = URL+'SerSensorsID:[' +str(id_num) + ']'
    #GSR],[1],[' + str(rate) + '],[' \
        #+ str(samples) + ']'
    print (URI)
    request = urlopen(URI)

    dict_str = request.read().decode("UTF-8")
    return ("SET Sensors ID? " + dict_str)

def get_value():
    URI = URL+'GetSensorValue:[GSR],[2]'
    request = urlopen(URI)
    dict_str = request.read().decode("UTF-8")
    
    return ("S VALUE " + dict_str)


def experiment_start(sensors, rate, samples):
    # 1 = 10000 per second
    # 2 = 3000 per second
    # 3 = 2000 per second
    # 4 = 1000 per second
    # 5 = 100 per second
    # 6 = 50 per second
    # 7 = 20 per second
    # 8 = 10 per second
    # 9 = 5 per second]

    #EJ: samples = 6000 '
    URI = URL+'StartExperiment:'
    for sensor in sensors:
        URI += '[' +str(sensor[0])+ '],[' +str(sensor[1])+ '],'

    URI += '[' +str(rate)+ '],[' + str(samples) + ']'

    print (URI)
    request = urlopen(URI)

    dict_str = request.read().decode("UTF-8")
    return ("EXP START? " + dict_str)


def get_experiment_values_clean(sensors):
    URI = URL+'GetExperimentSamples:'
    print(1)
    for sensor in sensors:
        URI += '[' +str(sensor[0])+ '],[' +str(sensor[1])+ '],'
    print(2)
    request = urlopen(URI)
    print(3)
    dict_str = request.read().decode("UTF-8")
    print(4)
    return (dict_str)


def get_experiment_values(sensors):
    URI = URL+'GetExperimentSamples:'
    print(1)
    for sensor in sensors:
        URI += '[' +str(sensor[0])+ '],[' +str(sensor[1])+ '],'
    print(2)
    request = urlopen(URI)
    print(3)
    dict_str = request.read().decode("UTF-8")
    print(4)
    return ("EXP VALUES " + dict_str)


def experiment_stop():
    URI = URL+'StopExperiment'
    request = urlopen(URI)

    dict_str = request.read().decode("UTF-8")
    return ("EXP STOP? " + dict_str)


def set_sensor_range():
    URI = URL +'SetSensorRange:[GSR],[2],[9001]'
    request = urlopen(URI)

    dict_str = request.read().decode("UTF-8")
    return ("SET RANGE " + dict_str)


if __name__ == '__main__':
    print (get_server_status())
    print (get_server_version())

    print ("Comenzando experimento")
    # r = experiment_start([('GSR',1), ('', 2)], 7, 10000)
    r = experiment_start([('GSR',1)], 7, 10000)
    print(r)
    with open('test_prueba.txt', "a") as text_file:
        text_file.write(r+'\n')

    time.sleep(10)
    v = get_experiment_values([('GSR',1)])
    with open('test_prueba.txt', "a") as text_file:
        text_file.write(v+'\n')
    print(v)

    s = experiment_stop()
    print(s)

    with open('test_prueba.txt', "a") as text_file:
        text_file.write(s+'\n')

