import flet as ft
from time import sleep
from app import Application
from back_end import Game_Solo
from back_end import words


class GameUI_Solo(ft.Container, Game_Solo, Application):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        self.width = 360
        self.height = 640
        self.expand = True
        self.margin = ft.margin.only(top=70)

        self.word_selected, self.tips_word = self.play_word()
        print(self.word_selected)
        print(self.tips_word)
        
        self.user_entry = ft.Ref[ft.TextField()]

        self.count_word = ft.Text(value=f"Palavra {self.words_played}/{self.total_words}",
                                  font_family="Century Gothic",
                                  size=20, weight="bold")
        
        self.tip1 = ft.Text(value=self.tips_word[0].upper(), color="black", weight="bold")
        self.tip2 = ft.Text(value=self.tips_word[1].upper(), color="black", weight="bold")
        self.tip3 = ft.Text(value=self.tips_word[2].upper(), color="black", weight="bold")
        
        # CONTAINERS DICAS --------------------------------------------------------------
        self.container1 = ft.Container(
            margin=ft.margin.only(left=-80),
            width=200,
            height=30,
            border_radius=ft.border_radius.all(15),
            bgcolor=ft.colors.GREY_100,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=30, height=30,
                        border_radius=ft.border_radius.all(
                            15),
                        bgcolor=ft.colors.AMBER_500,
                        content=ft.Text(
                            "10", size=16, color="black", weight="bold")
                    ),
                    self.tip1,
                    # ft.Text("Dica 1", color="black", weight="bold"),
                ],
            ),
        )
        
        self.container2 = ft.Container(
            width=200,
            height=30,
            border_radius=ft.border_radius.all(15),
            bgcolor=ft.colors.GREY_100,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=30, height=30,
                        border_radius=ft.border_radius.all(
                            15),
                        bgcolor=ft.colors.AMBER_500,
                        content=ft.Text(
                            "8", size=16, color="black", weight="bold")
                    ),
                    self.tip2,
                    # ft.Text("Dica 2", color="black", weight="bold"),
                ],
            ),
            visible=False,
        )
        
        self.container3 = ft.Container(
            margin=ft.margin.only(right=-80),
            width=200,
            height=30,
            border_radius=ft.border_radius.all(15),
            bgcolor=ft.colors.GREY_100,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=30, height=30,
                        border_radius=ft.border_radius.all(
                            15),
                        bgcolor=ft.colors.AMBER_500,
                        content=ft.Text(
                            "6", size=16, color="black", weight="bold")
                    ),
                    self.tip3,
                    # ft.Text("Dica 3", color="black", weight="bold"),
                ],
            ),
            visible=False,
        )
        # -------------------------------------------------------------------------------
        
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
                                content=self.count_word,
                            ),
                            
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                alignment=ft.alignment.center,
                                content=ft.Text("A dica é:")
                            ),
                            
                            self.container1,
                            self.container2,
                            self.container3,
                            
                            ft.Container(
                                margin=ft.margin.only(top=30),
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    spacing=25,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            ref=self.user_entry,
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
                                                ft.ElevatedButton(text="Responder", 
                                                                  width=135, on_click=self.answer_word),
                                                ft.ElevatedButton(text="Próxima dica", 
                                                                  width=135, on_click=self.next_tip)
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
    
    def answer_word(self, e):
        if self.user_entry.current.value.lower() == self.word_selected.lower():
            if self.container3.visible:
                self.score_win = 6
            elif self.container2.visible:
                self.score_win = 8
            else:
                self.score_win = 10
            
            self.win_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("ACERTOU!!!"),
                content=ft.Text(f"{self.word_selected} \n {self.score_win}"),
                actions=[
                    ft.TextButton("Menu", on_click=lambda e:self.page.close(self.win_modal)),
                    ft.TextButton("Continuar", on_click=self.next_word)
                ],
            )
            self.page.open(self.win_modal)
        
        else:
            print("ERROU!")
    
    def next_word(self, e):
        self.page.close(self.win_modal)
        sleep(1)
        
        if not words:
            print("sem palavras")
            endWord_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("FIM DE JOGO!"),
                content=ft.Text("Palavras zeradas"),
                actions=[
                    ft.TextButton("Continuar", 
                        on_click=lambda e: self.page.close(endWord_modal),
                    ),
                ],
            )
            self.page.open(endWord_modal)
            
            Application(self.page)
        else:
            self.page.clean()
            Game_Solo()
            self.page.add(GameUI_Solo(self.page))
    
    def next_tip(self, e):
        if self.container2.visible:
            self.container3.visible = True
        self.container2.visible = True
        
        self.page.update()
