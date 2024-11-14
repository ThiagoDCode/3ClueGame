import flet as ft


class Header(ft.AppBar):
    
    def build(self):
        appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.HOME),
            bgcolor=ft.colors.SURFACE_VARIANT,
            toolbar_height=35,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="ITEM 1"),
                        ft.PopupMenuItem(),
                        ft.PopupMenuItem(text="ITEM 2"),
                    ],
                ),
            ],
        )
        return appbar


class Body(ft.Container):
    
    def build(self):
        main_container = ft.Container(
            bgcolor="#272B30",
            width=360,
            height=300,
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
                    ),
                    
                    ft.Text("#Dallas", weight="bold"),
                    
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
                                            content=ft.Image(src="images/fire.png")
                                        ),
                                        ft.Text("5", color=ft.colors.BLACK, size=20, weight="bold"),
                                        ft.Text("Score", color=ft.colors.BLACK, size=10, weight="bold"),
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
                                        ft.Text("   Palavras\nDescobertas", color=ft.colors.BLACK, size=10, weight="bold"),
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
                ],
            ),
        )
        return main_container


class Buttons_Main(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_900
        self.color = ft.colors.WHITE70
        self.text = text
        self.width = 150


def main(page: ft.Page):
    page.title = "3 Clue Game"
    page.window.width = 360
    page.window.height = 640
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    head = Header().build()
    page.appbar = head
    
    page.add(
        Body().build(),
        ft.Column(
            controls=[
                Buttons_Main(text="Continuar"), 
                Buttons_Main(text="Novo Jogo"),
                Buttons_Main(text="Duelo"),
                Buttons_Main(text="Regras"),
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="Assets")
