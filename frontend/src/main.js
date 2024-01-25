function cargarImagenAleatoria ()
{
    const searchTerms ='tourist,landmark,travel,city,countries';
    const apiUrl = `https://source.unsplash.com/featured/?${searchTerms}`;

    const imagen = document.getElementById('imagenAleatoria')
    const timestamp = new Date().getTime();
    const imageUrl = `${apiUrl}?timestamp=${timestamp}`;

    axios.get(imageUrl)
    .then(Response =>
    {
        imagen.src = Response.request.responseURL;
    })
    .catch(error =>
    {
        console.error('Error al obtener la imagen',error);
    });
}