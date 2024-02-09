import flet as ft 

def main(page: ft.Page):

    img = ft.Image(
        src = 'https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg',
        border_radius = ft.border_radius.all(20),
        height=500,
        width=200,
        fit=ft.ImageFit.CONTAIN,
        repeat= ft.ImageRepeat.REPEAT,
    )
    img2 = ft.Image(
        src='../assets/images/python3D.jpeg',
        tooltip='Logo do Python',
          border_radius = ft.border_radius.all(20),
        height=500,
        width=200,
        fit=ft.ImageFit.CONTAIN,
        repeat= ft.ImageRepeat.REPEAT,
    )

    page.add(img, img2)
ft.app(target=main, assets_dir='../assets')