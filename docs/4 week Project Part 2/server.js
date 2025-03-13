const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');

// Пример "хранилища" (вместо базы данных)
let storage = [];

const app = express();
const port = 3000;

// Middleware
app.use(cors()); // Для разрешения запросов из клиентского интерфейса
app.use(bodyParser.json());

// Отдаём статические файлы из папки "public"
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint для получения всех файлов из "хранилища"
app.get('/api/storage', (req, res) => {
    res.json({ success: true, data: storage });
});

// Endpoint для добавления файла в "хранилище"
app.post('/api/storage', (req, res) => {
    const { name, content } = req.body;

    if (!name || !content) {
        return res.status(400).json({ success: false, message: "Имя и содержимое файла обязательны!" });
    }

    storage.push({ name, content });
    res.status(201).json({ success: true, message: 'Файл добавлен в хранилище!', data: { name, content } });
});

// Endpoint для удаления файла из "хранилища" по имени
app.delete('/api/storage/:name', (req, res) => {
    const { name } = req.params;
    storage = storage.filter(file => file.name !== name);
    res.json({ success: true, message: `Файл ${name} удалён из хранилища.` });
});

// Запуск сервера
app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});