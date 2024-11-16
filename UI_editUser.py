import flet as ft
import json


with open("user_data.json", mode="r", encoding="UTF-8") as file:
    user_data = json.load(file)


class EditUser(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        self.expand = True
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.user_nick_entry = ft.Ref[ft.TextField()]
        
        self.controls = [
            ft.Container(
                width=350,
                height=200,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE,
                content=ft.Text("GRADE DE AVATARES"),
            ),
            
            ft.Text("Nick-Name", size=16, weight="bold"),
            ft.Container(
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=30),
                content=ft.TextField(
                    ref=self.user_nick_entry,
                    width=220,
                    border_color="transparent",
                    expand=True,
                    value=user_data["user"],
                    color="black",
                    bgcolor="#B9BABB",
                ),
            ),
            
            ft.ElevatedButton(text="Salvar", on_click=self.button_save)
        ]
    
    def button_save(self, e):
        if self.user_nick_entry.current.value == "":
        
            nick_alert = ft.BottomSheet(
                content=ft.Container(
                    padding=35,
                    content=ft.Column(
                        tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Por favor digite seu nick-name"),
                            ft.ElevatedButton("OK", on_click=lambda _: self.page.close(nick_alert))
                        ]
                    ),
                ),
            )
            self.page.open(nick_alert)
        else:
            user_data["user"] = self.user_nick_entry.current.value

            with open("user_data.json", mode="w", encoding="UTF-8") as save:
                save.write(json.dumps(user_data, ensure_ascii=False, indent=4))
            
            nick_alert = ft.BottomSheet(
                content=ft.Container(
                    padding=35,
                    content=ft.Column(
                        tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Salvo com sucesso!"),
                            ft.ElevatedButton("OK", on_click=lambda _: self.page.close(nick_alert))
                        ]
                    ),
                ),
            )
            self.page.open(nick_alert)
