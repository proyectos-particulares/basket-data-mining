import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def ejecutar_script_en_url(
        url_pagina,
        script_js,
        tiempo_espera_carga=1,
        tiempo_espera_script=0
):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    # Ejecutar sin ventanas emergentes del navegador.
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=service, options=options)
    try:
        # Abrir la página web.
        driver.get(url_pagina)

        print(f"- Cargando {url_pagina}...")
        time.sleep(tiempo_espera_carga)

        # Ejecutar el script JS.
        result = driver.execute_script(script_js)

        print(f"- Ejecutando script JS...")
        time.sleep(tiempo_espera_script)

        return result
    finally:
        driver.quit()
