/*****
 app_valuacion de puestos functions
*/

$(document).ready(() => {
    if(typeof calculateVals != "undefined") {
        calculateVals();
    }
    if($("#data-graph").length > 0) {
        createGraph();
    }
})

let createGraph = () => {
    data = data.sort((row_1, row_2) => row_2.puntos - row_1.puntos);
    let context = document.getElementById('data-graph').getContext('2d');
    if("PuestoPtos" == grafico_typ) {
        let graph = new Chart(context, {
            "type": "horizontalBar",
            "data": {
                "options": {"scales": {"yAxes": [{"ticks": {"beginAtZero": true}}]}},
                "labels": data.map(row => row.puesto),
                "datasets": [{
                    "label": "Puntos",
                    "data": data.map(row => row.puntos)
                }]
            }
        });
    } else if("PuestoPesos" == grafico_typ) {
        let graph = new Chart(context, {
            "type": "horizontalBar",
            "data": {
                "options": {"scales": {"yAxes": [{"ticks": {"beginAtZero": true}}]}},
                "labels": data.map(row => row.puesto),
                "datasets": [{
                    "label": "Pesos",
                    "data": data.map(row => row.pesos)
                }]
            }
        });
    }
}
