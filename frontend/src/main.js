function loadRandomImage()
{
    const searchTerms ='tourist,landmark,travel,city,countries';
    const apiUrl = `https://source.unsplash.com/featured/?${searchTerms}`;

    const image = document.getElementById('randomImage')
    const gif = document.getElementById('gif')
    const timestamp = new Date().getTime();
    const imageUrl = `${apiUrl}?timestamp=${timestamp}`;
    image.style.display = 'none';
    gif.style.display = 'block';
    infoImage.style.display = 'none';

    axios.get(imageUrl)
    .then(Response =>
    {
        image.src = Response.request.responseURL;
        image.style.display = 'block';
        gif.style.display = 'none';
        showInfoImage()
    })
    .catch(error =>
    {
        console.error('Error al obtener la imagen',error);
    });
}

function showInfoImage() {

    const nameImage = "Nombre de la imagen";
    const descriptionImage = "Descripción de la imagen";

    // Muestra la información de la imagen
    const nameElement = document.getElementById("nameImage");
    const descriptionElement = document.getElementById("descriptionImage");
    const infoImage = document.getElementById("infoImage");

    nameElement.innerText = nameImage;
    descriptionElement.innerText = descriptionImage;
    infoImage.style.display = "block";
}
