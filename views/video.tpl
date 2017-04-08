% rebase("base.tpl", title='')
<iframe class="player" src=""></iframe>
<script>
  $(function(){
    $.get("http://localhost:3030/?video_id={{ video_id }}", function(data){
      urls = data.split("\n")
      ;(new Image()).src = urls[0]
      setTimeout(function(){
          $("iframe.player").attr("src", urls[1])
      }, 300)
    })
  })
</script>
