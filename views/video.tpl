<script src="{{! cookie_url }}"></script>
<iframe class="player" src="" frameborder="0"></iframe>
<script>
  setTimeout(() => {
    $("iframe").attr("src", "{{! url }}")
  }, 300)
</script>
