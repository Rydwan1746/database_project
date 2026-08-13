import functools
from django.http import JsonResponse


def session_login_required(view_func):
    """
    A React-friendly authentication guard decorator.

    Checks for an active officer session before allowing access to a view.
    Returns HTTP 401 Unauthorized as JSON instead of Django's default redirect
    to a login page, since React handles routing on the client side.

    Usage:
        from officers.decorators import session_login_required

        @session_login_required
        def my_protected_view(request):
            ...
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check for a valid officer session key
        if not request.session.get('officer_id'):
            return JsonResponse(
                {"status": "error", "message": "Authentication required. Please log in."},
                status=401
            )
        # Session is valid — proceed to the actual view
        return view_func(request, *args, **kwargs)

    return wrapper
