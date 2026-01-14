import reflex as rx
from redx_web.ui.routes import RouteImagen, Route

ANIMATE_FADE_IN_UP = "z-10 animate-fade-in-up"
BUTTON_PRIMARY = "px-8 py-4 bg-[#00edc6] text-black font-semibold rounded-md shadow-lg hover:bg-white transition-all duration-300 transform hover:scale-105 hover:shadow-xl"
BUTTON_SECONDARY = "px-8 py-4 bg-transparent border-2 border-gray-400 text-white font-semibold rounded-md hover:bg-white/10 hover:border-white transition-all duration-300"
TITLE_CLASSES = (
    "text-5xl md:text-7xl font-bold text-white tracking-tighter text-shadow-lg"
)
SUBTITLE_CLASSES = "mt-6 text-lg md:text-xl text-gray-200 max-w-2xl text-shadow"
ANIMATED_SECTION_CLASSES = "relative flex items-center justify-center w-full aspect-[4/3] scale-90 md:scale-100"


def RntireTitle(titulo1: str, titulo2: str, detalle: str, detalle2: str) -> rx.Component:
    return rx.el.div(
        rx.el.h1( titulo1,
            rx.el.span(titulo2, class_name="text-[#00f0d0]"),
            class_name=TITLE_CLASSES,
        ),
        rx.el.p( detalle,
            class_name=SUBTITLE_CLASSES,
        ),
        rx.el.p( detalle2,
            class_name=SUBTITLE_CLASSES,
        ),
        class_name=ANIMATE_FADE_IN_UP,
    )


def RntireButtons() -> rx.Component:
    return rx.el.div(
        rx.flex(
        rx.button("Consultar los precios", 
                    on_click=rx.redirect(Route.CONTACTOS.value),
                    padding_top="2%",
                    justify_content="center",
                    color_scheme="grass",
                    width="auto",
                    padding="1.5rem 3rem",
                    ),
        rx.button("Ponerse en contacto con ventas", 
                    on_click=rx.redirect(Route.CONTACTOS.value),
                    padding_top="2%",
                    justify_content="center",
                    color_scheme="grass",
                    width="auto",
                    padding="1.5rem 3rem",
                    high_contrast= False
                    ),
            spacing="4",
        ),
        class_name="mt-10 flex flex-col sm:flex-row gap-4",
    )


def AnimatedIcon() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("truck", class_name="h-16 w-16 text-teal-300"),
            class_name="absolute inset-0 flex items-center justify-center animate-pulse animation-delay-300",
        )
    )


def IconContainer() -> rx.Component:
    return rx.el.div(
        AnimatedIcon(),
        class_name="relative w-40 h-40 bg-gradient-to-br from-teal-500/20 to-purple-600/20 rounded-full shadow-2xl border border-white/10 backdrop-blur-md",
    )


def StatusBox() -> rx.Component:
    return rx.el.div(
        rx.el.p("Estado: Operativo", class_name="text-xs text-teal-300 font-semibold"),
        class_name="absolute top-8 left-0 bg-white/5 p-3 rounded-lg backdrop-blur-sm border border-white/10 shadow-lg",
    )


def BarChart() -> rx.Component:
    return rx.box(
        rx.icon("bar-chart", class_name="h-5 w-5 text-white/50"),
        rx.box(class_name="w-10 h-1 bg-purple-400/50 rounded-full ml-2"),
        class_name="absolute top-16 right-0 bg-white/5 p-3 rounded-lg backdrop-blur-sm border border-white/10 shadow-lg flex items-center",
    )


def VerticalBars() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="w-2 h-8 bg-teal-400/60 rounded-full"),
        rx.el.div(class_name="w-2 h-12 bg-teal-400/80 rounded-full ml-1.5"),
        rx.el.div(class_name="w-2 h-6 bg-teal-400/50 rounded-full ml-1.5"),
        class_name="absolute bottom-12 left-4 flex items-end",
    )


def UserLaptopIcons() -> rx.Component:
    return rx.el.div(
        rx.icon("shuffle", class_name="h-4 w-4 text-purple-300"),
        rx.el.div(
            class_name="w-10 h-10 rounded-full border-2 border-purple-400/70 flex items-center justify-center"
        ),
        rx.icon("shrink", class_name="h-4 w-4 text-purple-300"),
        class_name="absolute bottom-8 right-8 flex items-center",
    )


def AnimatedSection() -> rx.Component:
    return rx.el.div(
        IconContainer(),
        StatusBox(),
        BarChart(),
        VerticalBars(),
        UserLaptopIcons(),
        class_name=ANIMATED_SECTION_CLASSES,
    )


def inicio_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                AnimatedSection(),
                class_name="hidden lg:block relative animate-fade-in-up animation-delay-300",
            ),
            rx.el.div(
                RntireTitle(
                    "REDx Soluciones ",
                    "RDTire App ", 
                    "Administración, Control, Seguimiento, Planificación de tus vehículos y tus Llantas, en una sola aplicación", 
                    "Reduce costos y mejora la seguridad con RDTire App. Optimiza la gestión de llantas y vehículos en tiempo real."
                ), 
                RntireButtons(),
                class_name=ANIMATE_FADE_IN_UP),
            class_name="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-20 grid lg:grid-cols-2 gap-20 items-center",
        ),
        class_name="relative bg-gradient-to-br from-[#a8b2d1] via-[#495670] to-[#0a192f] overflow-hidden",
    )
 
def inicio_section2() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                RntireTitle(
                    "Te damos la bienvenida a ",
                    "REDx Soluciones ", 
                    "Somos tu socio estratégico en soluciones tecnológicas.   En REDx Soluciones, transformamos tus desafíos en oportunidades con innovación y tecnología de vanguardia.", 
                    "Impulsamos tu éxito a través de soluciones personalizadas que optimizan tus operaciones y potencian tu crecimiento."
                ), 
                class_name=ANIMATE_FADE_IN_UP
            ),
            rx.el.div(
                rx.image(src=RouteImagen.PORTADA.value, width="100%"),
                class_name="relative mx-auto",
            ),
            class_name="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-20 grid lg:grid-cols-2 gap-20 items-center",
        ),
        class_name="relative bg-gradient-to-br from-[#a8b2d1] via-[#495670] to-[#0a192f] overflow-hidden",
    )