from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def passport_application_list_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    status_filter = request.GET.get('status', '') # Pending, Under Review, Approved, Rejected
    # TODO: Query database to retrieve applications sorted by status filter
    return JsonResponse({
        "status": "success",
        "message": "Passport applications list (stub)",
        "filter": status_filter,
        "applications": [
            {"id": 201, "citizen_id": 101, "status": "Pending", "created_at": "2026-08-01"},
            {"id": 202, "citizen_id": 102, "status": "Under Review", "created_at": "2026-07-28"}
        ]
    })

def passport_application_detail_view(request, application_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to show applicant details and security/background flags
    return JsonResponse({
        "status": "success",
        "message": "Passport application detail (stub)",
        "application_id": application_id,
        "details": {
            "application_id": application_id,
            "citizen_name": "Jane Doe",
            "citizen_id": 101,
            "status": "Pending",
            "background_check_passed": True,
            "flags": ["No active travel bans"]
        }
    })

def passport_application_create_view(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Validate input, check for active citizen ID, and register a new application in MariaDB
        return JsonResponse({"status": "success", "message": "Passport application created successfully (stub)"})
    
    return JsonResponse({"status": "info", "message": "Render passport application creation form (stub)"})

def passport_review_action_view(request, application_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    # TODO(security): Officer authentication & permissions check.
    # TODO: Perform state transition: Approve/Reject/Request Info in MariaDB.
    action = request.POST.get('action') # Approve, Reject, Request Info
    notes = request.POST.get('notes', '')
    
    return JsonResponse({
        "status": "success",
        "message": f"Action '{action}' executed on passport application (stub)",
        "application_id": application_id,
        "notes": notes
    })
