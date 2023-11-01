import ctypes       as ct
from itertools      import repeat
from .spacebuffer   import space_buffer


class CGeoValuesArray:
    def __init__(self, x_coords, y_coords, elli_hs, norm_hs, n_values, inter_type, coord_type):
        self.x_arr      = (ct.c_double * n_values)(*x_coords)
        self.y_arr      = (ct.c_double * n_values)(*y_coords)
        self.eh_arr     = (ct.c_double * n_values)(*elli_hs)
        self.nh_arr     = (ct.c_double * n_values)(*norm_hs)

        self.i_type     = space_buffer(inter_type)
        self.c_type     = space_buffer(coord_type)

        self.ih_arr     = (ct.c_double * n_values)(*list(repeat(0, n_values)))
        self.num_el     = ct.c_int(n_values)
        self.int_flags  = (ct.c_int * n_values)(*list(repeat(0, n_values)))
        self.err_flag   = ct.c_int(0)

    def convert_to_python(self) -> list:
        python_values:      list[list] = []
        formatted_lists:    list[list] = []

        number_elems = self.num_el.value

        python_values.append(list(self.x_arr))
        python_values.append(list(self.y_arr))
        python_values.append(list(self.eh_arr))
        python_values.append(list(self.nh_arr))
        python_values.append(list(repeat(self.i_type.decode().strip(), number_elems)))
        python_values.append(list(repeat(self.c_type.decode().strip(), number_elems)))
        python_values.append(list(self.ih_arr))
        python_values.append(list(self.int_flags))
        python_values.append(list(repeat(self.err_flag.value, number_elems)))

        for i in range(self.num_el.value):
            tmp_list = []
            for lst in python_values:
                tmp_list.append(lst[i])
                
            formatted_lists.append(tmp_list)

        return formatted_lists
