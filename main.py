#Author: Felipe Lira
#Date: 16/02/2024
#Function: This script take a printscreen. 

import pyscreenshot as ImageGrab


def main():
    file_name = input("Input the file name for saving: ")

    imagem = ImageGrab.grab()
    imagem.save(f'{file_name}.jpg', 'jpeg')
    
if __name__ == "__main__":
    main()
