import flet as ft


class ConfigAppUI(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.expand = True
        self.alignment = ft.MainAxisAlignment.START
        
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
            ),
        ]
    
    def config_user(self, e):
        ...
