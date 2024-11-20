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
        
        img_avatares = [
            "images/avatar.png",
            "images/avatar1.png",
            "images/avatar2.png",
            "images/avatar3.png",
            "images/avatar4.png",
            "images/avatar5.png",
        ]
        
        self.grid_avatares = ft.GridView(
            expand=True,
            max_extent=110,
            child_aspect_ratio=1,
            spacing=2,
            run_spacing=2,
        )
        for img in img_avatares:
            self.grid_avatares.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER_100,
                    border=ft.border.all(3, color="black"),
                    image_src=img,
                    on_click=self.avatar_selected,
                    opacity=0.6,
                    key=img
                ),
            )
        
        self.controls = [
            ft.Text("Perfil", font_family="Lilita One", size=20),
            ft.Container(
                width=350,
                height=215,
                padding=1,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE,
                content=self.grid_avatares
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
    
    def avatar_selected(self, e):

        for avatar in self.grid_avatares.controls:
            avatar.opacity = 0.6
            avatar.border = ft.border.all(3, color="black")
        
        e.control.opacity = 1
        e.control.border = ft.border.all(3, color="YELLOW")
        self.avatar_link = user_data["avatar"] = e.control.key
        
        self.page.update()