
var ctx1 = document.getElementById('myChart1').getContext('2d');
var data1 = {
    labels: [{% for i in operations %}  '{{ i.inventory}}',  {% endfor %}],
    datasets: [{
    data: [{% for i in operations %}  {{ i.nos2}},  {% endfor %}], // Your data values here
    backgroundColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(240, 120, 50, 1)',], // Custom colors
    }]
};


var myPieChart = new Chart(ctx1, {
type: 'pie',
data: data1,
options: {
    responsive: true, // Make the chart responsive
    legend: {
    position: 'bottom', // Position the legend
    },
},
});


var ctx = document.getElementById('myChart2').getContext('2d');
var myChart = new Chart(ctx, {
type: 'line',
data: {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [{
      label: 'Assets',
      data: ['212300','367000','485000','295000','330000','530000','460000'],
      
      backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',
      ],
      borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',

      ],
      borderWidth: 2
  },{
      label: 'Liabilites',
      data: ['100000','200000','300000','170000','30000','220000','700000'],
      
      backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',
      ],
      borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',

      ],
      borderWidth: 2
  },{
      label: 'Liquidity',
      data: ['127300','167000','185000','205000','220000','230000','240000'],
      
      backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',
      ],
      borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(240, 120, 50, 1)',

      ],
      borderWidth: 2
  }]
},
options: {
  scales: {
      y: {
          beginAtZero: true
      }
    
  }
}
});

var myLineChart = new Chart(ctx2, {
type: 'line',
data: data2,
options: {
responsive: true, // Make the chart responsive
legend: {
position: 'bottom', // Position the legend
},
},
});

