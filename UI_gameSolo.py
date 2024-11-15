import flet as ft


class MyContainer(ft.Container):
    def __init__(self, tip_score, tip_text, margin=0):
        super().__init__()
        self.margin = ft.margin.only(left=margin)
        self.width = 200
        self.height = 30
        self.border_radius = ft.border_radius.all(15)
        self.bgcolor = ft.colors.GREY_100
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    width=30, height=30,
                    border_radius=ft.border_radius.all(15),
                    bgcolor=ft.colors.AMBER_500,
                    content=ft.Text(
                        value=tip_score, size=16,
                        color="black", weight="bold",
                    ),
                ),
                ft.Text(value=tip_text, color="black", weight="bold"),
            ],
        )


class UI_GameSolo2(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        self.expand = True
        self.alignment = ft.MainAxisAlignment.END
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.controls=[
            ft.Container(
                width=350,
                height=470,
                border_radius=ft.border_radius.all(10),
                bgcolor="#272B30",
                margin=ft.margin.only(top=70),
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
                            content=ft.Text(value="PALAVRA 1/100",
                                            size=20, weight="bold"),
                        ),
                        
                        ft.Container(
                            margin=ft.margin.only(top=20),
                            alignment=ft.alignment.center,
                            content=ft.Text("A dica é:")
                        ),
                        
                        MyContainer(tip_score="10", tip_text="DICA 1", margin=-80),
                        MyContainer(tip_score="8", tip_text="DICA 2"),
                        MyContainer(tip_score="6", tip_text="DICA 3", margin=80),
                    ],
                ),
            ),
            
            # AVATAR
            ft.Container(
                margin=ft.margin.only(top=-530, bottom=530),
                # margin=ft.margin.only(top=30),
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
        ]
