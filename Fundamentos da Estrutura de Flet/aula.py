import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text(value='Olá Mundo!')
    page.add(mensagem)
    page.add(ft.Text(value='Meu nome é Hebert Aragão'))


    elementos = [
        ft.Text(value='Elemento 1'),
        ft.Text(value='Elemento 2'),
        ft.Text(value='Elemento 3'),
        ft.Text(value='Elemento 4'),
        ft.Text(value='Elemento 5'),
    ]
    page.add(*elementos)
ft.app(target = main)

