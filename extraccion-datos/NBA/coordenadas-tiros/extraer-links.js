/*
Extraer los links de los partidos desde la página de calendario de un equipo.
Ejemplo: https://espndeportes.espn.com/basquetbol/nba/equipo/calendario/_/nombre/gs/temporada/2024
 */

function extraerLinks() {
    let texto = "";

    document.querySelectorAll('.ml4 a').forEach(a => {
        texto += `'${a.href}',\n`;
    });
    console.log(texto);
}

extraerLinks();