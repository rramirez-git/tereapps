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

let AppValuacionPuestosAdjuster = {
    init() {
        if(location.href.match(/\/puesto\/\d+\//ig)) {
            this.generic_read_screen('div_id_puesto');
        } else if(location.href.match(/\/factor\/\d+\//ig)) {
            this.generic_read_screen('div_id_factor', 'Factor');
        } else if(location.href.match(/\/tabulador\/\d+\//ig)) {
            this.generic_read_screen('div_id_tabulador', 'Tabulador');
        }
    },
    show_main_toolbar() {
        $("#main-toolbar, #opc-hide-main-toolbar").removeClass('d-none');
        $("#opc-show-main-toolbar").addClass('d-none');
    },
    hide_main_toolbar() {
        $("#main-toolbar, #opc-hide-main-toolbar").addClass('d-none');
        $("#opc-show-main-toolbar").removeClass('d-none');
    },
    generic_read_screen(id_element_4_np, elemento=null) {
        this.hide_main_toolbar();
        $(`#main-toolbar a[title="Listar Todos"]`).remove();
        let next_prev_div = $(`<div class="col-sm-2 text-left"></div>`);
        $(`#${id_element_4_np}`).append(next_prev_div);
        next_prev_div.append($(`a[title="Anterior"]`));
        next_prev_div.append($(`a[title="Siguiente"]`));
        for(let opc of [
            {id: 'opc-show-main-toolbar', fn: 'show_main_toolbar', label: 'Editar' + (elemento ? ' ' + elemento : ''), extraClass: ''},
            {id: 'opc-hide-main-toolbar', fn: 'hide_main_toolbar', label: 'Cerrar Edicion' + (elemento ? ' de ' + elemento : ''), extraClass: 'd-none'}
        ]) {
            $("#cntr-extra-actions").append(
                `<a id="${opc.id}" class="dropdown-item ${opc.extraClass}" href="#" onclick="AppValuacionPuestosAdjuster.${opc.fn}()">${opc.label}</a>`);
        }
    }
}

$(document).ready(() => {
    AppValuacionPuestosAdjuster.init();
})
