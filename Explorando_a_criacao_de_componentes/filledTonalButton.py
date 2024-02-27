import flet as ft

def main(page: ft.Page):

    btn1 = ft.FilledTonalButton(text='Botão secundário')
    page.add(btn1)

    page.add(
        ft.FilledTonalButton(text='Botão secundário'),
        ft.FilledTonalButton(text='Botão secundário desabilitado', disabled=True),
        ft.FilledTonalButton(text='Botão secundário com ícone', icon=ft.icons.ADD),
        ft.FilledTonalButton(text='Botão secundário com ícone', icon=ft.icons.ADD, icon_color=ft.colors.GREEN),
        ft.FilledTonalButton(text='Botão secundário', tooltip='Ação não permitida', disabled=True ),
        ft.FilledTonalButton(text='Botão secundário com estilo',style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder())) ,
    )
ft.app(target=main)