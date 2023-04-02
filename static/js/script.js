// funcion para el formulario
const myform = document.getElementById("Formulario");
myform.addEventListener("submit", (e) =>{

  //evita la recarga
  e.preventDefault();
  console.log("se mando el formulario")
  alert("Formulario enviado");
})

function alphaOnly(event) {
  var key = event.keyCode;`enter code here`
  return ((key >= 65 && key <= 90) || key == 8);
};

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
};
$("#id_formulario").validate({
  rules: {
    "txtEmail": {
      required: true,
      email: true
    },
    "txtRut": {
      required: true
    },
    "txtNombre": {
      required: true
    },
    "txtMovil": {
      required: true,
      tel: true,
      minlength: 9
    }
  },

  messages: {
    "txtEmail": {
      required: 'Ingrese email',
      email: 'No cumple formato'
    },
    "txtRut": {
      required: 'Ingrese rut'
    },
    "txtNombre": {
      required: 'Ingrese nombre'
    },
    "txtMovil": {
      required: 'Ingrese telefono movil',
      tel: 'No cumple formato',
      minlength:'Teléfono no válido'
    }
  }
});