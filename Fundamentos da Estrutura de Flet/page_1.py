import flet as ft

def main(page: ft.Page):

# alterar a cor de fundo
    #page.bgcolor = 'green'

    # alterar cor por Hexadecimal
    #page.bgcolor = '#B12B12'

    # cores imbutidas
    page.bgcolor = ft.colors.BLUE

    # alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START

    # espaço entre os elementos
    page.padding = 20
    page.spacing = 10

    # titulo do aplicativo
    page.title = 'Flet App'


    page.add(
        ft.Text(value='Olá Mundo!'),
        ft.Container(ft.Text(value='Olá Mundo'), bgcolor='black')
        )

    page.update()

ft.app(target= main)