'''
Created on May 6, 2015

@author: eytan
'''
from django.db import transaction
from django.db.models.aggregates import Max, Min
from rest_framework import status
from rest_framework.response import Response


@transaction.atomic
def safe_upload(request, model, serializer_class):
    try:
        count_all = model.objects.count()
        if count_all <= 2000:
            model.objects.all().delete()
        else:
            max_id = model.objects.aggregate(Max('id'))['id__max']
            min_id = model.objects.aggregate(Min('id'))['id__min']
            for safe_id in xrange(min_id, max_id, 2000):
                model.objects.filter(id__lt=safe_id).all().delete()
        
        serializer = serializer_class(data=request.DATA, files=request.FILES, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
