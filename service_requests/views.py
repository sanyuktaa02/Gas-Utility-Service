from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        email = request.POST['email']
        service_type = request.POST['service_type']
        details = request.POST['details']
        file_attachment = request.FILES.get('file_attachment')

        request_obj = ServiceRequest.objects.create(
            customer_name=customer_name,
            email=email,
            service_type=service_type,
            details=details,
            file_attachment=file_attachment,
        )
        return JsonResponse({'message': 'Request submitted successfully', 'id': request_obj.id})

    return render(request, 'submit_request.html')

def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return JsonResponse({
        'customer_name': service_request.customer_name,
        'status': service_request.status,
        'submitted_at': service_request.submitted_at,
        'resolved_at': service_request.resolved_at,
    })
