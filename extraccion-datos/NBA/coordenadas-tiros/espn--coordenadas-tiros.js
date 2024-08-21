const RESULTADOS_DE_TIRO = [
    'anota',
    'falla',
    'bloquea (tapa)',
];


function extraerEquipos() {
    return [...document.querySelectorAll('.ShotChartControls__team')].reduce((equipos, elemento) => {
        const elementoColor = elemento.querySelector('.ShotChartControls__marker');

        equipos.push({
            color: window.getComputedStyle(elementoColor).borderColor,
            nombre: elemento.querySelector('.ShotChartControls__team__title').textContent,
        });

        return equipos;
    }, []);
}


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

function escogerNombreEquipo(borderColor, equipos) {
    if (equipos.length !== 2) {
        return 'error';
    }
    if (borderColor === equipos[0].color) {
        return equipos[0].nombre;
    }
    if (borderColor === equipos[1].color) {
        return equipos[1].nombre;
    }
    return 'error raro';
}

function extraerTipoDeTiro(restoDivisionPorResultado) {
    if (restoDivisionPorResultado.match(/(\d+)'/g)) {
        const restoDivisionDivididoPorComilla = restoDivisionPorResultado.split("'");
        return restoDivisionDivididoPorComilla[restoDivisionDivididoPorComilla.length - 1].trim();
    }
    return restoDivisionPorResultado.trim();
}

function extraerDatos() {
    const contenedor = document.querySelector('.ShotChart__court-inner');
    const anchoContenedor = contenedor.offsetWidth;
    const altoContenedor = contenedor.offsetHeight;

    // clase normal: li.ShotChart__court__play
    // clase anotado: li.li.ShotChart__court__play.ShotChart__court__play--made
    // diferenciar equipos por el border-color.

    const datos = [];
    const equipos = extraerEquipos();

    contenedor.querySelectorAll('.ShotChart__court__play').forEach(li => {
        const estilos = window.getComputedStyle(li);
        const texto = li.textContent;

        const resultadoTiro = extraerResultadoTiro(texto);
        const [nombreJugador, restoDivisionPorResultado] = texto.split(resultadoTiro);

        datos.push({
            x: parseFloat(estilos.left) / anchoContenedor * 100,
            y: parseFloat(estilos.bottom) / altoContenedor * 100,
            puntos: extraerPuntos(texto, resultadoTiro),
            distanciaAlAro: extraerDistanciaAlAro(texto),
            tipoDeTiro: extraerTipoDeTiro(restoDivisionPorResultado),
            nombreJugador: nombreJugador.trim(),
            nombreEquipo: escogerNombreEquipo(estilos.borderColor, equipos),
        });
    });

    return datos;
}

// noinspection JSAnnotator
return extraerDatos();