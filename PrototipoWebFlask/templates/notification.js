function notifyMe() {
  // Comprobamos si el navegador soporta las notificaciones
  if (!("Notification" in window)) {
    alert("Este navegador no soporta las notificaciones del sistema");
  }

  // // Comprobamos si ya nos habían dado permiso
  // else if (Notification.permission === "granted") {
  //   // Si esta correcto lanzamos la notificación
  //   var notification = new Notification("Notificaciones activadas");
  // }

  // Si no, tendremos que pedir permiso al usuario
  // else if (Notification.permission !== 'denied') {
  //   Notification.requestPermission(function (permission) {
  //     // Si el usuario acepta, lanzamos la notificación
  //     if (permission === "granted") {
  //       var notification = new Notification("Notificaciones activadas!");
  //     }
  //   });
  // }

  // Finalmente, si el usuario te ha denegado el permiso y
  // quieres ser respetuoso no hay necesidad molestar más.
}

function spawnNotification(theBody) {

  var n = new Notification(theBody);
  // n.onclick = function(event) {
  // event.preventDefault(); // Previene al buscador de mover el foco a la pestaña del Notification
  // window.open('http://www.mozilla.org', '_blank');
  // }
  setTimeout(n.close.bind(n), 5000);
}

// setInterval(function(){$.ajax({
//   url: '/update_data',
//   type: 'POST',
//   success: function(response) {
//     console.log(response);
//     $("#content").html(response["fecha"]);
//   },
//   error: function(error) {
//     console.log(error);
//   }
// })}, 2000);
//


setInterval(function(){$.ajax({
  url: '/update_data',
  type: 'POST',
  success: function(response) {
    console.log(response);
    $("#content").html(response["pulso"]);
  },
  error: function(error) {
    console.log(error);
  }
})}, 2000);

