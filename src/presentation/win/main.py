import flet as ft
from flet import Page, Text, Column, SubmenuButton

class MainPage: 

    def handle_menu_item_click(self,e):
        print(f"{e.control.content.value}.on_click")

    def handle_submenu_open(self,e):
        print(f"{e.control.content.value}.on_open")

    def handle_submenu_close(self,e):
        print(f"{e.control.content.value}.on_close")

    def handle_submenu_hover(self,e):
        print(f"{e.control.content.value}.on_hover")

    def handle_exit_button(self, e):
        self.page.window_close()

    def build(self, page: Page): 
        self.page = page
        self.page.window_frameless = True
        self.page.bgcolor = ft.colors.WHITE
        self.page.spacing = 0
        self.page.padding = 0
        self.setup_title()
        self.setup_menu()

    def setup_title(self):
        self.page.title = "mentorIA"

    def maximize(self):
        self.page.window_maximized = not self.page.window_maximized
        self.page.update()

    def setup_menu(self):
        self.submenu_style = ft.ButtonStyle(
                        bgcolor={
                            ft.ControlState.HOVERED: ft.Colors.with_opacity(
                                opacity=0.10,
                                color=ft.colors.BLUE_100
                            )},
                        color=ft.colors.WHITE,
                    )


        self.menu_file = ft.SubmenuButton(
            content=ft.Text("File", color=ft.colors.BLACK),
            on_open=self.handle_submenu_open,
            on_close=self.handle_submenu_close,
            on_hover=self.handle_submenu_hover,
            controls=[
                ft.MenuItemButton(
                    content=ft.Text("Quit", color=ft.colors.WHITE),
                    leading=ft.Icon(ft.Icons.CLOSE),
                    style=self.submenu_style,
                    on_click=self.handle_exit_button,
                ),
            ],
        )


        self.menu_help = ft.SubmenuButton(
            content=ft.Text("Help", color=ft.colors.BLACK),
            on_open=self.handle_submenu_open,
            on_close=self.handle_submenu_close,
            on_hover=self.handle_submenu_hover,
            controls=[
                ft.MenuItemButton(
                    content=ft.Text("About"),
                    leading=ft.Icon(ft.Icons.INFO),
                    style=self.submenu_style,
                    on_click=self.handle_menu_item_click,
                )
            ],
        )
        
        
        #appbar_text_ref = ft.Ref[ft.Text]()

        #self.page.appbar = ft.AppBar(
        #    title=ft.Text("mentorIA", ref=appbar_text_ref),
        #    center_title=True,
        #    bgcolor=ft.Colors.BLACK,
        #    color=ft.Colors.WHITE
        #)

        self.menubar = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                padding=0,
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.GREY_400,
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
            controls=[
                self.menu_file,
                self.menu_help
            ],
        )
         
        widthscr = self.page.window_width

        

        self.page.add(
            ft.ResponsiveRow([
                    ft.WindowDragArea(
                        ft.Container(
                            width=widthscr,
                            bgcolor=ft.colors.BLACK,
                            padding=15,
                            col={"sm": 6, "md": 4, "xl": 2},
                            content=ft.Row([
                                ft.Text("mentorIA", size=30),
                                ft.Container(
                                    content=ft.Row([
                                        ft.IconButton(
                                            ft.icons.CHECK_BOX_OUTLINE_BLANK, 
                                            icon_color=ft.colors.WHITE,
                                            on_click=lambda e: self.maximize()
                                        ),
                                        ft.IconButton(
                                            ft.icons.CLOSE, 
                                            icon_color=ft.colors.WHITE,
                                            on_click=lambda e: self.page.window_close()
                                        ),
                                    ])
                                )
                            ], alignment="spaceBetween") 
                    ), 
                    ),
                    self.menubar,
                    ft.Text("Hello")
                ],
            )
        )

        self.page.add(
            ft.Row([
                ft.Text("Hello", color=ft.colors.BLACK)
            ], alignment="center")
        )