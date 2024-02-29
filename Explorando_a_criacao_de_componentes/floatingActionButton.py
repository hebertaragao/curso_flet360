import flet as ft

def main(page: ft.Page):
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREEN,
        mini=False,
        shape=ft.RoundedRectangleBorder(radius=10),
        tooltip='Cadastrar um novo produto',
        #text='Adicionar',
        on_click=lambda _: print('Fui clicado'),
    )
    page.update()

ft.app(target=main)