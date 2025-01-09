import reflex as rx
from myapp.components.getPasswords import MainClass

def passwordForm() -> rx.Component:
    return rx.vstack(
        rx.card(
        rx.vstack(
        rx.box(
            rx.input(
                placeholder="Ingrese la cantidad",
                required=True,
                on_change=MainClass.set_c,
                type="number",
                max_length=2,
                max=2,
            ),
            width="100%"
        ),
        rx.box(
            rx.hstack(
                rx.text("Números: "),
                rx.checkbox(
                    on_change=MainClass.set_numberChecked,
                    ),
                ),
        ),
        rx.box(
            rx.hstack(
                rx.text("Caracteres especiales: "),
                rx.checkbox(
                    on_change=MainClass.set_caracterChecked,
                    ),
            )
        ),
        rx.box(
            rx.hstack(
                rx.text("Letras: "),
                rx.checkbox(
                    on_change=MainClass.set_lettersChecked,
                    )
            )
        ),
        rx.box(
            rx.hstack(
                rx.text("Mayúsculas: "),
                rx.checkbox(
                    on_change=MainClass.set_UppercaseLetterChecked,
                    )
            )
        ),
        rx.box(
            rx.button(
                "GENERAR",
                on_click=MainClass.passwordWithCheckbox,
                width="100%"
            ),
            width="100%"
        ),

        spacing="5",
        direction="column", 
    ),
        ),
    )