from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def citizen_list_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    # TODO: Query legacy MariaDB database with paginated results and search parameter `q`
    return JsonResponse({
        "status": "success",
        "message": "Citizen list (stub)",
        "query": query,
        "page": page,
        "citizens": [
            {"id": 101, "name": "Jane Doe", "national_id": "GH-123456", "phone": "+233240000000"},
            {"id": 102, "name": "John Smith", "national_id": "GH-654321", "phone": "+233240000001"}
        ]
    })

def citizen_detail_view(request, citizen_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Fetch full demographic data, linked passport records, and associated documents from MariaDB
    return JsonResponse({
        "status": "success",
        "message": "Citizen details (stub)",
        "citizen_id": citizen_id,
        "details": {
            "name": "Jane Doe",
            "national_id": "GH-123456",
            "phone": "+233240000000",
            "dob": "1995-05-15",
            "address": "123 Ring Road, Accra",
            "linked_passports": [
                {"passport_number": "P123456", "status": "Active", "expiry": "2030-01-01"}
            ],
            "associated_documents": [
                {"document_id": 50, "document_type": "Birth Certificate", "verification_status": "Verified"}
            ]
        }
    })

def citizen_create_view(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Validate input and register a new citizen into the legacy MariaDB table
        return JsonResponse({"status": "success", "message": "Citizen created successfully (stub)"})
    
    return JsonResponse({"status": "info", "message": "Render citizen creation form (stub)"})

def citizen_update_view(request, citizen_id):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Validate input and modify existing demographic/address data in MariaDB
        return JsonResponse({"status": "success", "message": "Citizen updated successfully (stub)", "citizen_id": citizen_id})
    
    return JsonResponse({"status": "info", "message": "Render citizen update form (stub)", "citizen_id": citizen_id})
