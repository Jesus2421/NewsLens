document.addEventListener('DOMContentLoaded', () => {
    const newsContainer = document.getElementById('news-container');
    const biasFilter = document.getElementById('bias-filter');

    // 1. CONEXIÓN REAL AL BACKEND (Puerto 5000)
    console.log("Iniciando conexión con Hamilton Backend...");
    const socket = io('http://localhost:5000');

    let newsArticles = []; // Empezamos vacíos

    // 2. EVENTOS DE CONEXIÓN
    socket.on('connect', () => {
        console.log('✅ Conectado al servidor de noticias!');
        newsContainer.innerHTML = '<p style="color: green; font-weight: bold;">✅ Conectado. Esperando noticias...</p>';
    });

    socket.on('connect_error', (error) => {
        console.error('❌ Error de conexión:', error);
        newsContainer.innerHTML = '<p style="color: red;">Error: No se puede conectar con el servidor.</p>';
    });

    // 3. ESCUCHAR NOTICIAS REALES
    socket.on('nuevas_noticias', (data) => {
        console.log('📰 Noticias recibidas del servidor:', data);
        
        if (data.noticias && Array.isArray(data.noticias)) {
            // Actualizamos la lista local
            newsArticles = data.noticias;
            
            // Renderizamos inmediatamente
            console.log(`Procesando ${newsArticles.length} noticias para mostrar...`);
            displayNews(biasFilter.value);
        } else {
            console.warn('⚠️ Formato de noticias inesperado:', data);
        }
    });

    // 4. FUNCIÓN PARA MOSTRAR NOTICIAS (Renderizado)
    function displayNews(bias) {
        // Limpiar contenedor pero mantener un log visual si está vacío
        newsContainer.innerHTML = ''; 
        
        console.log(`Filtrando por: ${bias}`);
        
        // Filtrado robusto (ignorando mayúsculas/minúsculas)
        const filteredArticles = newsArticles.filter(article => {
            if (bias === 'all') return true;
            
            // Normalizar valores para comparar (ej: "Center" vs "center")
            const articleBias = (article.clasificacion || '').toLowerCase();
            const filterBias = bias.toLowerCase();
            
            return articleBias === filterBias;
        });

        console.log(`Noticias tras filtro: ${filteredArticles.length}`);

        if (filteredArticles.length === 0) {
            newsContainer.innerHTML = `
                <div style="text-align: center; padding: 20px; border: 1px dashed #ccc; width: 100%;">
                    <p>No hay noticias para el filtro: <strong>${bias}</strong></p>
                    <p><small>Total noticias recibidas: ${newsArticles.length}</small></p>
                </div>
            `;
            return;
        }

        filteredArticles.forEach(article => {
            const articleDiv = document.createElement('div');
            articleDiv.classList.add('news-item');
            
            // Estilos inline para asegurar visibilidad (por si el CSS falla)
            articleDiv.style.border = "1px solid #ddd";
            articleDiv.style.padding = "15px";
            articleDiv.style.margin = "10px";
            articleDiv.style.backgroundColor = "#fff";
            articleDiv.style.borderRadius = "8px";
            articleDiv.style.boxShadow = "0 2px 4px rgba(0,0,0,0.1)";
            
            // Añadir clase de sesgo para estilos
            if (article.clasificacion) {
                articleDiv.classList.add(`bias-${article.clasificacion.toLowerCase()}`);
            }
            
            let linkHtml = article.link ? `<a href="${article.link}" target="_blank" style="color: #007bff; text-decoration: none; font-weight: bold;">Leer más →</a>` : '';
            
            articleDiv.innerHTML = `
                <h3 style="margin-top: 0; color: #333;">${article.titulo}</h3>
                <p style="color: #666; font-size: 0.9em;">
                    <strong>Medio:</strong> ${article.medio} 
                    <span class="bias-tag" style="background: #eee; padding: 2px 6px; border-radius: 4px;">${article.clasificacion || 'Sin clasificar'}</span>
                </p>
                <p style="color: #999; font-size: 0.8em;">${article.fecha}</p>
                ${linkHtml}
            `;
            newsContainer.appendChild(articleDiv);
        });
    }

    // 5. FILTROS
    biasFilter.addEventListener('change', (e) => {
        displayNews(e.target.value);
    });
});
