function Send() {

    s1 = document.getElementById("sl")
    sw = document.getElementById("sw")
    pl = document.getElementById("pl")
    pw = document.getElementById("pw")

    var data = {
        "sepal_length":s1,
        "sepal_width": sw,
        "petal_length": pl,
        "petal_width": pw
    }


  $.ajax({
    type: "POST",
    url: 'http://localhost:8000/predict',
    headers:{
        "Accept" : "application/json",
        "Content-Type": "application/json",
        },
    data: JSON.stringify(data),

  }).done(function(response) {
      txtOut.value = response.prediction
      console.log(response)

  }).fail(function(response) {
      alert("fail: " + response)

  }
  ).always()
}
