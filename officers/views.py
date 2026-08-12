from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def officer_login_view(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Authenticate officer using credentials stored in MariaDB & set session flags
        return JsonResponse({"status": "success", "message": "Officer logged in successfully (stub)"})
    
    # GET request
    return JsonResponse({"status": "info", "message": "Render officer login form (stub)"})

def officer_logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    # TODO(security): Clear session and redirect to login screen
    return JsonResponse({"status": "success", "message": "Officer logged out successfully (stub)"})

def officer_management_list_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to list system officers with search and filtering by role/privilege group
    search_query = request.GET.get('q', '')
    role_filter = request.GET.get('role', '')
    
    return JsonResponse({
        "status": "success",
        "message": "List system officers (stub)",
        "filters": {
            "search_query": search_query,
            "role": role_filter
        },
        "officers": [
            {"id": 1, "username": "officer_alpha", "role": "Border Control", "privilege_group": "Standard"},
            {"id": 2, "username": "officer_beta", "role": "Visa Processing", "privilege_group": "Admin"}
        ]
    })
