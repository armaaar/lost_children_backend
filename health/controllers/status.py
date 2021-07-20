from django.views import View
from django.http import JsonResponse

class StatusView(View):
    """View for checking if server works"""
    def get(self, request):
        """Return status code"""

        # Send response
        return JsonResponse({
            'status': 'OK - healthy'
        })
