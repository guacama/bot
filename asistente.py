#Importamos los modulos
try:
    import pyttsx3
    import speech_recognition as sr
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import subprocess
    import pafy
    import wikipedia
    from cryptography.fernet import Fernet
    from googlesearch import search
    import os

except:
    print('Debes instalar los modulos')



class Asistente():
    def __init__(self):
        pass

    def Hablar(self,texto):
        self.texto = texto
        self.motor = pyttsx3.init()
        self.voz = self.motor.getProperty('voices')
        self.motor.setProperty('voice',self.voz[3].id)
        self.motor.setProperty('rate',150)
        self.motor.setProperty('gender','neutral')

        #Decimos el texto introducido
        self.motor.say(self.texto)
        self.motor.runAndWait()

    def ReconocimientoVoz(self):
        self.r = sr.Recognizer()
        
        with sr.Microphone() as fuente:
            print("Te estoy escuchando..")
            self.r.pause_threshold = 5
            self.escucha = self.r.listen(fuente, phrase_time_limit=6)
            self.detectar = "".lower()

            try:
                self.detectar = self.r.recognize_google(self.escucha, language='es')
                print(self.detectar)
            except:
                print('No entendi nada de lo que dijiste, repite alfavol')
            
            return self.detectar.lower()



class IAFunciones(Asistente):
    def __init__(self):
        self.Abrir = lambda app:subprocess.Popen(app)
        
    def Archivos(self,archivo,materia,nombre):
        if archivo == 'word':
            if materia == 'español':
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_Lengua_espa/" + nombre + ".docx","w")
                print("archivo creado..")

            elif materia == "sociales":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/tarea_de_sociales/" + nombre + ".docx", "w")

            elif materia == "ingles":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_ingles/" + nombre + ".docx", "w")

            elif materia == "biologia":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_Biologia/" + nombre + ".docx", "w")

            else:
                print("No se pudo crear")

        elif archivo == 'powerpoint':
            if materia == 'español':
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_Lengua_espa/" + nombre + ".pptx","w")
                print("archivo creado..")

            elif materia == "sociales":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/tarea_de_sociales/" + nombre + ".pptx", "w")

            elif materia == "ingles":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_ingles/" + nombre + ".pptx", "w")

            elif materia == "biologia":
                self.archivo = open("C:/Users/HP/OneDrive/Desktop/Tarea_de_Biologia/" + nombre + ".pptx", "w")

            else:
                print("No se pudo crear")

        
    def Teams(self):
        colegio = 'C:/Users/HP/AppData/Local/Microsoft/Teams/current/Teams.exe'
        self.Abrir(colegio)


    def Spotify(self):
        spotify = 'C:/Users/HP/AppData/Roaming/Spotify/Spotify.exe'
        self.Abrir(spotify)

    def Vscode(self):
        vs = 'C:/Users/HP/AppData/Local/Programs/Microsoft VS Code/Code.exe'
        self.Abrir(vs)

    def Google(self):
        google = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        self.Abrir(google)

    def VirtualBox(self):
        virtual = 'C:/Program Files/Oracle/VirtualBox/VirtualBox.exe'
        self.Abrir(virtual)

    def Sqllite3(self):
        sql = 'C:/Program Files/DB Browser for SQLite/DB Browser for SQLite.exe'
        self.Abrir(sql)

    def Deepsound(self):
        deep = 'C:/Program Files (x86)/DeepSound 2.0/DeepSound.exe'
        self.Abrir(deep)


    def Descarga(self,video=None,audio=None):
        if video == None and audio == None:
            self.Hablar('Tienes que decirme si quieres descargar el video o el audio, pa no quillarme')
        
        elif video:
            try:
                try:
                    self.url = input("Escriba la url del video->")
                except:
                    self.Hablar("Deje las drogas y escriba la url")
                self.a = pafy.new(self.url)
                print(self.a.title,self.a.likes,self.a.length)

                self.b = self.a.streams
                for i in self.b:
                    print(f"{i.bitrate,i.extension,i.get_filesize}")
                    
                try:
                    print("Elija su opcion en numeros '1','2', '3'")
                    self.elec_Video = int(input("Elija el audio que quiere->"))
                    print("Comenzando la descarga, espere....")
                    self.b[self.elec_Video].download(filepath='C:/Users/HP/OneDrive/Desktop')
                    self.Hablar("Descarga finalizada,el video se descargo en el escritorio")
                except:
                    self.mejor = self.a.getbest()
                    print(f"Descargando el video con mayor calidad->{self.mejor} espere....")
                    self.mejor.download(filepath="C:/Users/HP/OneDrive/Desktop")
                    self.Hablar("Descarga finalizada,el video se descargo en el escritorio")
            except:
                self.Hablar("Ha ocurido un error, no se pudo descargar su video ")

        elif audio:
            try:
                try:
                    self.url_audio = input("Escriba la url del video->")
                except:
                    self.Hablar("Deje las drogas y escriba la url")

                self.a_audio = pafy.new(self.url_audio)

                print(self.a_audio.duration)

                self.b_audio = self.a_audio.audiostreams

                for i in self.b_audio:
                    print(f"{i.bitrate,i.extension,i.get_filesize}")

                try:
                    self.elec_audio = int(input("Elija el audio que quiere->"))
                    self.Hablar("Comenzando la descarga, espere")
                    self.b_audio[self.elec_audio].download(filepath='C:/Users/HP/OneDrive/Desktop')
                    self.Hablar("Descarga finalizada,el video se descargo en el escritorio")
                except:
                    self.bestaudio = self.a.getbestaudio()
                    print(self.bestaudio.bitrate,self.bestaudio.extension,self.bestaudio.get_filesize)
                    print("Se a elejido el mejor audio...")
                    self.bestaudio.download(filepath="C:/Users/HP/OneDrive/Desktop")
                    self.Hablar("Descarga finalizada,el video se descargo en el escritorio")

            except:
                self.Hablar('Ocurrio un error mio,ni pa eso sirves')

    def Busqueda(self, busqueda):
        #Buscamos en wikipedia
        wikipedia.set_lang('es')
        summary = wikipedia.summary(busqueda)
        print(summary)
        buscar = wikipedia.page(busqueda)
        abrir_archivo = open(busqueda + ".txt",'wb')
        for links in buscar.references:
            a = links
        contenido = "{}\n\n\nLinks:{}".format(buscar.content,a).encode()
        abrir_archivo.write(contenido)
        abrir_archivo.close()



        
    def Encriptar(self,ruta,llave=None):
        try:
            if llave == None:
                #Usar el codigo comentado en caso de no tener clave
                #Se crea la clave y se guarda en un archivo
                llave = Fernet.generate_key()
                with open('llave.txt', 'wb') as clave:
                    clave.write(llave)
                    clave.close()
                
                with open('llave.txt', 'rb') as clave:
                    llave = clave.read()
                    
                #Procedemos a encriptar el archivo dado
                e = Fernet(llave)
                archivo = open(ruta,'rb').read()
                encriptar = e.encrypt(archivo)
                with open(ruta,'wb') as encriptado:
                    encriptado.write(encriptar)
                    encriptado.close()
            
            elif llave:
                e = Fernet(llave)
                archivo = open(ruta,'rb').read()
                encriptar = e.encrypt(archivo)
                with open(ruta,'wb') as encriptado:
                    encriptado.write(encriptar)
                    encriptado.close()
        
        except Exception as e:
            print('Ha ocurrido un error' + str(e))

    def Desencriptar(self,archivo,llave):

        try:
            
            with open('llave.txt', 'rb') as clave:
                llave = clave.read()

            #Procedemos a desencriptar los datos
            clave = Fernet(llave)
            with open(archivo, 'rb') as ds:
                d = ds.read()
                    
            desencriptar = clave.decrypt(d)

            #Ponemos los datos desencriptados en un archivo diferente
            with open('datos_desencriptados.txt','wb') as datos:
                datos.write(desencriptar)
                datos.close()
            
        except:
            print('Ha ocurrido un error')


    def Sistema(self,accion,segundos=None):
        
        if accion == 'apagar' and segundos:
            subprocess.run(f'shutdown /s -t {segundos}', shell=True)
        elif accion == 'apagar' and segundos == None:
            subprocess.run(f'shutdown /s -t 30', shell=True)
        
        elif accion == 'reiniciar' and segundos:
            subprocess.run(f'shutdown /r -t {segundos}', shell=True)

        elif accion == 'reiniciar' and segundos==None:
            subprocess.run(f'shutdown /r -t 30', shell=True)

        elif accion == 'cancelar':
            subprocess.run(f'shutdown /a', shell=True)


class IAWeb():
    
    def __init__(self):
        self.WEB_DRIVER = 'C:/Program Files (x86)/chromedriver.exe'
        self.driver = webdriver.Chrome(self.WEB_DRIVER)

    def Youtube(self,busqueda):
        self.driver.get('https://youtube.com')
        buscar = self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        buscar.send_keys(busqueda, Keys.ENTER)

    def Libros(self,materia=None):
        if materia == None:
            self.driver.get('https://www.blinklearning.com/login')
            self.usuario = self.driver.find_element_by_id('email')
            self.usuario.send_keys('popeyeseal@gmail.com')
            self.passw = self.driver.find_element_by_id('contrasena')
            self.passw.send_keys('jose1685', Keys.ENTER)
        else:
            self.driver.get('https://www.blinklearning.com/login')
            self.usuario = self.driver.find_element_by_id('email')
            self.usuario.send_keys('popeyeseal@gmail.com')
            self.passw = self.driver.find_element_by_id('contrasena')
            self.passw.send_keys('jose1685', Keys.ENTER)

            if materia == 'naturales':
                naturales = self.driver.find_element_by_class_name('mask')
                naturales.click()
            
            elif materia == 'sociales':
                sociales = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/ul/li[2]/div[1]/div/div')
                sociales.click()
            
            elif materia == 'español':
                espanol = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/ul/li[3]/div[1]/div/div')
                espanol.click()

            elif materia == 'matematicas':
                matematicas = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/ul/li[4]/div[1]/div/div')
                matematicas.click()
    
    def Ingles(self):
        self.driver.get('http://udpaccess.com/')
        self.usuario = self.driver.find_element_by_name('identifier')
        self.usuario.send_keys('popeyeseal@gmail.com')
        self.passw = self.driver.find_element_by_name('password')
        self.passw.send_keys('Jose1685', Keys.ENTER)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/ul/li/div/div/div/div[4]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/main/div[3]/div/ul/li/div/div[1]/div/div[1]').click()

    def Matematica(self):
        self.driver.get('https://es.khanacademy.org/login')
        self.usuario = self.driver.find_element_by_id('uid-identity-text-field-0-correo-electrnico-o-nombre-de-usuario')
        self.usuario.send_keys('josemiguel1751')
        self.passw = self.driver.find_element_by_id('uid-identity-text-field-1-contrasea')
        self.passw.send_keys('14789632', Keys.ENTER)






