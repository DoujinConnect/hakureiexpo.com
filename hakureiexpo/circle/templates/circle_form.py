{% extends "base.html" %}
{% block content %}
<div class="container">
  <h2>Submission</h2>
  <form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit" />
  </form>
</div>
{% endblock %}
