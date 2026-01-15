import reflex as rx

config = rx.Config(
    app_name="redx_web",
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
    #api_url="https://api-redx-web.up.railway.app:8000",
    api_url="https://api-redxsoluciones.koyeb.app:8000",
    cors_allowed_origins = [
         "http://localhost:3000",
         "https://redxsoluciones.vercel.app",
         "https://redxsoluciones.vercel.app:3000",
         "https://redxsoluciones-roberto-diaz-chs-projects.vercel.app"
     ],
    disable_plugins= ['reflex.plugins.sitemap.SitemapPlugin'] 
)