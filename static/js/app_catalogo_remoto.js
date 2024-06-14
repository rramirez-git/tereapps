let setSyncMsg = () => {
    $(`#main-toolbar a[href*='sinc']`).on('click', () => {
        App.openPanel(
            $(`#sync-msg-panel-content`).html(),
            "Sincronizando...");
    });
}

let openImgItemPanel = (item_pk, item_name) => {
    let img = $(`#images-loader-content #item-${item_pk}`);
    if(img.length > 0) {
        img = img[0];
        App.openPanel(img.outerHTML, item_name);
    }
}

let openAddItemToCatalogListPanel = item => {
    let template = Handlebars.compile( $( "#add-to-list-panel-content" ).html() );
    let html = template({item});
    App.openPanel(html, "Agregar elemento a lista");
}

let openDeleteItemFromCatalogListPanel = item => {
    let template = Handlebars.compile( $( "#remove-from-list-panel-content" ).html() );
    let html = template({item});
    App.openPanel(html, "Eliminar el elemento de la lista");
}
