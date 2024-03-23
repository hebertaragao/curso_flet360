import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.only(top=100)

    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(text='1', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.RED, color=ft.colors.WHITE),

            # ft.ElevatedButton(text='1', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            # ft.ElevatedButton(text='2', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            # ft.ElevatedButton(text='3', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),

            # ft.ElevatedButton(text='1', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            # ft.ElevatedButton(text='2', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            # ft.ElevatedButton(text='3', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        # wrap=True,
        run_spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.START,
        # expand=True,
    )
    row2 = ft.Row(
        controls=[
            ft.Image(height=200, src= 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png')
        ],
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=False,
    )
  
    page.add(row1, row2)

ft.app(target=main)