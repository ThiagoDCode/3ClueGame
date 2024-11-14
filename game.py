import flet as ft


class Game_Solo(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.width = 360
        self.height = 640
        self.expand = True,
        self.margin = ft.margin.only(top=70)
        
        self.content = ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Container(
                    width=310,
                    height=470,
                    border_radius=ft.border_radius.all(10),
                    bgcolor="#272B30",
                    padding=ft.padding.only(top=70),
                    content=ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Container(
                                width=200,
                                height=30,
                                border_radius=ft.border_radius.all(15),
                                bgcolor=ft.colors.BLUE_GREY,
                                alignment=ft.alignment.center,
                                content=ft.Text("Palavra 8/100",
                                                font_family="Century Gothic", 
                                                size=20, weight="bold")
                            ),
                            
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                alignment=ft.alignment.center,
                                content=ft.Text("A dica é:")
                            ),
                            
                            ft.Container(
                                margin=ft.margin.only(left=-80),
                                width=200,
                                height=30,
                                border_radius=ft.border_radius.all(15),
                                bgcolor=ft.colors.GREY_100,
                                alignment=ft.alignment.center,
                                content=ft.Text("Dica 1", color=ft.colors.BLACK)
                            ),
                            
                            ft.Container(
                                width=200,
                                height=30,
                                border_radius=ft.border_radius.all(15),
                                bgcolor=ft.colors.GREY_100,
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    "Dica 2", color=ft.colors.BLACK)
                            ),
                            
                            ft.Container(
                                margin=ft.margin.only(right=-80),
                                width=200,
                                height=30,
                                border_radius=ft.border_radius.all(15),
                                bgcolor=ft.colors.GREY_100,
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    "Dica 3", color=ft.colors.BLACK)
                            ),
                            
                            ft.Container(
                                margin=ft.margin.only(top=30),
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    spacing=25,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            width=220,
                                            border_color="transparent",
                                            expand=True,
                                            hint_text="Qual é a palavra?",
                                            hint_style=ft.TextStyle(color="#272B30"),
                                            color="black",
                                            bgcolor="#B9BABB",
                                        ),
                                        
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            controls=[
                                                ft.ElevatedButton(text="Responder", width=135),
                                                ft.ElevatedButton(text="Próxima dica", width=135)
                                            ],
                                        ),
                                    ],
                                )
                            ),
                        ],
                    )
                ),

                # Avatar
                ft.Container(
                    margin=ft.margin.only(top=-530, bottom=530),
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
            ],
        )
