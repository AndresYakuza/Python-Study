require('dotenv').config();
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Datos en memoria
let nextId = 1;
const items = [
  { id: nextId++, name: 'Aprender Angular' },
  { id: nextId++, name: 'Practicar Express' }
];

// Health
app.get('/health', (_req, res) => res.json({ ok: true }));

// CRUD
app.get('/items', (_req, res) => res.json(items));

app.post('/items', (req, res) => {
  const { name } = req.body || {};
  if (!name || !name.trim()) return res.status(400).json({ error: 'name requerido' });
  const item = { id: nextId++, name: String(name).trim() };
  items.push(item);
  res.status(201).json(item);
});

app.put('/items/:id', (req, res) => {
  const id = Number(req.params.id);
  const { name } = req.body || {};
  const idx = items.findIndex(i => i.id === id);
  if (idx === -1) return res.status(404).json({ error: 'no existe' });
  if (!name || !name.trim()) return res.status(400).json({ error: 'name requerido' });
  items[idx].name = String(name).trim();
  res.json(items[idx]);
});

app.delete('/items/:id', (req, res) => {
  const id = Number(req.params.id);
  const idx = items.findIndex(i => i.id === id);
  if (idx === -1) return res.status(404).json({ error: 'no existe' });
  const [deleted] = items.splice(idx, 1);
  res.json(deleted);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`API running on http://localhost:${port}`));
