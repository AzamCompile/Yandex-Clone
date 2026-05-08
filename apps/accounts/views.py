from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from apps.accounts.models import User
from apps.accounts.forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            login(request, user)
            return redirect("login")

    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form, 'hide_navbar': True})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("success")

        return render(request, "accounts/login.html", {"error": "Email yoki password xato"})

    return render(request, "accounts/login.html", )


def user_logout(request):
    logout(request)
    return redirect("login")

# Google

def send_google_auth(request):
    auth_url = (
        f"{settings.GOOGLE_AUTH_URL}"
        f"?client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )

    return redirect(auth_url)

def register_google_auth(request):
    code = request.GET.get('code')

    if not code:
        return JsonResponse({"error": "Google code kelmadi"}, status=400)

    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(settings.GOOGLE_TOKEN_URL, data=token_data)
    token_json = token_response.json()

    access_token = token_json.get("access_token")

    if not access_token:
        return JsonResponse({
            "error": "Access token olinmadi",
            "google_response": token_json
        }, status=400)

    user_info_response = requests.get(
        settings.GOOGLE_USER_INFO_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    user_info = user_info_response.json()

    email = user_info.get('email')
    name = user_info.get('name')

    if not email:
        return JsonResponse({"error": "Email kelmadi"}, status=400)


    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": email,
        }
    )

    login(request, user)

    return redirect('list')