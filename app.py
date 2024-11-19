import flet as ft
import os
import sys
import json
from time import sleep


with open("user_data.json", mode="r", encoding="UTF-8") as file:
    user_data = json.load(file)


class Buttons_Main(ft.ElevatedButton):
    def __init__(self, text, on_click=""):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_500
        self.color = ft.colors.WHITE
        self.style = ft.ButtonStyle(overlay_color="blue800")
        self.text = text
        self.width = 150
        self.on_click = on_click


class Application:
    def __init__(self, page: ft.Page):
        self.page = page
        
        self.page.title = "3 Clue Game"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window.width = 360
        self.page.window.height = 640
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # HEADER BAR --------------------------------------------------------------
        self.bar = ft.AppBar(
            leading=ft.IconButton(ft.icons.HOME, tooltip="Tela Inicial", on_click=self.home),
            bgcolor=ft.colors.SURFACE_VARIANT,
            toolbar_height=35,
            actions=[
                ft.PopupMenuButton(tooltip="Configurações",
                    items=[
                        ft.PopupMenuItem(text="Preferências"),
                        ft.PopupMenuItem(),
                        ft.PopupMenuItem(text="Sair"),
                    ],
                ),
            ],
        )
        self.page.appbar = self.bar
        
        # MODAL REGRAS -------------------------------------------------------------------------
        self.rules_modal = ft.AlertDialog(
            modal=True,
            alignment=ft.alignment.center,
            title=ft.Text("Regras do Jogo", font_family="Lilita One",
                          text_align=ft.TextAlign.CENTER),
            content=ft.Column(
                width=200,
                height=100,
                controls=[
                    ft.Divider(height=1, color="white"),
                    ft.Text("DESCUBRA A PALAVRA SECRETA, USANDO ATÉ 03 DICAS!",
                            font_family="Bauhaus 93", size=16,
                            text_align=ft.TextAlign.CENTER),
                ]
            ),
            actions=[
                ft.TextButton("Entendi", on_click=lambda e: self.page.close(self.rules_modal)),
            ],
        )
        # --------------------------------------------------------------------------------------
        
        self.page.add(
            self.build(),
        )
    
    def home(self, e):
        self.page.clean()
        self.page.add(self.build())
    
    def edit_user(self, e):
        from UI_editUser import EditUser
        
        self.page.clean()
        self.page.add(EditUser(self.page))
    
    def restart_app(self, e):
        self.page.window.destroy()
        sleep(0.5)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    def button_Continuar(self, e):
        from UI_gameSolo import UI_GameSolo2
        
        with open("word_list_copy.json", mode="r", encoding="UTF-8") as file:
            words = json.load(file)
        if not words:
            end_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("FIM DE JOGO!"),
                content=ft.Text("Palavras zeradas..."),
                actions=[ft.TextButton(
                    "Continuar", on_click=lambda _: self.page.close(end_modal)),
                ],
            )
            self.page.open(end_modal)
        else:
            self.page.clean()
            self.page.add(UI_GameSolo2(self.page))
    
    def button_NovoJogo(self, e):
        with open("user_data.json", mode="r", encoding="UTF-8") as file:
            user_data = json.load(file)
        
        if user_data["words_played"][1] > 0:
            self.alert_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("Novo Jogo", font_family="Lilita One",
                              text_align=ft.TextAlign.CENTER),
                content=ft.Text(
                    "Isso reiniciará seu jogo, zerando sua pontuação. \n\nDeseja continuar?",
                    font_family="Baskerville Old Face", size=18),
                actions=[
                    ft.TextButton(text="Confirmar", on_click=self.new_game),
                    ft.TextButton(text="Cancelar", 
                                  on_click=lambda _: self.page.close(self.alert_modal)),
                ]
            )
            self.page.open(self.alert_modal)
        else:
            self.new_game(e)
    
    def new_game(self, e):
        from UI_gameSolo import UI_GameSolo2
        from gameSolo import restart_game
        
        if e.control.text == "Confirmar":
            self.page.close(self.alert_modal)
            sleep(0.5)
        
        self.page.overlay.append(
            ft.Container(
                alignment=ft.alignment.center,
                width=360,
                height=640,
                content=ft.CupertinoActivityIndicator(
                    radius=50, color=ft.colors.BLUE, animating=True
                )
            )
        )
        self.main_container.opacity = 0.30
        self.page.update()
        sleep(3)
        self.page.overlay.clear()
        self.main_container.opacity = 1
        self.page.update()
        
        restart_game()
        self.page.clean()
        self.page.add(UI_GameSolo2(self.page))
    
    # BUILD HOME -----------------------------------------------------------------------------------------
    def build(self):
        with open("user_data.json", mode="r", encoding="UTF-8") as file:
            user_data = json.load(file)
        
        self.btn_continuar = ft.ElevatedButton(
            text="Continuar",
            width=150,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_500,
            on_click=self.button_Continuar,
            disabled=True,
            opacity=0.6,
            style=ft.ButtonStyle(overlay_color="blue800")
        )
        if user_data["words_played"][1]:
            self.btn_continuar.disabled = False
            self.btn_continuar.opacity = 1
        
        self.main_container = ft.Container(
            width=360,
            height=640,
            margin=ft.margin.only(top=-10, left=-10, right=-10),
            content=ft.Stack([
                ft.Image(
                    src="images/fundo_letras2.jpg",
                    fit=ft.ImageFit.COVER,
                    height=570,
                    opacity=0.2
                ),
                ft.Container(
                    width=360,
                    height=640,
                    margin=ft.margin.only(top=25),
                    content=ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=-20),
                                width=250,
                                height=35,
                                alignment=ft.alignment.center,
                                border_radius=ft.border_radius.all(20),
                                border=ft.border.only(bottom=ft.border.BorderSide(3)),
                                image_src="images/logo.png"
                            ), 
                            
                            ft.Text("Bem Vindo!", size=20, weight="bold"),
                            ft.Container(
                                width=100,
                                height=100,
                                border_radius=ft.border_radius.all(100),
                                bgcolor="white",
                                alignment=ft.alignment.center,
                                content=ft.Image(src=user_data["avatar"],
                                                 fit=ft.ImageFit.COVER,
                                                 width=150,
                                                ),
                                on_click=self.edit_user,
                                tooltip="Editar Perfil"
                            ),
                            ft.Text(user_data["user"], 
                                    font_family="DaddyTimeMono Nerd Font",
                                    size=16, weight="bold"),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        width=95,
                                        height=100,
                                        bgcolor="white",
                                        border=ft.border.all(1, "BLUE"),
                                        border_radius=ft.border_radius.only(
                                            top_left=5, top_right=5,
                                            bottom_left=50, bottom_right=50),
                                        gradient=ft.PaintLinearGradient(
                                            begin=ft.alignment.top_center,
                                            end=ft.alignment.bottom_center,
                                            colors=[ft.colors.BLUE, ft.colors.BLUE_900],
                                        ),
                                        padding=5,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    width=30,
                                                    height=30,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Image(
                                                        src="images/fire.png")
                                                ),
                                                ft.Text(user_data["record"][1],
                                                        color=ft.colors.BLACK, size=20, weight="bold"),
                                                ft.Text("Melhor Score",
                                                        color=ft.colors.BLACK, size=10, weight="bold"),
                                            ],
                                        )
                                    ),

                                    ft.Container(
                                        width=95,
                                        height=115,
                                        bgcolor="white",
                                        border=ft.border.all(1, "PURPLE"),
                                        border_radius=ft.border_radius.only(
                                            top_left=5, top_right=5,
                                            bottom_left=50, bottom_right=50),
                                        padding=-13,
                                        gradient=ft.PaintLinearGradient(
                                            begin=ft.alignment.top_center,
                                            end=ft.alignment.bottom_center,
                                            colors=[ft.colors.PURPLE, ft.colors.PINK_900],
                                        ),
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    width=50,
                                                    height=50,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Image(
                                                        src="images/stars.png")
                                                ),
                                                ft.Text(
                                                    user_data["words_played"][2],
                                                    color=ft.colors.BLACK, size=20, weight="bold"),
                                                ft.Text(
                                                    "   Palavras\nDescobertas",
                                                    color=ft.colors.BLACK, size=10, weight="bold"),
                                            ],
                                        )
                                    ),

                                    ft.Container(
                                        width=95,
                                        height=100,
                                        bgcolor="white",
                                        border=ft.border.all(1, "YELLOW"),
                                        border_radius=ft.border_radius.only(
                                            top_left=5, top_right=5,
                                            bottom_left=50, bottom_right=50),
                                        padding=5,
                                        gradient=ft.PaintLinearGradient(
                                            begin=ft.alignment.top_center,
                                            end=ft.alignment.bottom_center,
                                            colors=[ft.colors.YELLOW, ft.colors.GREEN_500],
                                        ),
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    width=30,
                                                    height=30,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Image(
                                                        src="images/coin.png")
                                                ),
                                                ft.Text(user_data["score"],
                                                    color=ft.colors.BLACK, size=20, weight="bold"),
                                                ft.Text("Pontuação",
                                                    color=ft.colors.BLACK, size=10, weight="bold"),
                                            ],
                                        )
                                    ),
                                ],
                            ),

                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Column(
                                    controls=[
                                        self.btn_continuar,
                                        Buttons_Main(text="Novo Jogo", on_click=self.button_NovoJogo),
                                        Buttons_Main(text="Duelo"),
                                        Buttons_Main(text="Regras", 
                                                     on_click=lambda e: self.page.open(self.rules_modal)),
                                    ]
                                ),
                            ),
                        ],
                    ),
                )
            ]),
        )
        return self.main_container
    # ----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    ft.app(target=Application, assets_dir="Assets")
