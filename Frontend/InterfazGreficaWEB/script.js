document.addEventListener('DOMContentLoaded', () => {
    const newsContainer = document.getElementById('news-container');
    const biasFilter = document.getElementById('bias-filter');

    // Simulación de la carga de noticias desde una API
    const newsArticles = [
        { title: 'Noticia 1', content: 'Contenido de la noticia 1', source: 'Fuente A', bias: 'left' },
        { title: 'Noticia 2', content: 'Contenido de la noticia 2', source: 'Fuente B', bias: 'center' },
        { title: 'Noticia 3', content: 'Contenido de la noticia 3', source: 'Fuente C', bias: 'right' },
        { title: 'Noticia 4', content: 'Contenido de la noticia 4', source: 'Fuente D', bias: 'left' },
        { title: 'Noticia 5', content: 'Contenido de la noticia 5', source: 'Fuente E', bias: 'center' }
    ];

    function displayNews(bias) {
        newsContainer.innerHTML = ''; // Limpiar el contenedor de noticias
        const filteredArticles = newsArticles.filter(article => bias === 'all' || article.bias === bias);

        filteredArticles.forEach(article => {
            const articleDiv = document.createElement('div');
            articleDiv.classList.add('news-item');
            articleDiv.innerHTML = `<h3>${article.title}</h3><p>${article.content}</p><p><strong>Fuente:</strong> ${article.source}</p>`;
            newsContainer.appendChild(articleDiv);
        });
    }

    // Cargar todas las noticias al inicio
    displayNews('all');

    // Manejar el cambio en el filtro
    biasFilter.addEventListener('change', (e) => {
        const selectedBias = e.target.value;
        displayNews(selectedBias);
    });

    // Manejo del formulario de contacto
    document.getElementById('contact-form').addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Mensaje enviado!');
        e.target.reset();
    });
});