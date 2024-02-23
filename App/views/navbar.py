import reflex as rx
from App.styles.styles import Size
def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="assets/pixel-art-retro-8-bit-poke-ball-from-pokemon-free-vector.jpg",
            width=Size.DEFAULT.value,
            height=Size.DEFAULT.value
        ),
        rx.text("Cibersou"),
        width="100%"
    )