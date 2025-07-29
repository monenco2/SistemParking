import React from 'react'
import { useState } from 'react'
import './App.css'


export default function Register() {
const [form, setForm] = useState({ username: '', email: '', password:
'' });
const [error, setError] = useState(null);
const [success, setSuccess] = useState(false);

const handleChange = e => setForm({ ...form, [e.target.name]:
e.target.value });

const handleSubmit = async e => {
e.preventDefault();
try {
await api.post('/register/', form);
setSuccess(true);
} catch (err) {
setError(err.response?.data || 'Error en el registro');
}
};

if (success) return <p>¡Registro exitoso! Ahora puedes iniciar
sesión.</p>;

return (
     <form onSubmit={handleSubmit}>
{error && <p style={{ color: 'red'
}}>{JSON.stringify(error)}</p>}
    <>
      <h1>Registro</h1>
      <div className="card">
        
        
      <input name='username' placeholder='Usuario' 
      value={form.username} onChange={handleChange} />
      <input name='email' type='email' placeholder='Correo' 
      value={form.email} onChange={handleChange}   />
      <input name='password' type='password' placeholder='Contraseña' 
      value={form.password} onChange={handleChange}  /> 
        
        <button type='submit'>Registrarse</button>
      </div>
      <p className="read-the-docs">
        Registrate para poder acceder.
      </p>
    </>
  </form>



 )

 






}
