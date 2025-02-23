document.addEventListener("DOMContentLoaded", function () {
  var toastElList = document.querySelectorAll('.toast');
  toastElList.forEach(function (toastEl) {
    var toast = new bootstrap.Toast(toastEl);
    toast.show();
  });
});

$(document).ready(function() {
  var navbar = $(".navbar");


  $(window).scroll(function() {
      if ($(this).scrollTop() > 0) {
          navbar.addClass("scrolled");
      } else {
          navbar.removeClass("scrolled");
      }
  });
});