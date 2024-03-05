import flet as ft
def main(page: ft.Page):
    btn1 = ft.TextButton(
        text='Editar',
        icon= ft.icons.EDIT,
        icon_color=ft.colors.RED,
        tooltip='Clique aqui para editar o texto',
        url='https://programadoraventureiro.com',
        style=ft.ButtonStyle(color=ft.colors.WHITE),
        on_click=lambda _: print('Editando o conteúdo...'),
    )
    
    page.add(btn1)
ft.app(main)