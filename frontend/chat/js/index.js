function show_iframe(){
  let iframe = document.getElementById("iframe");
  let close_btn = document.getElementById("close_btn");
  iframe.style.display="block";
  close_btn.style.display="block"
}

function close_iframe(){
  let iframe = document.getElementById("iframe");
  let close_btn = document.getElementById("close_btn");
  iframe.style.display="none";
  close_btn.style.display="none"
}

$(document).ready(function(){
  $(".gnb>li").click(function(){
    var idx = $(this).index();
    $("section").not($("section").eq(idx)).hide();
    $("section").eq(idx).show();
  });
});