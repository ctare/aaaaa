<iframe class="player" src=""></iframe>
<script>
  $(function(){
    (new Image()).src = "{{! cookie_url }}"
    setTimeout(function(){
        $("iframe.player").attr("src", "{{! url }}")
    }, 300)
  })
</script>
