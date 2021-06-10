"""Contact views."""

# Django
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

# Forms
from .forms import ContactForm


def contact(request):

    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get("nombre")
            email = request.POST.get("email")
            content = request.POST.get("contenido")
            email = EmailMessage(
                "Mensaje desde App Django",
                "El usuario con nombre {} con la diireccion {} escribe lo siguiente:\n\n {}".format(name, email, content),
                "", ["julianhdelgado0404@gmail.com"],
                reply_to=[email]
                )
            try:
                email.send()
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?Novalido")
    return render(request, "contact/contact.html", {"contact_form": contact_form} )
