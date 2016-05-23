$(document).ready(function(){
  $('#news-slider').slider({full_width: true, height: 345});
  $('.carousel').carousel({dist: -130});
  $('.modal-trigger').leanModal();

  $(".lecturer-preview").click(function() {
    var id = $(this).attr("lecturer-id");
    console.log(id);
    // var id = 2;
    $("#lecturer-modal .modal-content").load("/board/lecturer_modal/"+id);
    // $("#myModal").text(id);      
  });
});