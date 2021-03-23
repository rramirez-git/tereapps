/*
JS file for zend_django app
*/

Date.prototype.asMySQL = function() {
    let res = "" + this.getFullYear() + "-"
        + ( this.getMonth() < 9 ? "0" : "" ) + ( this.getMonth() + 1 ) + "-"
        + ( this.getDate() < 10 ? "0" : "" ) + this.getDate();
    return res;
}
Date.prototype.asMx = function() {
    let res = ( this.getDate() < 10 ? "0" : "" ) + this.getDate() + "/"
        + ( this.getMonth() < 9 ? "0" : "" ) + ( this.getMonth() + 1 )
        + "/" + this.getFullYear();
    return res;
}
Date.prototype.theTime = function() {
    let res = "";
    if ( this.getHours() < 10 ) { res += "0"; }
    res += this.getHours() + ":";
    if ( this.getMinutes() < 10 ) { res += "0"; }
    res += this.getMinutes();
    return res;
}
Date.prototype.fromMX = function( date ) {
    return new Date(
        parseInt( date.substr( 6, 4 ) ),
        parseInt( date.substr( 3, 4 ) ) - 1,
        parseInt( date.substr( 0, 2 ) ) );
}
Date.prototype.addDays = function( days ) {
    let date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}
Number.prototype.asMoney = function() {
    let asString = `${this}`;
    if( asString.indexOf( "." ) == -1 ){ asString += "."; }
    asString += "00";
    return asString.substr( 0, asString.indexOf( "." ) + 3 );
}

class clsApp {
    checkInputIn( idcontainer ) {
        $( '#' + idcontainer + ' input[type="checkbox"]' ).attr(
            'checked', true );
    }
    uncheckInputIn( idcontainer ) {
        $( '#' + idcontainer + ' input[type="checkbox"]' ).attr(
            'checked', false );
    }
    openPanel( body, title, close = true, footer = null, idmodal="modal-panel-message" ) {
        let template = Handlebars.compile( $( "#modal-panel-message-template" ).html() );
        let html = template( { title, body, footer, close, idmodal } );
        $( `#${idmodal}` ).remove();
        $( document.body ).append( $( html ) );
        $( `#${idmodal}` ).modal();
    }
    closePanel(idmodal="modal-panel-message") {
        $(`#${idmodal}`).remove();
        $('.modal-backdrop').remove();
        $(document.body).removeClass("modal-open");
        $(document.body).css("padding-right", "0px")
    }
    setUIControls() {
        if( req_ui ) {
            $.datepicker.setDefaults( $.datepicker.regional[ "es" ] );
            $( `input[type="date"]` ).datepicker( {
                changeMonth: true,
                changeYear: true,
                dateFormat : 'yy-mm-dd'
            } );
        }
    }
    setReadOnlyForm(container_selector = "#main-form") {
        let frm = $(container_selector);
        frm.find("input").attr("disabled", true);
        frm.find("textarea").attr("disabled", true);
        frm.find("button").attr("disabled", true);
        frm.find("select").attr("disabled", true);
        frm.find("input").attr("readonly", true);
        frm.find("textarea").attr("readonly", true);
        frm.find("button").attr("readonly", true);
        frm.find("select").attr("readonly", true);
        frm.find('input[type="file"]').parent().parent().remove();
        frm.find('input[type="number"]').each( function() {
            let valor = this.value;
            if( valor.indexOf( '.' ) >-1 ) {
                this.value = valor.substr( 0, valor.indexOf( '.' ) + 3 );
            }
        } );
        frm.find("#btn-save").remove();
    }
    showPrivacyPolicy(){
        App.openPanel( $( "#privacy-policy-template" ).html(), "Política de Privacidad" );
    }
    showDeletingConfirmation(url, elemento="elemento", pre_elemento="el") {
        let template = Handlebars.compile( $( "#deleting-confirmation-template" ).html() );
        let html = template( { url, elemento, pre_elemento } );
        App.openPanel( html, "Confirmación de Eliminación");
        return false;
    }
    isEmpty(valor) {
        return "" == valor || 0.0 == parseFloat( valor );
    }
    validate_required_fields( container ) {
        let elements = $(`${container} [required="required"]`);
        for( let idx = 0; idx <= elements.length; idx++){
            let element = $(elements[idx]);
            if(element.val() == "") {
                let lbl = element.parent().find('label');
                let msg = "El elemento ";
                if(lbl.length > 0) {
                    msg += lbl.text() + " ";
                }
                msg += "no puede estar vacío";
                alert(msg);
                element.focus();
                return false;
            }
        }
        return true;
    }
}

let App = new clsApp();

$( document ).ready( () => {
    $('[data-toggle="tooltip"]').tooltip();
    App.setUIControls();

    //$(document.body).css('padding-left', $("#container-main-menu").width()+"px");
} );

$(document).ready(function($) {
    var bsDefaults = {
         offset: true,
         overlay: false,
         width: '300px'
      },
    bsMain = $('.bs-offset-main'),
    bsOverlay = $('.bs-canvas-overlay');

    $('[data-toggle="canvas"][aria-expanded="false"]').on('click', function() {
        var canvas = $(this).data('target'),
        opts = $.extend({}, bsDefaults, $(canvas).data()),
        prop = $(canvas).hasClass('bs-canvas-right') ? 'margin-right' : 'margin-left';

      if (opts.width === '100%')
         opts.offset = false;

      $(canvas).css('width', opts.width);
      if (opts.offset && bsMain.length)
         bsMain.css(prop, opts.width);

      $(canvas + ' .bs-canvas-close').attr('aria-expanded', "true");
      $('[data-toggle="canvas"][data-target="' + canvas + '"]').attr('aria-expanded', "true");
      if (opts.overlay && bsOverlay.length)
         bsOverlay.addClass('show');

      $("#main-navbar-title").css(prop, opts.width);

      return false;
   });

   $('.bs-canvas-close, .bs-canvas-overlay').on('click', function() {
      var canvas, aria;
      if ($(this).hasClass('bs-canvas-close')) {
         canvas = $(this).closest('.bs-canvas');
         aria = $(this).add($('[data-toggle="canvas"][data-target="#' + canvas.attr('id') + '"]'));
         if (bsMain.length)
            bsMain.css(($(canvas).hasClass('bs-canvas-right') ? 'margin-right' : 'margin-left'), '');
      } else {
         canvas = $('.bs-canvas');
         aria = $('.bs-canvas-close, [data-toggle="canvas"]');
         if (bsMain.length)
            bsMain.css({
               'margin-left': '',
               'margin-right': ''
            });
      }
      canvas.css('width', '');
      aria.attr('aria-expanded', "false");
      if (bsOverlay.length)
         bsOverlay.removeClass('show');

      $("#main-navbar-title").css('margin-left', '1rem');

      return false;
   });

   if("True" === leftMenu_display) {
       $('[data-toggle="canvas"][aria-expanded="false"]').trigger( "click" );
   }
});

let setLeftMenuOpc = (valor) => {
    $.post(
        leftMenu_url,
        {
            seccion: 'general',
            parametro: 'open_left_menu',
            user: leftMenu_user,
            value: valor,
            csrfmiddlewaretoken: $(`#csrf_token input[type="hidden"]`).val()
        }
    ).fail((data) => {
        console.log("Error estableciendo parametro");
        console.log(`State: ${data.readyState}`);
        console.log(data.responseText);
        });
}

$(document).ready( () => {
    if($("#data-grid-report").length) {
        $.getScript('/static/js/data-grid-results.js');
    }

    $("#main-toolbar form.form-inline").contents().appendTo($("#top-main-menu #finder"));
    $("#main-toolbar form.form-inline").remove();

    $("#main-title-page").contents().appendTo($("#main-navbar-title"));
    $("#main-title-page").remove();
} );
