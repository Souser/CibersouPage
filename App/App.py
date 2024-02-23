"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import App.styles.styles as styles
from App.views.navbar import navbar

def index() ->rx.Component:
    return rx.box(
        navbar()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title= "CiberSou",
    description="Probando la nueva empresa"

)
app.compile(

)