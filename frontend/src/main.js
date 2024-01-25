function cargarImagenAleatoria ()
{
    const searchTerms ='tourist,landmark,travel,city,countries';
    const apiUrl = `https://source.unsplash.com/featured/?${searchTerms}`;

    const imagen = document.getElementById('imagenAleatoria')
    const gif = document.getElementById('gif')
    const timestamp = new Date().getTime();
    const imageUrl = `${apiUrl}?timestamp=${timestamp}`;
    imagen.style.display = 'none';
    gif.style.display = 'block';
    imagenInfo.style.display = 'none';

    axios.get(imageUrl)
    .then(Response =>
    {
        imagen.src = Response.request.responseURL;
        imagen.style.display = 'block';
        gif.style.display = 'none';
        mostrarInformacionImagen()
    })
    .catch(error =>
    {
        console.error('Error al obtener la imagen',error);
    });
}

function mostrarInformacionImagen() {

    const nombreImagen = "Nombre de la imagen";
    const descripcionImagen = "Descripción de la imagen";

    // Muestra la información de la imagen
    const nombreElemento = document.getElementById("nombreImagen");
    const descripcionElemento = document.getElementById("descripcionImagen");
    const imagenInfo = document.getElementById("imagenInfo");

    nombreElemento.innerText = nombreImagen;
    descripcionElemento.innerText = descripcionImagen;
    imagenInfo.style.display = "block";
}
