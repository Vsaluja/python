from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeView(APIView):
    # myEmp = [{
    #     "name": "vansh",
    #     "occupation": "Software dev"
    # }, {
    #     "name": "rohan",
    #     "occupation": "UI/UX Desginer"
    # }]

    def get(self, request):
        return Response({"message": "Hello world"})


# Render start command
# gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000
# gunicorn deploy.wsgi:application --bind 0.0.0.0:8000
