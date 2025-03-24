google.charts.load('current', {'packages':['corechart']});

    function drawChart(probability,pid) {
            var data = google.visualization.arrayToDataTable([
              ['iris species', 'prob'],
              ['setosa',     prob[0][0]],
              ['versicolor',  prob[0][1]],
              ['virginica', prob[0][2]]
             ]);


             var options = {
               title: '붓꽃 품종 확률',
               is3D: true,
             };

             var chart = new google.visualization.PieChart(pid);
             chart.draw(data, options);
           }

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
           txtOut.value = response.prediction + "일 확률:" + response.probability
           console.log(response)
           google.charts.setOnLoadCallback(drawChart(response.probability, document.getElementById("pieChart")));

        }).fail(function(response) {
          alert("fail: " + response)

        }
        ).always()
    }
