document.querySelector("#btngatos").addEventListener('click', function () {
    obtener_datos();

});




function obtener_datos() {

    let url = 'https://cat-fact.herokuapp.com/facts/random';

    const api = new XMLHttpRequest();
    api.open('GET', url, true);
    api.send();


    api.onreadystatechange = function () {

        if (this.status == 200 && this.readyState == 4) {
            let datos = JSON.parse(this.responseText);

            
                    //console.log(datos.text);


            var texto = datos.text;
            


            $('#facts').html(texto);
            


           

        }
    }

}
