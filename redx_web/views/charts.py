import reflex as rx
import random

data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]
    



def chart():
    return rx.card(
        rx.heading("Metricas Generales",
                   size="6",
                   align="center",
                   width="100%"),
        rx.text("visualizacion de datos, en diferentes estilos, y de diferentes fuentes de origen excel, archivo plano, base de datos", 
                padding="1em"),
        rx.divider(),         
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8",
                x_axis_id="primary",
                y_axis_id="left",
            ),
            rx.recharts.area(
                data_key="pv",
                x_axis_id="secondary",
                y_axis_id="right",
                type_="monotone",
                stroke="#82ca9d",
                fill="#82ca9d",
            ),
            rx.recharts.x_axis(
                data_key="name", x_axis_id="primary"
            ),
            rx.recharts.x_axis(
                data_key="name",
                x_axis_id="secondary",
                orientation="top",
            ),
            rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
            rx.recharts.y_axis(
                data_key="pv",
                y_axis_id="right",
                orientation="right",
            ),
            rx.recharts.graphing_tooltip(),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=300,
        ),
        width="100%"
)