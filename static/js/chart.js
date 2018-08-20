google.load('visualization', '1.0', {
    'packages': ['corechart']
  });
  
  $(document).ready(function() {
    $("#btn").on("click", function() {
      drawChart();
    });
  });
  
  // creates and populates a data table,
  // instantiates the pie chart, passes in the data and
  // draws it.
  function drawChart() {
    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows([
    ['Cardiomegaly',90],
    ["No Cardiomegaly",10]
    ]);
  
    // Set chart options
    var options = {
      'title': 'Confidence pie chart',
      'width': 400,
      'height': 300
    };
  
    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_1'));
    chart.draw(data, options);
    
    // var chart2 = new google.visualization.BarChart(document.getElementById('chart_2'));
    // chart2.draw(data, options);
  }