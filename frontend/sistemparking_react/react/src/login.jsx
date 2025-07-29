import React from 'react'
import { useState } from 'react';
import './App.css'

export default function Login() {
const [form, setForm] = useState({ username: '', password: '' });
const [error, setError] = useState(null);
const navigate = useNavigate();

const handleChange = e => setForm({ ...form, [e.target.name]:
e.target.value });

const handleSubmit = async e => {
e.preventDefault();
try {
const res = await api.post('/login/', form);
localStorage.setItem('token', res.data.token);
navigate('/dashboard');
} catch {
setError('Usuario o contraseña incorrectos');
}
};

return (
<form onSubmit={handleSubmit}>
<h2>Iniciar Sesión</h2>
{error && <p style={{ color: 'red' }}>{error}</p>}
<input name='username' placeholder='Usuario'
value={form.username} onChange={handleChange} />
<input name='password' type='password' placeholder='Contraseña'
value={form.password} onChange={handleChange} />
<button type='submit'>Entrar</button>
</form>
);
}