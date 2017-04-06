% rebase("base.tpl", title='')
% from bottle import template
<form id="search-form">
  <input id="search" type="text" placeholder="検索" v-model="highlight">
</form>

<div id="description"></div>
<div id="mylist"></div>

<div class="fix-window">
  <div id="up-button" class="move-button">top</div>
  <div id="player" class="player"></div>
  <div id="down-button" class="move-button" style="display: none">down</div>
</div>

<script>
function get(a_tag, attr) {
  return a_tag.attributes[attr].value
}

function video_tag_highlight(re) {
  $.each($(".video-tag"), function(i, t){
    t.innerHTML = (t.attributes["title_data"].value.replace(new RegExp("(" +re+ ")", "i"), "<span class='highlight'>$1</span>"))
  })
}

$(function() {
  let v_query = new Vue({
    el: '#search-form',
    data: {
      highlight: ""
    },
    watch: {
      highlight: function(data){
        video_tag_highlight(data)
      }
    }
  });
  
  $('.fix-window').on('click', '#up-button', function(e){
    parent = e.target.parentElement
    parent.style.bottom = "auto"
    parent.style.top = "0"
    p = parent
    $(parent.querySelectorAll(".move-button")).css("display", "")
    e.target.style.display = "none"
  }).on('click', '#down-button', function(e){
    parent = e.target.parentElement
    parent.style.top = "auto"
    parent.style.bottom = "0"
    $(parent.querySelectorAll(".move-button")).css("display", "")
    e.target.style.display = "none"
  })

  $("#search-form").on("submit", function(e){
    $.post("/search", {q: $("#search").val()}, function(data){
      $("#mylist").html(data)
      video_tag_highlight($("#search").val())
    })
    e.preventDefault()
  })

  $("#mylist").on("click", ".pager[url]", function(e){
    $.post("/search", {q: $("#search").val(), url: e.target.attributes["url"].value}, function(data){
        $("#mylist").html(data)
    })
  })

  $(document).on('click', 'a[mylist]', function(e){
    $.get("/mylist", {mylist: get(e.target, 'mylist')}, function(data){
      $("#mylist").html(data)
    })
  })

  $(document).on('click', 'a[video]', function(e){
    vid = get(e.target, "video")
    $.get("/video", {video_id: vid}, function(data){
        $("#player").html(data)
    })
    $.get("/description", {video_id: vid}, function(data){
        $("#description").html(data)
    })
  })
})
</script>

<style>
.fix-window {
  position: fixed;
  right: 0;
  bottom: 0;
  background: black;
}

.player {
  width: 300px;
  height: 180px;
}

.move-button {
  background: lightgray;
  text-align: center;
  width: 100%;
  padding: 5px;
}

.video-tag {
  display: inline-block;
  margin: 2px;
  padding: 2px;
  background: gray;
  color: white;
  border-radius: 5px;
}

.highlight {
  background: black;
  border-radius: 5px;
}
</style>
