import flet as ft

def main(page: ft.Page):
    col1 = ft.Column(
        controls=[
            ft.ElevatedButton(text='1', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.RED, color=ft.colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20, 
        # wrap=True,
        run_spacing=50,
        width=500,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    #page.add(col1)
    page.add(ft.Container(col1, bgcolor=ft.colors.AMBER_100))
ft.app(target=main)