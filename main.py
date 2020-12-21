try:
    import BBD
    import asistente 
    import subprocess
    import random
    import bot
    subprocess.run('pipenv install pyttsx3',shell=True)
 
except:
    print('Instalando los requierements.txt...')
    subprocess.run('pip install -r requirements.txt',shell=True)


IA = asistente.Asistente()
FUNCIONES_IA = asistente.IAFunciones()
BASE_DATOS = BBD


def Sistema_OP(comandos):
    R = comandos
    for spotify in bot.Sistema_op[0]['spotify']:
        if spotify in R:
            IA.Hablar('ejecutando spotify papi')
            FUNCIONES_IA.Spotify()
            break
    
    for teams in bot.Sistema_op[1]['teams']:
        if teams in R:
            IA.Hablar('Eso es una orden chulo')
            FUNCIONES_IA.Teams()
            break
    
    for google in bot.Sistema_op[2]['google']:
        if google in R:
            IA.Hablar('Abriendo google')
            FUNCIONES_IA.Google()
            break
    
    for deepsound in bot.Sistema_op[3]['deepsound']:
        if deepsound in R:
            IA.Hablar('Ejecutando la sal')
            FUNCIONES_IA.Deepsound()
            break
    
    for vscode in bot.Sistema_op[4]['vscode']:
        if vscode in R:
            IA.Hablar('Abriendo tu editor de texto')
            FUNCIONES_IA.Vscode()
            break
    
    for sqllite3 in bot.Sistema_op[5]['sqllite3']:
        if sqllite3 in R:
            IA.Hablar('Abriendo tu manejador de base de datos')
            FUNCIONES_IA.Sqllite3()
            break
    
    for virtualbox in bot.Sistema_op[6]['virtualbox']:
        if virtualbox in R:
            IA.Hablar('tato jefe')
            FUNCIONES_IA.VirtualBox()
            break
    
    for apagar_sistema in bot.Sistema_op[7]['apagar_sistema']:
        if apagar_sistema in R:
            IA.Hablar('El sistema se apagara en 30 segundos')
            FUNCIONES_IA.Sistema('apagar')
            break
    
    for reiniciar_sistema in bot.Sistema_op[8]['reiniciar_sistema']:
        if reiniciar_sistema in R:
            IA.Hablar('El sistema se reiniciara en 30 segundos')
            FUNCIONES_IA.Sistema('reiniciar')
            break
    
    for cancelar_sistema in bot.Sistema_op[9]['cancelar_sistema']:
        if cancelar_sistema in R:
            IA.Hablar('si lo vas a cancelar pa que lo dices,ma que jode,ya lo cancele')
            FUNCIONES_IA.Sistema('cancelar')
            break
    

def IAWeb(comandos):
    R = comandos
    for youtube in bot.IAWeb[0]['youtube']:
        if youtube in R:
            IA.Hablar('Que quieres buscar')
            busqueda = IA.ReconocimientoVoz()
            IA.Hablar('tato jefe')
            asistente.IAWeb().Youtube(busqueda)
            break
    
    for español in bot.IAWeb[1]['libros']['español']:
        if español in R:
            IA.Hablar('Abriendo el libro de español')
            asistente.IAWeb().Libros('español')
            break

    for sociales in bot.IAWeb[1]['libros']['sociales']:
        if sociales in R:
            IA.Hablar('Abriendo el libro de sociales')
            asistente.IAWeb().Libros('sociales')
            break
    
    for biologia in bot.IAWeb[1]['libros']['biologia']:
        if biologia in R:
            IA.Hablar('tato chulo')
            asistente.IAWeb().Libros('naturales')
            break

    for ingles in bot.IAWeb[2]['aplicaciones']['ingles']:
        if ingles in R:
            IA.Hablar('Abriendo el libro de ingles chulo')
            asistente.IAWeb().Ingles()
            break

    for matematicas in bot.IAWeb[2]['aplicaciones']['matematicas']:
        if matematicas in R:
            IA.Hablar('Abriendo la aplicacion de matematicas papi')
            asistente.IAWeb().Matematica()
            break



def Personal(comandos):
    R = comandos
    for bbd in bot.personal[0]['BBD']['palabra_clave']:
       if bbd in R:
            IA.Hablar('Que quiere hacer jefe')
            opciones = IA.ReconocimientoVoz()
            for insertar in bot.personal[0]['BBD']['insertar']:
               if insertar in opciones:
                   IA.Hablar('Mostrando opcion de insertar contenido')
                   BBD.BBDManager().Insertar()
                   break
            
            for visualizar in bot.personal[0]['BBD']['visualizar']:
               if visualizar in opciones:
                   IA.Hablar('Mostrano contenido de la base de datos')
                   BBD.BBDManager().Visualizar()
                   break

            for eliminar in bot.personal[0]['BBD']['eliminar']:
               if eliminar in opciones:
                   IA.Hablar('Mostrando opcion de eliminar contenido')
                   BBD.BBDManager().Eliminar()
                   break
            break

    for busqueda in bot.personal[1]['busqueda']:
        if busqueda in R:
            IA.Hablar('Dime lo quieres buscar')
            buscar = IA.ReconocimientoVoz()
            FUNCIONES_IA.Busqueda(buscar)
            IA.Hablar('La busqueda completa se guardo en un archivo de texto miop')

    for descarga_vid in bot.personal[3]['descarga']['descarga_vid']:
        if descarga_vid in R:
            IA.Hablar('Escribe la uereele del video')
            FUNCIONES_IA.Descarga(True,False)
            break

    for descarga_audio in bot.personal[3]['descarga']['descarga_audio']:
        if descarga_audio in R:
            IA.Hablar('Escribe la uereele del audio')
            FUNCIONES_IA.Descarga(False,True)
            break

    
    for encriptar in bot.personal[2]['criptografia']['encriptar']:
        if encriptar in R:
            IA.Hablar('Tienes una llave?')
            respuesta = IA.ReconocimientoVoz()
            if 'no' in respuesta:
                IA.Hablar('Solo introduce la ruta del archivo, la llave se generara sola')
                print('👿 NO TE OLVIDES DE GUARDAR ESTA LLAVE PARA ENCRIPTAR Y DESENCRIPTAR TUS ARCHIVOS 👿 ')
                print("⚠ ESCRIBA LA RUTA CON ESTE SIMBOLO '/' PARA EVITAR ERRORES ⚠")
                print()
                ruta = input('Escribe la ruta->')
                print('Archivo encriptado correctamente')
                FUNCIONES_IA.Encriptar(ruta)
            
            elif 'si' or 'sí' in respuesta:
                IA.Hablar('Introduce tu llave y la ruta del archivo para encriptarlo')
                print("⚠ ESCRIBA LA RUTA CON ESTE SIMBOLO '/' PARA EVITAR ERRORES ⚠")
                print()
                ruta = input('Escribe la ruta->')
                llave = input('Escribe la llave->')
                FUNCIONES_IA.Encriptar(ruta,llave)
                break
            break
    
    
    for desencriptar in bot.personal[2]['criptografia']['desencriptar']:
        if desencriptar in R:
            IA.Hablar('Introduce tu llave y la ruta del archivo para desencriptarlo')
            print("⚠ ESCRIBA LA RUTA CON ESTE SIMBOLO '/' PARA EVITAR ERRORES ⚠")
            print()
            ruta = input('Escribe la ruta->')
            llave = input('Escribe la llave->')
            FUNCIONES_IA.Desencriptar(ruta,llave)
            IA.Hablar('Archivo desencriptado correctamente')
            print("El archivo desencriptado se ha guardado en otro archivo\nLlamado 'datos_desencriptados.txt'")
            break


       
def main():
    while True:
        A = bot.interaccion[0]['palabras_claves']
        R = IA.ReconocimientoVoz()
        for palabra_clave in A:
            if R.count(palabra_clave) > 0:
                IA.Hablar('estoy lista')
                comandos = IA.ReconocimientoVoz()
                for sistema_op in bot.Sistema_op[10]['completo']:
                    if sistema_op in comandos:
                        Sistema_OP(comandos)
                        break

                for iaweb in bot.IAWeb[3]['completo']:
                    if iaweb in comandos:
                        IAWeb(comandos)
                        break

                for personal in bot.personal[4]['completo']:
                    if personal in comandos:
                        Personal(comandos)
                        break
                break
    


if __name__ == "__main__":
    main()






 

                                