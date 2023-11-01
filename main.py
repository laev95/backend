from fastapi import FastAPI
from fortran_interop.interpolate import interpolate_array


app = FastAPI()


@app.post("/interpolation/", status_code=200)
def interpolate(geo_data: dict):
    result = interpolate_array(*geo_data.values())
    return result
