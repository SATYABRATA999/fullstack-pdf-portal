from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from .models import Document
from .serializers import DocumentSerializer
import os

class DocumentUploadView(APIView):
    def post(self, request):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file.name.endswith('.pdf'):
            return Response({'error': 'Only PDF files allowed'}, status=400)

        document = Document.objects.create(
            filename=uploaded_file.name,
            file=uploaded_file,
            filesize=uploaded_file.size
        )
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=201)


class DocumentListView(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-created_at')
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)


class DocumentDownloadView(APIView):
    def get(self, request, pk):
        try:
            doc = Document.objects.get(pk=pk)
            return FileResponse(doc.file, as_attachment=True)
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=404)


class DocumentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            doc = Document.objects.get(pk=pk)
            path = doc.file.path
            doc.delete()
            if os.path.exists(path):
                os.remove(path)
            return Response({'message': 'File deleted successfully'})
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=404)

