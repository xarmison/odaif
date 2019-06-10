import requests as req
import cv2 as cv

# Mostra a imagem referenciada por imgPath
def show(imgPath):
    img = cv.imread(imgPath, cv.IMREAD_COLOR)

    main_win = 'QRCode da reserva'
    cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)
    cv.resizeWindow(main_win, 300, 300)

    cv.imshow(main_win, img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    
    while(1):
        # Recebe do usuária a ação que deve ser executada
        cmd = input("\nWhat to do: ")
        
        # Se a ação buy foi selecionada uma requisição
        # ao servidor na rota buy e disparada
        if(cmd == 'buy'):
            print('Realizando compra ...\n')
            try:
                req.get(f'http://localhost:2000/buy')
            except:
                pass

        # Se a ação deliver foi selecionada o sistema mostra
        # o qrCode para que ele seja escaneado
        elif(cmd == 'deliver'):
            print('Escanei o QRCode.')
            show('qrCode.png')


