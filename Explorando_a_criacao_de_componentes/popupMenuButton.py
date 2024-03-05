import flet as ft

def main(page:ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        e.control.update()


    pb = ft.PopupMenuButton(
        icon=ft.icons.MENU_BOOK,
        items=[
            ft.PopupMenuItem(text='Item 1'),
            ft.PopupMenuItem(text='Item 2', icon=ft.icons.POWER_INPUT),
            ft.PopupMenuItem(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.NOTIFICATION_IMPORTANT),
                        ft.Column(
                            controls=[
                                ft.Text(value='Hebert gostaria de enviar uma mensagem para você!', style=ft.TextThemeStyle.LABEL_LARGE, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                ft.Text(value='Olá, tudo bem? como vai o estudo do curso de flet 360? Espero que esteja aprendendo bastante.', style=ft.TextThemeStyle.LABEL_SMALL, max_lines=2,overflow=ft.TextOverflow.ELLIPSIS),
                            ],
                            width=200
                        ),
                    ],
                ),
                on_click=lambda _: print("Fui clicado"),
            ),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(
                text='Selecione esse item',
                checked=False,
                on_click=check_item_clicked,
            )
        ]
    )

    page.add(pb)

ft.app(target=main)