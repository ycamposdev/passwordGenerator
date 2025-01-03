"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from myapp.views.form import passwordForm
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.center(
            passwordForm()
        ),
        size="1"
    )


app = rx.App()
app.add_page(index)
