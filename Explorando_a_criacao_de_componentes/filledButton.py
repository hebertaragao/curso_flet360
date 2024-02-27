import flet as ft

def main(page: ft.Page):
    btn1 = ft.FilledButton(text='Botão primário')
    btn2 = ft.FilledButton(
        text='Botão com ícone', 
        icon=ft.icons.STAR, 
        icon_color=ft.colors.AMBER
        )
    
    style = ft.ButtonStyle(
        padding=50,
        animation_duration=500,
        side={
            ft.MaterialState.DEFAULT:ft.BorderSide(2, ft.colors.RED),
            ft.MaterialState.HOVERED:ft.BorderSide(10, ft.colors.GREEN)
        },
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30)
        },
    )

    btn3 = ft.FilledButton(
        text='Botão personalizado',
        style= style
    )

    btn4 = ft.FilledButton(
        text='Botão com link',
        url='https://programadoraventureiro.com',
        tooltip='Clique para ir para o site oficial'
    )

    page.add(btn1, btn2, btn3, btn4)

ft.app(target=main)