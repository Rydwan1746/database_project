from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def visa_queue_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to retrieve pending visa applications requiring officer review
    return JsonResponse({
        "status": "success",
        "message": "Visa applications pending queue (stub)",
        "queue": [
            {"id": 301, "applicant_name": "Alice Johnson", "category": "Tourist", "submission_date": "2026-08-05"},
            {"id": 302, "applicant_name": "Bob Marley", "category": "Business", "submission_date": "2026-08-08"}
        ]
    })

def visa_detail_view(request, visa_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to retrieve details (travel dates, sponsor details, category)
    return JsonResponse({
        "status": "success",
        "message": "Visa application detail (stub)",
        "visa_id": visa_id,
        "details": {
            "visa_id": visa_id,
            "applicant_name": "Alice Johnson",
            "category": "Tourist",
            "travel_dates": {"start": "2026-09-01", "end": "2026-09-30"},
            "sponsor_details": "Self-sponsored",
            "passport_number": "P888888"
        }
    })

def visa_process_view(request, visa_id):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Validate input, check officer credentials, execute state change (issue or deny) in MariaDB
        decision = request.POST.get('decision') # Issued, Denied
        comments = request.POST.get('comments', '')
        return JsonResponse({
            "status": "success",
            "message": f"Visa processing decision '{decision}' recorded (stub)",
            "visa_id": visa_id,
            "comments": comments
        })
    
    return JsonResponse({"status": "info", "message": "Render visa processing form (stub)", "visa_id": visa_id})
