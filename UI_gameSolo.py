import flet as ft
from time import sleep
from gameSolo import GameSolo
from app import Application


class ContainerTip(ft.Container):
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
        self.visible = False


class UI_GameSolo2(ft.Column, GameSolo):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        self.expand = True
        self.alignment = ft.MainAxisAlignment.END
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.containerTip1 = ContainerTip(
            tip_score="10", tip_text=self.tips_word[0].upper(), margin=-80)
        self.containerTip1.visible = True
        self.containerTip2 = ContainerTip(
            tip_score="8", tip_text=self.tips_word[1].upper())
        self.containerTip3 = ContainerTip(
            tip_score="6", tip_text=self.tips_word[2].upper(), margin=80)
        
        self.user_entry = ft.Ref[ft.TextField()]

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
                        
                        self.containerTip1,
                        self.containerTip2,
                        self.containerTip3,
                        
                        ft.Container(
                            margin=ft.margin.only(top=30),
                            alignment=ft.alignment.center,
                            content=ft.TextField(
                                ref=self.user_entry,
                                width=220,
                                border_color="transparent",
                                expand=True,
                                hint_text="Qual é a palavra?",
                                hint_style=ft.TextStyle(color="#272B30"),
                                color="black",
                                bgcolor="#B9BABB",
                            ),
                        ),
                        
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.ElevatedButton(text="Responder",
                                                  width=135, on_click=self.button_responder),
                                ft.ElevatedButton(text="Próxima dica",
                                                  width=135, on_click=self.button_nextTip),
                            ],
                        ),
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
    
    def button_responder(self, e):
        if self.user_entry.current.value.lower() == self.word_selected.lower():
            if self.containerTip3.visible:
                self.score = 6
            elif self.containerTip2.visible:
                self.score = 8
            else:
                self.score = 10
        
            self.win_modal = ft.AlertDialog(
                alignment=ft.alignment.center,
                modal=True,
                title=ft.Text("PARABÉNS, ACERTOU!"),
                content=ft.Text(f"{self.word_selected} \nganho {self.score}"),
                actions=[
                    ft.TextButton("Menu", on_click=self.home, key="win"),
                    ft.TextButton("Próxima Palavra", key="win", 
                                  on_click=self.button_nextWord),
                ],
            )
            self.page.open(self.win_modal)
            
            self.result_game(record=True, score_win=self.score)
        else:
            self.result_game(record=False)
            self.lose_modal = ft.AlertDialog(
                alignment=ft.alignment.center,
                modal=True,
                title=ft.Text("ERROU!"),
                content=ft.Text(f"ERROU"),
                actions=[
                    ft.TextButton("Menu", on_click=self.home, key="lose"),
                    ft.TextButton("Próxima Palavra", key="lose", 
                                  on_click=self.button_nextWord),
                ],
            )
            self.page.open(self.lose_modal)
    
    def button_nextTip(self, e):
        if self.containerTip2.visible:
            self.containerTip3.visible = True
        self.containerTip2.visible = True
        
        self.page.update()
    
    def button_nextWord(self, e):
        if e.control.key == "win":
            self.page.close(self.win_modal)
        else:
            self.page.close(self.lose_modal)
        
        sleep(1)
        print("PRÓXIMA PALAVRA >>>")
        
        if not self.words:
            print("SEM PALAVRAS")
            self.end_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("FIM DE JOGO!"),
                content=ft.Text("Palavras zeradas..."),
                actions=[
                    ft.TextButton("Continuar", on_click=self.home, key="end"),
                ],
            )
            self.page.open(self.end_modal)
        else:
            self.page.clean()
            self.page.add(UI_GameSolo2(self.page))
            sleep(1)
    
    def home(self, e):
        if e.control.key == "win":
            self.page.close(self.win_modal)
        elif e.control.key == "lose":
            self.page.close(self.lose_modal)
        else:
            self.page.close(self.end_modal)
        sleep(0.5)
        
        self.page.clean()
        Application(self.page).home(e)
