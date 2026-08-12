from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

def document_verification_queue_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    # TODO: Query database to retrieve uploaded documents flagged for manual review
    return JsonResponse({
        "status": "success",
        "message": "Document verification manual review queue (stub)",
        "queue": [
            {"id": 501, "citizen_id": 101, "document_type": "Birth Certificate", "status": "Pending Review"},
            {"id": 502, "citizen_id": 102, "document_type": "National ID Card", "status": "Pending Review"}
        ]
    })

def document_verify_action_view(request, document_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    # TODO(security): Validate input, authenticate officer permissions
    # TODO: Mark document as Verified or Rejected in MariaDB, save failure notes if applicable
    status = request.POST.get('status') # Verified, Rejected
    notes = request.POST.get('notes', '')
    
    return JsonResponse({
        "status": "success",
        "message": f"Document status set to '{status}' (stub)",
        "document_id": document_id,
        "notes": notes
    })
