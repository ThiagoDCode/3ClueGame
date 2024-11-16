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
        self.bgcolor = ft.colors.BLUE_900
        self.color = ft.colors.WHITE70
        self.text = text
        self.width = 150
        self.on_click = on_click


class Application:
    def __init__(self, page: ft.Page):
        self.page = page
        
        self.page.title = "3 Clue Game"
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
                        ft.PopupMenuItem(text="Preferências", on_click=self.configs_app),
                        ft.PopupMenuItem(),
                        ft.PopupMenuItem(text="ITEM 2"),
                    ],
                ),
            ],
        )
        self.page.appbar = self.bar
        
        # MODAL REGRAS -------------------------------------------------------------------------
        self.rules_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Regras do Jogo"),
            content=ft.Text("Descubra a palavra secreta, usando até 03 dicas!"),
            actions=[
                ft.TextButton("Continuar", on_click=lambda e: self.page.close(self.rules_modal)),
            ],
        )
        # --------------------------------------------------------------------------------------

        self.page.add(
            self.build(),
        )
    
    def home(self, e):
        self.page.clean()
        self.page.add(self.build())
    
    def configs_app(self, e):
        from configs_app import ConfigAppUI
        self.page.clean()
        self.page.add(ConfigAppUI(self.page))
    
    def edit_user(self, e):
        from UI_editUser import EditUser
        
        self.page.clean()
        self.page.add(EditUser(self.page))
    
    def restart_app(self, e):
        self.page.window.destroy()
        sleep(0.5)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    # def continued(self, e):
    #     from game_ui import GameUI_Solo
        
    #     if not words:
    #         print("sem palavras")
    #         endGame_modal = ft.AlertDialog(
    #             modal=True,
    #             title=ft.Text("Fim de Jogo"),
    #             content=ft.Text("Palavras zeradas"),
    #             actions=[
    #                 ft.TextButton("Novo Jogo", on_click=lambda e: self.page.close(endGame_modal)),
    #                 ft.TextButton("Continuar", on_click=lambda e: self.page.close(endGame_modal))
    #             ]
    #         )
    #         self.page.open(endGame_modal)
    #     else:
    #         self.page.clean()
    #         self.page.add(GameUI_Solo(self.page))
    
    def button_NovoJogo(self, e):
        with open("user_data.json", mode="r", encoding="UTF-8") as file:
            user_data = json.load(file)
        
        if user_data["words_win"] > 0:
            self.alert_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirmar novo Jogo"),
                content=ft.Text(
                    "Isso reiniciará seu jogo, zerando sua pontuação. \n\nDeseja continuar?"),
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
        
        restart_game()
        self.page.clean()
        self.page.add(UI_GameSolo2(self.page))
    
    # BUILD HOME -----------------------------------------------------------------------------------------
    def build(self):
        with open("user_data.json", mode="r", encoding="UTF-8") as file:
            user_data = json.load(file)
        
        main_container = ft.Container(
            width=360,
            height=640,
            margin=ft.margin.only(top=-10),
            content=ft.Column(
                horizontal_alignment="center",
                controls=[
                    ft.Text("Bem Vindo!", size=20, weight="bold"),
                    ft.Container(
                        width=100,
                        height=100,
                        border_radius=ft.border_radius.all(100),
                        bgcolor="white",
                        alignment=ft.alignment.center,
                        content=ft.Image(src="images/avatar.png",
                                         fit=ft.ImageFit.COVER,
                                         width=150,
                                        ),
                        on_click=self.edit_user,
                        tooltip="Editar Perfil"
                    ),

                    ft.Text(user_data["user"], weight="bold"),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=95,
                                height=100,
                                bgcolor="white",
                                border_radius=ft.border_radius.only(bottom_left=50, bottom_right=50),
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
                                        ft.Text("5", color=ft.colors.BLACK,size=20, weight="bold"),
                                        ft.Text("Melhor Score", color=ft.colors.BLACK, size=10, weight="bold"),
                                    ],
                                )
                            ),

                            ft.Container(
                                width=95,
                                height=100,
                                bgcolor="white",
                                border_radius=ft.border_radius.only(bottom_left=50, bottom_right=50),
                                padding=-13,
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            width=50,
                                            height=50,
                                            alignment=ft.alignment.center,
                                            content=ft.Image(src="images/stars.png")
                                        ),
                                        ft.Text("5", color=ft.colors.BLACK, size=20, weight="bold"),
                                        ft.Text("   Palavras\nDescobertas", 
                                                color=ft.colors.BLACK, size=10, weight="bold"),
                                    ],
                                )
                            ),

                            ft.Container(
                                width=95,
                                height=100,
                                bgcolor="white",
                                border_radius=ft.border_radius.only(bottom_left=50, bottom_right=50),
                                padding=5,
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            width=30,
                                            height=30,
                                            alignment=ft.alignment.center,
                                            content=ft.Image(src="images/coin.png")
                                        ),
                                        ft.Text("5", color=ft.colors.BLACK, size=20, weight="bold"),
                                        ft.Text("Pontuação", color=ft.colors.BLACK, size=10, weight="bold"),
                                    ],
                                )
                            ),
                        ],
                    ),

                    ft.Container(
                        margin=ft.margin.only(top=40),
                        content=ft.Column(
                            controls=[
                                Buttons_Main(text="Continuar"),
                                Buttons_Main(text="Novo Jogo", on_click=self.button_NovoJogo),
                                Buttons_Main(text="Duelo"),
                                Buttons_Main(text="Regras", on_click=lambda e: self.page.open(self.rules_modal)),
                            ]
                        ),
                    ),
                ],
            ),
        )
        return main_container
    # ----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    ft.app(target=Application, assets_dir="Assets")
