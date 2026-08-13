import json
from django.http import JsonResponse, HttpResponseNotAllowed
from .decorators import session_login_required

# ---------------------------------------------------------------------------
# TODO: Replace this mock record with a real MariaDB query once connected.
# Example query after models are generated via inspectdb:
#   from .models import Officer
#   officer = Officer.objects.filter(username=username).first()
# ---------------------------------------------------------------------------
MOCK_OFFICERS = {
    "admin": {
        "id": 1,
        "username": "admin",
        "password": "passport2026",   # TODO(security): Replace with hashed password check
        "role": "Administrator",
        "privilege_group": "Admin",
    },
    "border_officer": {
        "id": 2,
        "username": "border_officer",
        "password": "border2026",
        "role": "Border Control",
        "privilege_group": "Standard",
    },
}


def officer_login_view(request):
    """
    Authenticates an immigration officer and establishes a Django session.

    GET  → Signals React the login endpoint is available.
           Returns 200 with already_authenticated if session exists.
    POST → Reads JSON body {username, password}, validates credentials,
           sets session keys on success, and returns officer profile data.
    """
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        if request.session.get('officer_id'):
            return JsonResponse(
                {"status": "already_authenticated", "message": "Already logged in."},
                status=200
            )
        return JsonResponse({"status": "info", "message": "Submit credentials to log in."})

    # --- POST: Process login ---
    try:
        body = json.loads(request.body)
        username = body.get('username', '').strip()
        password = body.get('password', '').strip()
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse(
            {"status": "error", "message": "Invalid request body. Expected JSON."},
            status=400
        )

    # MUST NOT log credentials server-side (security requirement)
    if not username or not password:
        return JsonResponse(
            {"status": "error", "message": "Username and password are required."},
            status=400
        )

    # TODO: Replace mock lookup with real DB query once MariaDB is connected:
    #   officer = Officer.objects.filter(username=username).first()
    #   if not officer or not check_password(password, officer.password_hash):
    officer = MOCK_OFFICERS.get(username)
    if not officer or officer['password'] != password:
        # Generic message — never reveal which field is wrong
        return JsonResponse(
            {"status": "error", "message": "Invalid credentials."},
            status=401
        )

    # Credentials valid — regenerate session ID to prevent session fixation attacks
    request.session.cycle_key()
    request.session['officer_id'] = officer['id']
    request.session['username'] = officer['username']
    request.session['role'] = officer['role']
    request.session['privilege_group'] = officer['privilege_group']

    return JsonResponse({
        "status": "success",
        "message": "Login successful.",
        "officer": {
            "id": officer['id'],
            "username": officer['username'],
            "role": officer['role'],
            "privilege_group": officer['privilege_group'],
        }
    })


def officer_logout_view(request):
    """
    Destroys the active session server-side and clears the session cookie.

    POST only. Uses session.flush() to fully invalidate the session in the DB,
    not just clear() which empties the dict but keeps the session ID active.
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    if not request.session.get('officer_id'):
        return JsonResponse(
            {"status": "error", "message": "No active session to log out from."},
            status=400
        )

    request.session.flush()  # Fully destroys session in DB and clears cookie
    return JsonResponse({"status": "success", "message": "Logged out successfully."})


@session_login_required
def officer_profile_view(request):
    """
    Returns the currently authenticated officer's profile from the session.
    React calls GET /officers/me/ on app startup to check login state.
    Returns 401 if no session exists (handled by the decorator).
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return JsonResponse({
        "status": "success",
        "officer": {
            "id": request.session.get('officer_id'),
            "username": request.session.get('username'),
            "role": request.session.get('role'),
            "privilege_group": request.session.get('privilege_group'),
        }
    })


@session_login_required
def officer_management_list_view(request):
    """
    Lists all system officers with optional search and role filtering.
    Requires an active officer session.
    GET only — accepts ?q= (name search) and ?role= (filter by role).
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    search_query = request.GET.get('q', '')
    role_filter = request.GET.get('role', '')

    # TODO: Replace with real MariaDB ORM query once connected:
    #   officers = Officer.objects.all()
    #   if search_query: officers = officers.filter(username__icontains=search_query)
    #   if role_filter:  officers = officers.filter(role=role_filter)
    return JsonResponse({
        "status": "success",
        "message": "Officer list (stub — replace with DB query)",
        "filters": {"search_query": search_query, "role": role_filter},
        "officers": [
            {"id": 1, "username": "admin", "role": "Administrator", "privilege_group": "Admin"},
            {"id": 2, "username": "border_officer", "role": "Border Control", "privilege_group": "Standard"},
        ]
    })

