import uvicorn
from fastapi import FastAPI
from server.routes.carRoute import car_router
from server.routes.userRoute import user_router
from server.routes.houseRoute import house_router

description = """
Ini adalah API untuk melakukan prediksi harga mobil-mobil bekas di Indonesia. Silakan masukan input yang sesuai dengan deksripsi di bawah ini untuk mendapatkan harga mobil bekas berdasarkan kriteria yang Anda masukkan. 🚀

Beberapa instance yang terdapat pada API ini:

## Users

Anda dapat melakukan:
* **Registrasion**
* **Login**

## Items

Anda dapat ...
"""

app = FastAPI(
    title="Car Price Prediction API",
    description=description
)
app.include_router(user_router)
app.include_router(car_router)
app.include_router(house_router)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8090, reload=True)