import flet as ft

def main(page: ft.page):
    page.fonts = {
       # 'Kanit': 'https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf',
        'Dragon Slayer': 'Dragon Slayer.ttf',
    }
    t1 = ft.Text(
        value = 'Olá mundo, seja bem vindo ao curso de Flet do Programador aventureiro',
        style= ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor= ft.colors.WHITE,
        color= ft.colors.BLACK,
        font_family= 'Dragon Slayer',
        italic= True,
        # max_lines=2,
        # overflow= ft.TextOverflow.ELLIPSIS,
        no_wrap=True,
        selectable=True,
        size= 30,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
    )

    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    title_style = ft.TextStyle(
        bgcolor= ft.colors.AMBER,
        color=ft.colors.RED,
        decoration=ft.TextDecoration.OVERLINE,
        decoration_color=ft.colors.RED,
        decoration_thickness=1,
        decoration_style=ft.TextDecorationStyle.SOLID,
        italic=True,
        size=50,
        weight=ft.FontWeight.W_900,
    )
    t2 = ft.Text(
        spans=[
            ft.TextSpan(text='Texto com link ', style=link_style, url='https://programadoraventureiro.com'),
            ft.TextSpan(text='Continuação do texto...'),
            ft.TextSpan(text='Texto em destaque!!!', style=title_style),
        ],
        size=40,
    )

    page.add(t1, t2)


ft.app(target=main, assets_dir= 'assets')