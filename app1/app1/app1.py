"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://www.youtube.com/watch?v=Ci5raxp37QE"

valor=0

class State(rx.State):
    """The app state."""

class RadioState_HL(rx.State):
    text: str = "No Selection"

def radio_state_example_HL():


def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.theme(appearance="dark", has_background=False, radius="large", accent_color="cyan"),
        rx.vstack(
            rx.heading("",margin_bottom="90px"),
            rx.heading("Bienvenidos a mi web", size="9",color_scheme="orange",
            high_contrast=True),     
            rx.text("Esta pagina web fue creada para escribir articulos sobre viajes"),        
            rx.text("Elija su destino preferido: "),
            rx.radio(
                    ["Tokio", "New york", "Lima"],

                    direction="row",
                    spacing="8",
                    size="3",
                    on_change=RadioState_HL.set_text,                    
                ),
                     rx.image(
                    src="hongkong.png",
                    width="200px",
                    height="auto",
                    border_radius="40px 50px",
                    border="5px solid #555",
                    )
             

                ),
            rx.link("Que hay en Tokio?", href=docs_url ),
           rx.button(
                    rx.icon(tag="heart"),
                    "Like",
                    color_scheme="red",
                ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

    
    

app = rx.App()
app.add_page(index)
