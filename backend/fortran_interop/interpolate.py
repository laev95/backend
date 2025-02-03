import ctypes as ct
from os import path
from .CModel import CGeoValuesArray
from typing import List


file_path = path.dirname(__file__)
LIB_GRAV_INTER = ct.CDLL(file_path + "/lib/libGravityInterpolation.so")


def interpolate_array(x: list[float], y: list[float], e_h: list[float], n_h: list[float], inter: str, coord: str) -> list:
    len_arrays = len(x)
    geo_arrays = CGeoValuesArray(x, y, e_h, n_h, len_arrays, inter, coord)

    interpolate_gravity             = LIB_GRAV_INTER.dogravityinterpolation_array
    interpolate_gravity.argtypes    = [
                                        ct.POINTER(ct.c_double * len_arrays),
                                        ct.POINTER(ct.c_double * len_arrays),
                                        ct.POINTER(ct.c_double * len_arrays),
                                        ct.POINTER(ct.c_double * len_arrays),
                                        ct.c_char_p,
                                        ct.c_char_p,
                                        ct.POINTER(ct.c_double * len_arrays),
                                        ct.POINTER(ct.c_int),
                                        ct.POINTER(ct.c_int * len_arrays),
                                        ct.POINTER(ct.c_int)
                                    ]

    interpolate_gravity(
         
        ct.byref(geo_arrays.x_arr),
        ct.byref(geo_arrays.y_arr),
        ct.byref(geo_arrays.eh_arr),
        ct.byref(geo_arrays.nh_arr),
        geo_arrays.i_type,
        geo_arrays.c_type,
        ct.byref(geo_arrays.ih_arr),
        ct.byref(geo_arrays.num_el),
        ct.byref(geo_arrays.int_flags),
        ct.byref(geo_arrays.err_flag)
         
    )

    return geo_arrays.convert_to_python()
