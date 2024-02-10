import flet as ft
def main(page: ft.Page):
    page.spacing = 50

    btn1 = ft.ElevatedButton(text='Clique aqui')
    btn2 = ft.ElevatedButton(text='Botão innativo', disabled=True)
    btn3 = ft.ElevatedButton(text='Botão com ícone', icon=ft.icons.FAVORITE)
    btn4 = ft.ElevatedButton(
        text='Demais propriedades',
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE,
        icon=ft.icons.FAVORITE_BORDER,
        icon_color=ft.colors.WHITE,
        tooltip='Olá, eu sou um botão',
        url='https://programadoraventureiro.com',
        )
    
    style = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
        },
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.PINK,
            ft.MaterialState.DISABLED: ft.colors.GREEN,
            ft.MaterialState.FOCUSED: ft.colors.RED,
            ft.MaterialState.DEFAULT: ft.colors.AMBER,
        },
        padding={
            ft.MaterialState.HOVERED: 20,
            ft.MaterialState.DEFAULT: 10,
        },
        animation_duration=1000,
        side={
            ft.MaterialState.HOVERED: ft.BorderSide(width=1, color=ft.colors.BLUE),
            ft.MaterialState.DEFAULT: ft.BorderSide(width=5, color=ft.colors.ORANGE_600),
        },
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
            ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=20),
        }

    )
    btn5 = ft.ElevatedButton(
        text='Botão com estilo personalizado',
        style=style
        )
    btn6 = ft.ElevatedButton(
        text='Outro Botão',
        style=style
        )

    page.add(btn1, btn2, btn3, btn4, btn5, btn6)

    def button_clicked(e):
        e.control.data += 1
        text.value= f'Botão acionado {e.control.data} vezes'
        text.update()
        btn.update()

    btn = ft.ElevatedButton(
        text='Botão com contagem de cliques',
        on_click=button_clicked,
        data=0,
    )
    text = ft.Text()

    page.add(btn, text)

ft.app(target=main)