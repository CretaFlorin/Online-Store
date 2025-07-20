from django.http import HttpResponse


def admin_required(view_func):
    def wrapper_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "admin":
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("Only admins can view this.")

    return wrapper_view
