import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {
  const [noticias, setNoticias] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/noticias')
      .then(res => {
        if (!res.ok) throw new Error('Error al obtener noticias');
        return res.json();
      })
      .then(data => {
        setNoticias(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Noticias Clasificadas</h1>
        {loading && <p>Cargando noticias...</p>}
        {error && <p style={{color: 'red'}}>Error: {error}</p>}
        <ul style={{textAlign: 'left', maxWidth: 600, margin: '0 auto'}}>
          {noticias.map((noticia, idx) => (
            <li key={idx} style={{marginBottom: 20, borderBottom: '1px solid #ccc', paddingBottom: 10}}>
              <strong>{noticia.titulo}</strong> <br/>
              <span>Medio: {noticia.medio}</span> <br/>
              <span>Fecha: {noticia.fecha}</span> <br/>
              <span>Sesgo: <b>{noticia.sesgo}</b></span> <br/>
              <a href={noticia.link} target="_blank" rel="noopener noreferrer">Ver noticia</a>
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
