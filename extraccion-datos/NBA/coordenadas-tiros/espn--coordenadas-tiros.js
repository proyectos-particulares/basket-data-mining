const RESULTADOS_DE_TIRO = [
    'anota',
    'falla',
    'bloquea (tapa)',
];

function extraerResultadoTiro(texto) {
    // Devuelve el resultado del tiro: anota, falla o bloquea (tapa).
    for (const tipo of RESULTADOS_DE_TIRO) {
        if (texto.includes(tipo)) {
            return tipo;
        }
    }
    return null;
}

function extraerPuntos(texto, resultadoTiro) {
    // Si el resultado de tiro no es "anota", entonces ha fallado.
    // Si el texto contiene '3pts', entonces es un triple.
    // Si no ha fallado y no es un triple, entonces es un tiro en pintura.
    if (resultadoTiro !== RESULTADOS_DE_TIRO[0]) {
        return 0;
    }
    if (texto.includes('3pts')) {
        return 3;
    }
    return 2;
}

function extraerDistanciaAlAro(texto) {
    // Si el texto contiene el patrón formado por un número y una comilla simple,
    // entonces el número es la distancia al aro.
    const coincidencias = texto.match(/(\d+)'/g);
    return coincidencias ?
        parseInt(coincidencias[0]) :
        0;
}

function extraerDatos() {
    const contenedor = document.querySelector('.ShotChart__court-inner');
    const anchoContenedor = contenedor.offsetWidth;
    const altoContenedor = contenedor.offsetHeight;

    // clase normal: li.ShotChart__court__play
    // clase anotado: li.li.ShotChart__court__play.ShotChart__court__play--made
    // diferenciar equipos por el border-color.

    const datos = [];

    contenedor.querySelectorAll('.ShotChart__court__play').forEach(li => {
        const estilos = window.getComputedStyle(li);
        const texto = li.textContent;

        const resultadoTiro = extraerResultadoTiro(texto);
        const [nombreJugador, restoDivisionPorResultado] = texto.split(resultadoTiro);

        datos.push({
            x: parseFloat(estilos.left) / anchoContenedor * 100,
            y: parseFloat(estilos.top) / altoContenedor * 100,
            puntos: extraerPuntos(texto, resultadoTiro),
            distanciaAlAro: extraerDistanciaAlAro(texto),
            tipoDeTiro: restoDivisionPorResultado,
            nombreJugador: nombreJugador.trim(),
            nombreEquipo: estilos.borderColor,
        });
    });

    // console.log(datos);
    return datos;
}

// noinspection JSAnnotator
return extraerDatos();