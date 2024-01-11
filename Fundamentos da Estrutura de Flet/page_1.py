import flet as ft

def main(page: ft.Page):

# alterar a cor de fundo
    #page.bgcolor = 'green'

    # alterar cor por Hexadecimal
    #page.bgcolor = '#B12B12'

    # cores imbutidas
    page.bgcolor = ft.colors.BLUE

    # alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND

    # espaço entre os elementos
    page.padding = 20
    page.spacing = 10

    # titulo do aplicativo
    page.title = 'Flet App'

    # coloca a tela sempre em primeiro plano
    page.window_always_on_top = True

    # esconder ou não a barra de títulos
    page.window_title_bar_hidden = False

    # esconder ou não os botões de maximizar, minimizar e fechar
    page.window_frameless = False

    # iniciar o aplicativo em tela cheia
    page.window_full_screen = False

    # alterar tamanho da tela = altura
    page.window_height = 300

    # tamanho máximo da tela = altura
    page.window_max_height =900

    # tamnho mínimo que a tela terá = altura
    page.window_min_height = 200

    # alterar tamanho da tela = largura
    page.window_width = 600

    # tamanho máximo de tela = largura
    page.window_max_width = 900

    # tamanho mínimo de tela = largura
    page.window_min_width = 200

    # desativar opção de redimensionamento da janela
    page.window_resizable = True

    # modificar aonde o aplicativo vai iniciar
    page.window_top = 100
    page.window_left = 100
    page.window_movable = True

    # previnir que o usuário não feche a aplicação
    page.window_prevent_close = True

    # barra de progresso para o usuario saber que finalizou a aplicação
    page.window_progress_bar = 1

    # Qual plataforma está rodando
    print(page.platform)

    def page_resize(e):
        print('Tamanho: ', page.window_width, page.window_height)
    page.on_resize = page_resize

    def on_window_event(e):
        match e.data:
            case 'moved':
                print('Moveu a página')
            case 'resized':
                print('Redimensionou a página')
            case 'minimize':
                print('Minimizou')
            case _:
                print('Outra ação')

    page.on_window_event = on_window_event

    page.add(
        ft.Text(value='Olá Mundo!'),
        ft.Container(ft.Text(value='Olá Mundo'), bgcolor='black')
        )

    page.update()

ft.app(target= main)