$(document).ready(function() {
  var url = '/api/';
  var table = $('#tabletools').dataTable({
    ajax: {
      url: '/modulos/hora/getdata_json',
      dataSrc: ''
    },
    columns: [
      { data: 'Hora' },
      { data: 'Modificar' },
      { data: 'Eliminar' },
    ],
    "language": {
      "lengthMenu": "_MENU_",
      "sProcessing":     "Procesando...",
      "sZeroRecords":    "No se encontraron resultados",
      "sEmptyTable":     "Ningún dato disponible en esta tabla",
      "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
      "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
      "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
      "sInfoPostFix":    "",
      "sUrl":            "",
      "sInfoThousands":  ",",
      "sLoadingRecords": "Cargando...",
      "oPaginate": {
        "sFirst":    "Primero",
        "sLast":     "Último",
        "sNext":     "Siguiente",
        "sPrevious": "Anterior"
      },
      "oAria": {
        "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
      }
    }
  });
  $('.dataTables_filter input').attr('placeholder','Buscar');
  $('#example_length').hide();

  //DOM Manipulation to move datatable elements integrate to panel
  $('.panel-ctrls').append($('.dataTables_filter').addClass("pull-right")).find("label").addClass("panel-ctrls-center");
  $('.panel-ctrls').append("<i class='separator'></i>");
  $('.panel-ctrls').append($('.dataTables_length').addClass("pull-left")).find("label").addClass("panel-ctrls-center");
  $('.dataTables_paginate>ul.pagination').addClass("pull-right m0");
});
