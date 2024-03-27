import flet as ft

def main(page: ft.Page):

    rrow1 = ft.ResponsiveRow(
        columns=12,
        run_spacing=50,
        spacing=20,
        expand=True,
        controls=[
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='1',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='2',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='3',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='4',
                bgcolor=ft.colors.RED,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='5',
                bgcolor=ft.colors.RED,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='6',
                bgcolor=ft.colors.RED,
                color=ft.colors.BLACK,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'xl': 2},
                text='7',
                bgcolor=ft.colors.GREEN,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'xl': 2},
                text='8',
                bgcolor=ft.colors.GREEN,
                color=ft.colors.BLACK,
            ),
             ft.ElevatedButton(
                col={'sm': 4, 'xl': 2},
                text='9',
                bgcolor=ft.colors.GREEN,
                color=ft.colors.BLACK,
            )
        ]
    )

    text = ft.Text()

    def page_size(e):
        text.value = f'Largura: {page.window_width}, Altura: {page.window_height}'
        text.update()

    page.on_resize = page_size

    page.add(rrow1, text)

ft.app(target=main)