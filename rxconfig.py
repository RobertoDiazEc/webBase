import reflex as rx

config = rx.Config(
    app_name="redx_web",
    #api_url="https://api-redx-web.up.railway.app:8000",
    api_url="https://api-redxsoluciones.koyeb.app:8000",
    cors_allowed_origins = [
         "http://localhost:3000",
         "https://redeveloped-web.vercel.app",
         "https://redeveloped-web.vercel.app:3000"
         "https://redeveloped-web-roberto-diaz-chs-projects.vercel.app"
     ],
)