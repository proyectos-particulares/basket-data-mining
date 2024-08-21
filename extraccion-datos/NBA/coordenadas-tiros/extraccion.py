import pandas as pd

from utils.python.ejecutar_script_js_en_url import ejecutar_script_en_url

RUTA_SCRIPT = './espn--coordenadas-tiros.js'
LINKS_PAGINAS = [
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584690/suns-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584715/warriors-kings',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584724/warriors-rockets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584736/warriors-pelicans',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584754/kings-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584093/warriors-thunder',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584770/warriors-cavaliers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584773/warriors-pistons',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584797/warriors-nuggets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584804/cavaliers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584814/timberwolves-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584113/timberwolves-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584829/thunder-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584835/thunder-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584852/rockets-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584864/warriors-suns',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584139/spurs-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584148/warriors-kings',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584901/clippers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584908/warriors-clippers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401616468/trail-blazers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401616476/warriors-thunder',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584936/warriors-suns',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584953/warriors-clippers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584967/nets-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584976/warriors-trail-blazers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401584990/celtics-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585014/wizards-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585027/trail-blazers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585030/warriors-nuggets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585054/heat-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585072/mavericks-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585091/magic-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585106/nuggets-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585118/pistons-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585132/raptors-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585153/pelicans-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585164/warriors-bulls',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585173/warriors-bucks',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585188/warriors-grizzlies',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585254/hawks-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585260/kings-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585278/lakers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585301/76ers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585321/warriors-grizzlies',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585327/warriors-hawks',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585345/warriors-nets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585355/warriors-76ers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585361/warriors-pacers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585385/suns-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585397/warriors-jazz',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585417/clippers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401636113/warriors-jazz',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585430/lakers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585439/hornets-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585452/nuggets-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585462/warriors-wizards',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585480/warriors-knicks',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585488/warriors-raptors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585500/warriors-celtics',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585527/bucks-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585535/bulls-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585549/spurs-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585564/warriors-spurs',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585580/warriors-mavericks',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585601/warriors-lakers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585616/knicks-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585629/grizzlies-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585644/pacers-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585659/warriors-timberwolves',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585672/warriors-heat',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585677/warriors-magic',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585690/warriors-hornets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585713/warriors-spurs',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401636114/mavericks-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585741/warriors-rockets',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585725/warriors-mavericks',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585770/jazz-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585783/warriors-lakers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585797/warriors-trail-blazers',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585810/pelicans-warriors',
    'https://espndeportes.espn.com/basquetbol/nba/juego/_/juegoId/401585826/jazz-warriors',
]


def main():
    # Lista para almacenar todos los resultados.
    resultados = []
    script = open(RUTA_SCRIPT, 'r').read()

    # Recorrer cada URL y ejecutar el script JS.
    for url in LINKS_PAGINAS:
        resultado = ejecutar_script_en_url(url, script, 0)
        resultados.append({'url': url, 'datos': resultado})

    print()

    # Crear un archivo Excel con múltiples hojas.
    with pd.ExcelWriter('./documentos-generados/partidos-warriors--23-24.xlsx', engine='xlsxwriter') as xls_writer:
        for resultado in resultados:
            url_pagina = resultado['url']
            datos = resultado['datos']

            if len(datos) == 0:
                print(f"No se encontraron datos para {url_pagina}")
                continue

            # Convertir datos a DataFrame
            data_frame = pd.DataFrame(datos)

            # Nombre de la hoja en el archivo Excel
            nombre_partido = url_pagina.split('/')[-1]

            # Guardar DataFrame en una hoja del archivo Excel
            data_frame.to_excel(xls_writer, sheet_name=nombre_partido, index=False)
            hoja = xls_writer.sheets[nombre_partido]

            # Ajustar el ancho de las columnas automáticamente
            for i, col in enumerate(data_frame.columns):
                max_length = max(data_frame[col].astype(str).map(len).max(), len(col)) + 2
                hoja.set_column(i, i, max_length)

            print(f"Resultados para {url_pagina} guardados en la hoja: {nombre_partido}")

        print("\n¡Archivo Excel creado con éxito!")


if __name__ == '__main__':
    main()
