$('#buzz .row').hide()

$('#buzz h2').click(function(event) {
  $('#buzz .row').fadeIn();
});

if($('buzz .row').is(":visible")) {
  $('buzz .row').fadeOut();
}});
