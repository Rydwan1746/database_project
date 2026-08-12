from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def border_checkpoint_dashboard_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to show traffic rates and recent border crossings for the active checkpoint
    checkpoint_id = request.GET.get('checkpoint', 'Main Terminal')
    return JsonResponse({
        "status": "success",
        "message": "Border checkpoint dashboard (stub)",
        "checkpoint": checkpoint_id,
        "metrics": {
            "traffic_rate_per_hour": 142,
            "recent_crossings_count": 10
        },
        "recent_crossings": [
            {"passport_number": "P123456", "direction": "ENTRY", "timestamp": "2026-08-12T11:00:00Z"},
            {"passport_number": "P987654", "direction": "EXIT", "timestamp": "2026-08-12T11:05:00Z"}
        ]
    })

def border_log_entry_view(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    if request.method == 'POST':
        # TODO(security): Validate input, verify traveler against travel bans or expired visas in MariaDB
        # TODO: Log the incoming/outgoing traveler in database
        passport_number = request.POST.get('passport_number')
        visa_number = request.POST.get('visa_number')
        direction = request.POST.get('direction') # ENTRY, EXIT
        
        return JsonResponse({
            "status": "success",
            "message": f"Traveler log for '{passport_number}' registered as {direction} (stub)",
            "validation_checks": {
                "travel_ban_check": "Passed",
                "visa_expiry_check": "Passed"
            }
        })
    
    return JsonResponse({"status": "info", "message": "Render border log entry form (stub)"})
