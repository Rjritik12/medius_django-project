import pandas as pd
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from.models import UploadFile

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        upload_file = UploadFile(file=file)
        upload_file.save()
        df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
        summary_report = generate_summary_report(df, file.name)
        return HttpResponse(summary_report)
    return render(request, 'upload.html')

def generate_summary_report(df, file_name):
    report = 'File Name: {}\n'.format(file_name)
    report += 'File Size: {}\n'.format(df.size)
    report += 'Number of Rows: {}\n'.format(df.shape[0])
    report += 'Number of Columns: {}\n'.format(df.shape[1])
    report += 'Column Names: {}\n'.format(df.columns.tolist())
    report += 'Data Types: {}\n'.format(df.dtypes.tolist())
    return report

