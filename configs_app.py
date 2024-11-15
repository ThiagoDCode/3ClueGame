import flet as ft


class ConfigAppUI(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.expand = True
        self.alignment = ft.MainAxisAlignment.START
        # self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Configurações de Usuário"),
                        ft.Divider(height=1, color="white"),
                    ],
                ),
                on_click=self.config_user,
            ),
            ft.Container(
                margin=ft.margin.only(top=-10),
                alignment=ft.alignment.center,
                width=350,
                height=300,
                bgcolor=ft.colors.GREY,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(top=5),
                            width=310,
                            height=200,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE,
                            content=ft.Text("GRADE DE AVATARES"),
                        ),
                        
                    ]
                ),
            ),
            
            
            
            # ft.Container(
            #     width=350,
            #     height=200,
            #     alignment=ft.alignment.center,
            #     bgcolor=ft.colors.BLUE,
            #     content=ft.Text("GRADE DE AVATARES"),
            # ),
        ]
    
    def config_user(self, e):
        ...
