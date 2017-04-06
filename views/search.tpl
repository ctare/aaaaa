% from bottle import template

<div id="search">
  % if pager["prev"]:
    <span class="pager prev" url="{{ pager["prev"] }}">前へ</span>
  % end
  % for number, url in sorted(pager["number"].items(), key=lambda x: int(x[0])):
    % if number == pager["now"]:
      <span class="pager now">{{ number }}</span>
    % else:
      <span url="{{ url }}" class="pager">{{ number }}</span>
    % end
  % end
  % if pager["next"]:
    <span class="pager next" url="{{ pager["next"] }}">次へ</span>
  % end
</div>

{{! template("mylist.tpl", {"mylist": videos}) }}

<style>
.pager{
  display: inline-block;
  background: lightgray;
  border-radius: 5px;
  padding: 5px;
}

.pager:hover{
  opacity: 0.5;
}

.pager.now{
  background: darkgray;
  color: lightgray;
}
</style>
