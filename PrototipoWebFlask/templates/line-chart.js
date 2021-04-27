new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
    datasets: [{
        data: [90, 87, 95, 84, 88, 78, 75],
        label: "RPM",
        borderColor: "#3e95cd",
        fill: false
      },
        {
        data: [96,96,95,92,94,94,95],
        label: "Saturacion oxigeno",
        borderColor: "#8e5ea2",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Ritmo Cardiaco-Saturacion'
    }
  }
});
