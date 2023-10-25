import  ctypes      as      ct
from    os          import  path
from    .Cmodels    import  CGeoValuesArray


DIR_NAME        = path.dirname(__file__)
LIB_GRAV_INTER  = ct.CDLL(DIR_NAME + '/lib/libGravityInterpolation.so')


def interpolate_array(x_coords: list[float], y_coords: list[float], elli_h: list[float], norm_h: list[float],
                      inter_type: str, coord_type: str):

    len_arrays   = len(x_coords)
    input_types  = [
                    ct.POINTER(ct.c_double*len_arrays),
                    ct.POINTER(ct.c_double*len_arrays),
                    ct.POINTER(ct.c_double*len_arrays),
                    ct.POINTER(ct.c_double*len_arrays),
                    ct.c_char_p,
                    ct.c_char_p,
                    ct.POINTER(ct.c_double*len_arrays),
                    ct.POINTER(ct.c_int),
                    ct.POINTER(ct.c_int*len_arrays),
                    ct.POINTER(ct.c_int)
                    ]

    interpolate_gravity             = LIB_GRAV_INTER.dogravityinterpolation_array
    interpolate_gravity.argtypes    = input_types
    interpolate_gravity.restype     = ct.c_void_p

    geo_arrays = CGeoValuesArray(x_coords, y_coords, elli_h, norm_h, len_arrays, inter_type, coord_type)

    interpolate_gravity(
                        ct.byref(geo_arrays.x_arr),
                        ct.byref(geo_arrays.y_arr),
                        ct.byref(geo_arrays.eh_arr),
                        ct.byref(geo_arrays.nh_arr),
                        geo_arrays.i_type,
                        geo_arrays.system,
                        ct.byref(geo_arrays.ih_arr),
                        ct.byref(geo_arrays.num_el),
                        ct.byref(geo_arrays.int_flags),
                        ct.byref(geo_arrays.err_flag)
                        )

    return geo_arrays.convert_to_python()
