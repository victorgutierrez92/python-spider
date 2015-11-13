#!/usr/bin/env python
# -*- coding: ISO8859-1 -*-
import requests
import os

from StringIO import StringIO
import lxml.etree

# para extracción de imágenes
import urllib, cStringIO
from PIL import Image
from base64 import b64encode

def stringFormat(s):
	s = str(s)[2:-2].translate(None, "'")
	s = s.replace("\\xc3\\xa1", "a")
	s = s.replace("\\xc3\\xa9", "e")
	s = s.replace("\\xc3\\xad", "i")
	s = s.replace("\\xc3\\xb3", "o")
	s = s.replace("\\xc3\\xb1", "n")
	s = s.replace("\\xc3\\xba", "u")
	s = s.replace("\\xc3\\xbc", "u")

	s = s.replace("\\xc3\\x81", "A")
	s = s.replace("\\xc3\\x89", "E")
	s = s.replace("\\xc3\\x8d", "I")
	s = s.replace("\\xc3\\x93", "O")
	s = s.replace("\\xc3\\x91", "N")
	s = s.replace("\\xc3\\x9a", "U")
	s = s.replace("\\xc3\\x9c", "U")
	return s

def cleanXpathResponse(x):
	if not x:
		return ""
	else:
		return stringFormat(x)

session = requests.Session()

paramsPost = {"__VIEWSTATE":"dDwtMTc4MDI2NTM1MDt0PDtsPGk8MT47PjtsPHQ8O2w8aTwzPjtpPDE3Pjs+O2w8dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPEFHU1VfTm9tYnJlO0FHU1VfSWQ7Pj47Pjt0PGk8Mj47QDxMTyBDQU1QSU5PO1BSVUVCQTs+O0A8NDI7Mjk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPENsYXZlIGluY29ycmVjdGEuOz4+Oz47Oz47Pj47Pj47bDxjaGtBZG07Pj4=","chkAdm":"on","lstSucursal":"42","btnIngresar":"Ingresar","txtLogin":"usuario","txtPass":"contraseña"}
headers = {"Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Referer":"http://lc.fitnet.cl/login.aspx","User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded"}
cookies = {"ASP.NET_SessionId":"n0t1fc55wxtsourvzc5vft45"}
response = session.post("http://lc.fitnet.cl/login.aspx", data=paramsPost, headers=headers, cookies=cookies)

output_handler = open('output.csv', 'a')
output_handler.write('Codigo;')
output_handler.write('Sucursal;')
output_handler.write('Pais;')
output_handler.write('Rut;')
output_handler.write('Pasaporte;')
output_handler.write('Primer Nombre;')
output_handler.write('Segundo Nombre;')
output_handler.write('Primer Apellido;')
output_handler.write('Segundo Apellido;')
output_handler.write('Direccion;')
output_handler.write('Region;')
output_handler.write('Comuna;')
output_handler.write('Ciudad;')
output_handler.write('Tel. Casa;')
output_handler.write('Tel. Trabajo;')
output_handler.write('Fax;')
output_handler.write('Cod. Posta.;')
output_handler.write('Estado Civil;')
output_handler.write('Sexo;')
output_handler.write('Dia Nacimiento;')
output_handler.write('Mes Nacimiento;')
output_handler.write('Ano Nacimiento;')
output_handler.write('Mail;')
output_handler.write('Imagen (Base64Encode);')
output_handler.write('Tipo Membresia;')
output_handler.write('ID Plan 1;')
output_handler.write('Nombre Plan 1;')
output_handler.write('Inicio Plan 1;')
output_handler.write('Fin Plan 1;')
output_handler.write('ID Plan 2;')
output_handler.write('Nombre Plan 2;')
output_handler.write('Inicio Plan 2;')
output_handler.write('Fin Plan 2;')
output_handler.write('ID Plan 3;')
output_handler.write('Nombre Plan 3;')
output_handler.write('Inicio Plan 3;')
output_handler.write('Fin Plan 3;')
output_handler.write('ID Plan 4;')
output_handler.write('Nombre Plan 4;')
output_handler.write('Inicio Plan 4;')
output_handler.write('Fin Plan 4;')
output_handler.write('ID Plan 5;')
output_handler.write('Nombre Plan 5;')
output_handler.write('Inicio Plan 5;')
output_handler.write('Fin Plan 5;')
output_handler.write('ID Plan 6;')
output_handler.write('Nombre Plan 6;')
output_handler.write('Inicio Plan 6;')
output_handler.write('Fin Plan 6;')
output_handler.write('ID Plan 7;')
output_handler.write('Nombre Plan 7;')
output_handler.write('Inicio Plan 7;')
output_handler.write('Fin Plan 7;')
output_handler.write('ID Plan 8;')
output_handler.write('Nombre Plan 8;')
output_handler.write('Inicio Plan 8;')
output_handler.write('Fin Plan 8;')
output_handler.write('ID Plan 9;')
output_handler.write('Nombre Plan 9;')
output_handler.write('Inicio Plan 9;')
output_handler.write('Fin Plan 9;')
output_handler.write('ID Plan 10;')
output_handler.write('Nombre Plan 10;')
output_handler.write('Inicio Plan 10;')
output_handler.write('Fin Plan 10;')
output_handler.write('ID Plan 11;')
output_handler.write('Nombre Plan 11;')
output_handler.write('Inicio Plan 11;')
output_handler.write('Fin Plan 11;')
output_handler.write('ID Plan 12;')
output_handler.write('Nombre Plan 12;')
output_handler.write('Inicio Plan 12;')
output_handler.write('Fin Plan 12;')
output_handler.write('ID Plan 13;')
output_handler.write('Nombre Plan 13;')
output_handler.write('Inicio Plan 13;')
output_handler.write('Fin Plan 13;')
output_handler.write('ID Plan 14;')
output_handler.write('Nombre Plan 14;')
output_handler.write('Inicio Plan 14;')
output_handler.write('Fin Plan 14;')
output_handler.write('ID Plan 15;')
output_handler.write('Nombre Plan 15;')
output_handler.write('Inicio Plan 15;')
output_handler.write('Fin Plan 15;')
output_handler.write('ID Plan 16;')
output_handler.write('Nombre Plan 16;')
output_handler.write('Inicio Plan 16;')
output_handler.write('Fin Plan 16;')
output_handler.write('ID Plan 17;')
output_handler.write('Nombre Plan 17;')
output_handler.write('Inicio Plan 17;')
output_handler.write('Fin Plan 17;')
output_handler.write('ID Plan 18;')
output_handler.write('Nombre Plan 18;')
output_handler.write('Inicio Plan 18;')
output_handler.write('Fin Plan 18;')
output_handler.write('ID Plan 19;')
output_handler.write('Nombre Plan 19;')
output_handler.write('Inicio Plan 19;')
output_handler.write('Fin Plan 19;')
output_handler.write('ID Plan 20;')
output_handler.write('Nombre Plan 20;')
output_handler.write('Inicio Plan 20;')
output_handler.write('Fin Plan 20\n')

totalFound = 0

for count in range(10000):
	id_usuario = count;
	paramsPost = {"inpAno":"","hiddMail_formato":" ","hiddMail_listaNombre":" ","inpDiaTerminoDesde":"4","inpPasaporte":"","hiddMail_listaId":" ","optSocioCorp":"optSociosAmbos","hiddMail_asunto":"[Ingrese el Asunto del Correo]","inpDiaTerminoHasta":"4","inpTexto":"juan","lstEstado":"1","lstSucursal":"42","optSexo":"optM","__EVENTTARGET":"","inpMesTerminoHasta":"11","__EVENTARGUMENT":"","chkCodigo":"on","btnBuscar":"Buscar","hiddMail_listaEmail":" ","inpDia":"","hiddMail_texto":"[Ingrese el Texto]","inpAnnoTerminoDesde":"2015","inpMesTerminoDesde":"11","hidFechaTerminoHasta":"4/11/2015","inpCodigo":str(id_usuario),"lstPlan":"1","lstTipo":"1","hidFechaTerminoDesde":"4/11/2015","lstRegistrosPagina":"10","inpAnnoTerminoHasta":"2015","__VIEWSTATE":"dDwtMTczMDMzNzY4NDt0PDtsPGk8MT47PjtsPHQ8O2w8aTwyMz47aTwyNT47aTwyNz47aTwzMT47aTwzNT47aTw0Mz47aTw3OD47aTw4MD47aTw4Mj47aTw4ND47aTw4Nj47aTw4OD47aTw5MD47PjtsPHQ8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxhZ3RzX25vbWJyZTthZ3RzX2lkOz4+Oz47dDxpPDU+O0A8UG93ZXI7R29sZDtQcmVtaXVtO1ZpcDtUb2RvIEdyYXRpczs+O0A8MTsyOzM7ODs5Oz4+Oz47Oz47dDxwPHA8bDxDaGVja2VkOz47bDxvPGY+Oz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPE5vbWJyZTtJZDs+Pjs+O3Q8aTwxNj47QDxNRU5TVUFMIFBSRVBBR087VFJJTUVTVFJBTCBQUkVQQUdPO1NFTUVTVFJBTCBQUkVQQUdPO0FOVUFMIFBSRVBBR087UEFDIE9ORSBDTFVCO1BBVCBPTkUgQ0xVQjtBTlVBTCBGVVRCT0w7TUVOU1VBTCBCQUlMRSBOScORQVM7TUVOU1VBTCBDQVJBQklORVJPUztNRU5TVUFMIEVTQ09MQVI7T0NITyBNRVNFUztUUklNRVNUUkFMIE9OTElORTtQTEFOIFpVTUJBOzIgTUVTRVMgNTAgZGN0by4gKyAxIE1FUyBERSBSRUdBTE87UExBTiAyIE1FU0VTIENPTiA1MCBEQ1RPLjtQbGFuIDIgbWVzZXMgNjAgZGN0by47PjtAPDE7MjszOzQ7NTs2Ozc7ODs5OzEwOzExOzEzOzI4OzI5OzMwOzMxOz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPEFHU1VfTm9tYnJlO0FHU1VfSWQ7Pj47Pjt0PGk8Mj47QDxMTyBDQU1QSU5PO1BSVUVCQTs+O0A8NDI7Mjk7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxBR0VUX0VzdGFkbztBR0VUX0lkOz4+Oz47dDxpPDU+O0A8QWN0aXZvO0Jsb3F1ZWFkbztJbmFjdGl2bztSZXRpcm87VWx0aW1vIE1lczs+O0A8MTs0OzI7NTszOz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPGFnY3Bfbm9tYnJlO2FnY3BfaWQ7Pj47Pjt0PGk8OT47QDxQQUMgMTIgTWVzZXM7UEFDIE1lbnN1YWwgSW5kZWZpbmlkbztQQUMtUEFUIDEyIG1lc2VzO1BBQy1QQVQgbWVuc3VhbCBJbmRlZmluaWRvO1BBVCAxMiBNZXNlcztQQVQgTWVuc3VhbCBJbmRlZmluaWRvO1BMQU4gREUgQ0FSR0E7UGxhbiBOb3JtYWw7UHJvbW9jacOzbjs+O0A8OTs4OzY7NTsxMTsxMDs0OzE7Mjs+Pjs+Ozs+O3Q8cDw7cDxsPE9uQ2xpY2s7PjtsPGphdmFzY3JpcHQ6cmV0dXJuIHZhbGlkYUJ1c3F1ZWRhKGRvY3VtZW50LmluZ3Jlc2FyKTs+Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTtQYWdlQ291bnQ7UGFnZVNpemU7XyFEYXRhU291cmNlSXRlbUNvdW50O18hSXRlbUNvdW50O0N1cnJlbnRQYWdlSW5kZXg7RGF0YUtleXM7PjtsPG88Zj47aTwxPjtpPDEwPjtpPDA+O2k8MD47aTwwPjtsPD47Pj47PjtAMDxAMDxwPGw8VmlzaWJsZTtIZWFkZXJUZXh0Oz47bDxvPGY+O1w8Ylw+RW52aWFyIE1haWxcPC9iXD47Pj47Ozs7Pjs7QDA8cDxsPFZpc2libGU7PjtsPG88dD47Pj47Ozs7PjtAMDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs7Ozs+Ozs7O0AwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Ozs7Oz47OztAMDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs7Ozs+O0AwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Ozs7Oz47QDA8cDxsPFZpc2libGU7PjtsPG88dD47Pj47Ozs7PjtAMDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs7Ozs+OztAMDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs7Ozs+O0AwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Ozs7Oz47O0AwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Ozs7Oz47QDA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Ozs7Pjs+Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+Oz47bDx0PHA8O3A8bDxvbm1vdXNlb3V0Oz47bDx0aGlzLnN0eWxlLmJhY2tncm91bmRDb2xvcj0nI2YxZjFmMSc7Pj4+Ozs+O3Q8cDw7cDxsPG9ubW91c2VvdXQ7PjtsPHRoaXMuc3R5bGUuYmFja2dyb3VuZENvbG9yPScjZjFmMWYxJzs+Pj47Oz47Pj47Pj47dDxwPHA8bDxGb3JlQ29sb3I7VGV4dDtfIVNCOz47bDwyPFJlZD47Tm8gc2UgZW5jb250cmFyb24gcmVzdWx0YWRvcyBwYXJhIGxhIGLDunNxdWVkYTtpPDQ+Oz4+Oz47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxPbkNsaWNrOz47bDxqYXZhc2NyaXB0OnJldHVybiBjb25maXJtKCfCv0VzdGEgc2VndXJvIHF1ZSBkZXNlYSBlbGltaW5hciBsb3Mgc29jaW9zIHNlbGVjY2lvbmFkb3M/Jyk7Pj4+Ozs+O3Q8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDI+O2k8Mz47aTw2PjtpPDc+O2k8MTA+O2k8MTE+O2k8MTI+O2k8MTM+Oz47bDx0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjs+Pjs+Pjs+Pjs+PjtsPGNoa0NvZGlnbztjaGtSdXQ7Y2hrTm9tYnJlO2Noa0ZlY2hhO2Noa1RpcG9Tb2NpbztjaGtQbGFuO2Noa1N1Y3Vyc2FsO2Noa0VzdGFkbztjaGtQYXNhcG9ydGU7Y2hrQ2F0ZWdvcmlhO2Noa0ZlY2hhVGVybWlub0Rlc2RlO2Noa1NleG87b3B0TTtvcHRGO29wdEY7Y2hrRmVjaGFUZXJtaW5vSGFzdGE7b3B0U29jaW9Ob0NvcnBvcmF0aXZvO29wdFNvY2lvTm9Db3Jwb3JhdGl2bztvcHRTb2Npb0NvcnBvcmF0aXZvO29wdFNvY2lvQ29ycG9yYXRpdm87b3B0U29jaW9zQW1ib3M7Y2hrSW1hZ2VuOz4+","inpMes":"","lstCategoria":"9","inpRut":""}
	response = session.post("http://lc.fitnet.cl/socios/editar.aspx", data=paramsPost, headers=headers, cookies=cookies)

	if(response.content.find("No se encontraron") != -1):
		print "Usuario con ID " + str(id_usuario) + " NO encontrado Total [" + str(totalFound) + "]."
	else:
		totalFound = totalFound + 1;

		print "Usuario con ID " + str(id_usuario) + " SI encontrado Total [" + str(totalFound) + "]."
		HTML = StringIO(response.content)

		# here goes the useful code
		ISO8859_1_html_parser = lxml.etree.HTMLParser(encoding='ISO8859-1')
		tree = lxml.etree.parse(HTML, parser=ISO8859_1_html_parser) # you can pass parse() a file-like object or an URL
		root = tree.getroot()	# obtiene el elemento raíz del arbol

		urlSocio = cleanXpathResponse(root.xpath('//a[@id="DataGrid1__ctl3_HyperLink1"]/@href')) # XPATH (XML Path Lenguage, permite la construcción de expresiones que recorren y procesan un documento XML) evaluado en el contexto del documento. Retorna una lista, boolean, float o string.

		tipoMembresia = root.xpath('//td[@width="100"]//font[@size="2"]/text()')
		tipoMembresia = tipoMembresia[1]

		response = session.get("http://lc.fitnet.cl/socios/" + urlSocio, headers=headers, cookies=cookies)

		HTML = StringIO(response.content)

		# here goes the useful code
		ISO8859_1_html_parser = lxml.etree.HTMLParser(encoding='ISO8859-1')
		tree = lxml.etree.parse(HTML, parser=ISO8859_1_html_parser) # you can pass parse() a file-like object or an URL
		root = tree.getroot()

		sucursal = cleanXpathResponse(root.xpath('//select[@id="lstSucursal"]//option[@selected="selected"]/text()'))
		pais = cleanXpathResponse(root.xpath('//select[@id="lstPais"]//option[@selected="selected"]/text()'))
		sexo = cleanXpathResponse(root.xpath('//input[@name="optSexo" and @checked="checked"]/@id'))
		rut = cleanXpathResponse(root.xpath('//input[@id="inpRut"]/@value'))
		pasaporte = cleanXpathResponse(root.xpath('//input[@id="inpPasaporte"]/@value'))
		primerNombre = cleanXpathResponse(root.xpath('//input[@id="inpNombre1"]/@value'))
		segundoNombre = cleanXpathResponse(root.xpath('//input[@id="inpNombre2"]/@value'))
		primerApellido = cleanXpathResponse(root.xpath('//input[@id="inpApellido1"]/@value'))
		segundoApellido = cleanXpathResponse(root.xpath('//input[@id="inpApellido2"]/@value'))
		direccion = cleanXpathResponse(root.xpath('//input[@id="inpDireccion"]/@value'))
		region = cleanXpathResponse(root.xpath('//select[@id="lstRegion"]//option[@selected="selected"]/text()'))
		comuna = cleanXpathResponse(root.xpath('//select[@id="lstComuna"]//option[@selected="selected"]/text()'))
		ciudad = cleanXpathResponse(root.xpath('//input[@id="inpCiudad"]/@value'))
		telCasa = cleanXpathResponse(root.xpath('//input[@id="inpTelefonoCasa"]/@value'))
		telTrabajo = cleanXpathResponse(root.xpath('//input[@id="inpTelefonoTrabajo"]/@value'))
		fax = cleanXpathResponse(root.xpath('//input[@id="inpFax"]/@value'))
		codPostal = cleanXpathResponse(root.xpath('//input[@id="inpCodigoPostal"]/@value'))

		estadoCivil = cleanXpathResponse(root.xpath('//select[@id="lstEstadoCivil"]//option[@selected="selected"]/text()'))

		if(sexo == "optF"):
			sexo = "Femenino"
		else:
			sexo = "Masculino"

		nacDia = cleanXpathResponse(root.xpath('//input[@id="inpDiaNac"]/@value'))
		nacMes = cleanXpathResponse(root.xpath('//input[@id="inpMesNac"]/@value'))
		nacAno = cleanXpathResponse(root.xpath('//input[@id="inpAnoNac"]/@value'))
		mail = cleanXpathResponse(root.xpath('//input[@id="inpEmail"]/@value'))
		urlImagen = cleanXpathResponse(root.xpath('//img[@id="imagen" and @name="imagen"]/@src'))

		if(urlImagen == "../imagenes/transparente.gif"):
			imagenBase64 = ""
		else:
			urlImagen = urlImagen[2:]
			archivoImagen = cStringIO.StringIO(urllib.urlopen("http://lc.fitnet.cl" + urlImagen).read())
			imageHandler = Image.open(archivoImagen)
			imageHandler.save(str(id_usuario) + '.jpeg')
		
			imageHanlder_2 = open(str(id_usuario) + '.jpeg', 'rb')
			raw_image_data = imageHanlder_2.read()
			imagenBase64 = b64encode(raw_image_data)
		
			os.remove(str(id_usuario) + '.jpeg')

		urlSocio = urlSocio.split("=",1)[1]
		response = session.get("http://lc.fitnet.cl/planes/index.aspx?id=" + urlSocio, headers=headers, cookies=cookies)

		HTML = StringIO(response.content)

		# here goes the useful code
		ISO8859_1_html_parser = lxml.etree.HTMLParser(encoding='ISO8859-1')
		tree = lxml.etree.parse(HTML, parser=ISO8859_1_html_parser) # you can pass parse() a file-like object or an URL
		root = tree.getroot()

		idPlan = root.xpath('//td[@width=20 and @align="Center"]//font/text()')
		nombrePlan = root.xpath('//td[@width=250 and @align="Center"]//font/text()')
		duracionPlan = root.xpath('//td[@width=200 and @align="Center"]//font/text()')

		output_handler.write(str(id_usuario) + ';')
		output_handler.write(sucursal + ';')
		output_handler.write(pais + ';')
		output_handler.write(rut + ';')
		output_handler.write(pasaporte + ';')
		output_handler.write(primerNombre + ';')
		output_handler.write(segundoNombre + ';')
		output_handler.write(primerApellido + ';')
		output_handler.write(segundoApellido + ';')
		output_handler.write(direccion + ';')
		output_handler.write(region + ';')
		output_handler.write(comuna + ';')
		output_handler.write(ciudad + ';')
		output_handler.write(telCasa + ';')
		output_handler.write(telTrabajo + ';')
		output_handler.write(fax + ';')
		output_handler.write(codPostal + ';')
		output_handler.write(estadoCivil + ';')
		output_handler.write(sexo + ';')
		output_handler.write(nacDia + ';')
		output_handler.write(nacMes + ';')
		output_handler.write(nacAno + ';')
		output_handler.write(mail + ';')
		output_handler.write(imagenBase64 + ';')
		output_handler.write(tipoMembresia + ';')

		for i in range(len(idPlan)):
			tmp_idPlan = cleanXpathResponse(idPlan[i])
			tmp_nombrePlan = nombrePlan[i].encode('ISO8859-1')
			tmp_inicioPlan = cleanXpathResponse(duracionPlan[i])
			tmp_finPlan = cleanXpathResponse(duracionPlan[i+1])

			output_handler.write(tmp_idPlan + ';')
			output_handler.write(tmp_nombrePlan + ';')
			output_handler.write(tmp_inicioPlan + ';')
			output_handler.write(tmp_finPlan + ';')

		for i in range(20-len(idPlan)):
			output_handler.write(';;;')
		output_handler.write('\n')

output_handler.close()
