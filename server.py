from http.server import BaseHTTPRequestHandler
from sys import argv
import socketserver
import qrcode

# Gera o qrCode de reserva
def buyFood():
    qrcodeImg = qrcode.make(f'http://{ip}:2000/deliver')
    qrcodeImg.save('qrCode.png')
    print('\nCompra realizada com sucesso!\nApresente o QRCode no resturante.\n')

def deliverFood():
    print('QRCode confirmado!')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        # Trata a ação de compra
        if(self.path == '/buy'):
            buyFood()
        
        # Trata a ação de entrega
        elif(self.path == '/deliver'):
            deliverFood()

        self.send_response(200)

if __name__ == '__main__':
    try:
        global ip
        ip = argv[1]
    except:
        print(f'Argumentos faltando!\nUso: {argv[0]} IP')
        exit(0)

    print(f'Server is running on IP {ip}...')
    httpd = socketserver.TCPServer(("", 2000), Handler)
    httpd.serve_forever()