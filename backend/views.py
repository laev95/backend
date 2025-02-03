from rest_framework.decorators      import api_view
from rest_framework.response        import Response
from .fortran_interop.interpolate   import interpolate_array
from rest_framework                 import status


@api_view(["POST"])
def process_geo_data(request) -> Response:
    if request.method == "POST":
        return Response(interpolate_array(*request.data.values()), status=status.HTTP_200_OK)