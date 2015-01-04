#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Script.py
#  
#  Copyright 2014 Starky <starky@GA-990FXA-UD3>
#  
#  La idea de este script es que comunique a un servidor remoto cual es su ip externa
#
#  
#

import pycurl
from StringIO import StringIO

import mechanize
url = "http://nuestraurl.com"


def descargaip():
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, 'http://ifconfig.es')
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	return body

def enviaremoto(IPexterna):
	br = mechanize.Browser() # inicializo la variable para usar la libreria
	
	response=br.open(url)
	#print response.read() 
	br.select_form(name = "formulario")
	print br.form
	br.form[ "nombrepc" ] = "Casa" 
	br.form[ "ip" ] = IPexterna
	br.submit()
	print br.response().read()
	

def main():
	IP = descargaip()
	print IP
	enviaremoto(IP)


if __name__ == '__main__':
	main()
