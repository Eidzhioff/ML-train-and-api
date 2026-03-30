# ML-train-and-api: Предсказание цены на автомобиль

Проект представляет собой ML-сервис для предсказания стоимости автомобиля на основе его характеристик. Включает в себя обученную модель, REST API и веб-интерфейс.

## 📋 Описание

Сервис принимает на вход параметры автомобиля (тип двигателя, размеры, мощность и др.) и возвращает предсказанную цену. Модель обучается на датасете с характеристиками автомобилей.

## 🏗️ Архитектура проекта

```
ML-train-and-api/
├── app.py              # FastAPI сервер для предсказаний
├── interface.py        # Streamlit веб-интерфейс
├── model.pkl           # Обученная ML-модель
├── config.json         # Конфигурация признаков
├── train.ipynb         # Ноутбук для обучения модели
├── load_model.ipynb    # Ноутбук для загрузки и тестирования
├── requirements.txt    # Зависимости проекта
├── Dockerfile          # Docker-конфигурация
└── data/
    ├── carprice.csv    # Исходный датасет
    └── carprice_gen.csv # Сгенерированный датасет
```

## 🚀 Быстрый старт

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск API

```bash
python app.py
```

API будет доступно по адресу: `http://127.0.0.1:5000`

### Запуск веб-интерфейса

```bash
streamlit run interface.py
```

## 📡 API Endpoints

### Проверка статуса

```bash
GET /status
```

**Ответ:**
```json
{ "status": "ok" }
```

### Предсказание цены

```bash
POST /get_predict
Content-Type: application/json
```

**Пример запроса:**
```json
{
  "symboling": 0,
  "CarName": "ford focus",
  "fueltype": "gas",
  "aspiration": "std",
  "doornumber": "four",
  "carbody": "sedan",
  "drivewheel": "fwd",
  "enginelocation": "front",
  "wheelbase": 104.3,
  "carlength": 178.5,
  "carwidth": 69.5,
  "carheight": 57.9,
  "curbweight": 2850,
  "enginetype": "ohc",
  "cylindernumber": "four",
  "enginesize": 122,
  "fuelsystem": "mpfi",
  "boreratio": 3.31,
  "stroke": 3.54,
  "compressionratio": 10.0,
  "horsepower": 120,
  "peakrpm": 6000,
  "citympg": 26,
  "highwaympg": 36
}
```

**Ответ:**
```json
{ "prediction": [15000.50] }
```

## 🐳 Docker

### Сборка образа

```bash
docker build -t car-price-api .
```

### Запуск контейнера

```bash
docker run -p 1703:5000 car-price-api
```

## 📊 Признаки модели

| Категория | Признаки |
|-----------|----------|
| **Числовые** | wheelbase, carlength, carwidth, carheight, curbweight, enginesize, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg |
| **Бинарные** | fueltype, aspiration, doornumber, enginelocation |
| **Категориальные** | carbody, drivewheel, enginetype, cylindernumber, fuelsystem, car_company, car_model, symboling |

## 🛠️ Технологии

- **FastAPI** — REST API фреймворк
- **Streamlit** — веб-интерфейс
- **Scikit-learn** — ML-модель и предобработка
- **Pandas/NumPy** — работа с данными
- **Pydantic** — валидация данных
- **Docker** — контейнеризация