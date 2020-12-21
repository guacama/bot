try:
    import sqlite3
    import hashlib
    import smtplib
    from email.message import EmailMessage as msg
    import os
    import asistente
    

except Exception as e:
    print('Debe de instalar el modulo' + str(e))


class BBDManager():
    def __init__(self):
        #SE CREA LA CONEXION Y EL CURSOR
        self.conexion = sqlite3.connect('Manager.db')
        self.cursor = self.conexion.cursor()
        self.USUARIO = os.environ.get('Usuario')
        self.PASS = os.environ.get('Contra')
        self.mensaje = msg()
        self.bot = asistente.Asistente()
        try:
            #SE CREA LA TABLA
            self.cursor.execute(
                '''CREATE TABLE MANAGER(
                    CLAVE INTEGER PRIMARY KEY AUTOINCREMENT,
                    URL text ,
                    DOMINIO text,
                    USUARIO text,
                    CONTRA text)''')
            #SI LA TABLA YA EXISTE SE PROCEDE A INSERTAR EL CONTENIDO
        except:
            print('.............✔✔✔...............')

    def Insertar(self):
        #SE INSERTAN LOS DATOS EN LA BBD
        try:
            self.url = input("Escriba la URL-->")
            self.dominio = input("Escriba el dominio-->")
            self.usuario = input('Escriba su usuario-->')
            print('-------------------------------------------')
            print('Escriba una contraseña corta porfavor')
            print()
            self.contra = input("Escriba una contraseña-->")
            #SE ENCRIPTA LA CONTRASENA
            self.cifrado = hashlib.new('sha1', self.contra.encode())
            print("Su contraseña es -->", self.cifrado.hexdigest())
            self.bbd = [(self.url,self.dominio,self.usuario,self.cifrado.hexdigest())]
            #SE GUARDAN LOS DATOS  
            self.cursor.executemany("INSERT INTO MANAGER VALUES (null,?,?,?,?)", self.bbd)
            self.conexion.commit()
            self.bot.Hablar('Datos insertados correctamente')
            
            #ENVIANDO LA CLAVE AL CORREO
            self.contenido = f"Esta es la clave de {self.url}:\n{self.cifrado.hexdigest()}\n\nCada vez que quieras ver tu contraseña ve a la BBD\n\nUn mensaje de tu bot preferido"
            self.mensaje['Subject'] = f'Clave de {self.dominio}'
            self.mensaje['From'] = self.USUARIO
            self.mensaje['To'] = 'popeyeseal@gmail.com', self.USUARIO
            self.mensaje.set_content(self.contenido)
            self.conexion = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.conexion.login(self.USUARIO,self.PASS)
            self.conexion.send_message(self.mensaje)
            self.conexion.quit()
            self.bot.Hablar("Le acabo de enviar un correo con su clave jefe")
        
        except Exception as e:
            print('A ocurrido un error..' + str(e))   


    def Visualizar(self):
        self.cursor.execute("SELECT * FROM MANAGER")
        self.imprimir = self.cursor.fetchall()
        for i in self.imprimir:
            print(f"La clave es ->{i[0]} | La URL es ->{i[1]} | El Dominio es -> {i[2]} | Su Usuario es -> {i[3]} | Su Contraseña es {i[4]} ")


    def Eliminar(self):
        self.clave = input("Escriba la Clave del sitio que quiere eliminar-->")
        self.cursor.execute(f"DELETE FROM MANAGER WHERE CLAVE='{self.clave}'")
        self.conexion.commit()
        self.bot.Hablar(f'Se elimino el sitio de la base de datos miop')



