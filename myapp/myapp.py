"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from myapp.views.form import passwordForm
from myapp.components.getPasswords import MainClass


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.center(
            rx.vstack(
                passwordForm(),  
            ),
            margin="2em"
        ),
        
        rx.center(
            rx.text(
                MainClass.pwd,
                size="6"),
            ),
        
        size="4",
    )


app = rx.App()
app.add_page(index)
