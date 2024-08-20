from utils.python.ejecutar_script_js_en_url import ejecutar_script_en_url

RUTA_SCRIPT = './espn--coordenadas-tiros.js'
LINKS_PAGINAS = [
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401656363/mavericks-celtics',
]


def main():
    # Lista para almacenar todos los resultados
    resultados = []
    script = open(RUTA_SCRIPT, 'r').read()

    # Recorrer cada URL y ejecutar el script JS
    for url in LINKS_PAGINAS:
        resultado = ejecutar_script_en_url(url, script)
        resultados.append({'url': url, 'datos': resultado})

    # Mostrar todos los resultados juntos
    for resultado in resultados:
        utl_pagina = resultado['url']
        datos = resultado['datos']

        print(f"\nResultados para {utl_pagina}:")
        print(datos)


if __name__ == '__main__':
    main()
