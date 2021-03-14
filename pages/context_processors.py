from .models import Contact


def global_context(request):
    contact_list = Contact.objects.all()

    if not contact_list:
        return {}

    return {
        "email": contact_list[0].email,
        "phone": contact_list[0].phone,
        "facebook": contact_list[0].facebook,
        "instagram": contact_list[0].instagram,
    }