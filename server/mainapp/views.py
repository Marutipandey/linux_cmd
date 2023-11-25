# import subprocess
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse,JsonResponse
# import os

# @csrf_exempt
# def execute_command(request):
#     if request.method == 'POST':
#         command = request.POST.get('command', '')
#         output = run_command(command)
#         request.session['output'] = output
#         save_output_to_file(output)

#         return JsonResponse({'output': output})

#     return JsonResponse({'output': ''})

# def download_output(request):
#     file_path = r'D:\recovery\desk\ghost ap\ghost\server\output.txt'

#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as file:
#             response = HttpResponse(file.read(), content_type='text/plain')
#             response['Content-Disposition'] = 'attachment; filename=output.txt'
#             return response

#     else:
#         return HttpResponse('Output file not found.')

# def run_command(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, error = process.communicate()
#     output = output.decode('utf-8')

#     if error:
#         return f"Error: {error.decode('utf-8')}"

#     return output

# def save_output_to_file(output):
#     file_path = r'D:\recovery\desk\ghost ap\ghost\server\output.txt'

#     with open(file_path, 'w') as file:
#         file.write(output)

# import subprocess
# import os
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['POST'])
# def execute_command(request):
#     if request.method == 'POST':
#         command = request.data.get('command', '')
#         output = run_command(command)
#         return Response({'output': output})

#     return Response({'output': ''})

# def run_command(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, error = process.communicate()
#     output = output.decode('utf-8').strip()  # Remove leading/trailing whitespace

#     if error:
#         return f"Error: {error.decode('utf-8')}"

#     return output

# def save_output_to_file(output):
#     file_path = r'C:\Users\Yashn\Downloads\ezyzip (1)\server\output.txt'

#     with open(file_path, 'w') as file:
#         file.write(output)
import subprocess
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse


@api_view(['POST'])
def execute_command(request):
    if request.method == 'POST':
        command = request.data.get('command', '')
        output = run_command(command)
        return Response({'output': output})

    return Response({'output': ''})

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8').strip()  # Remove leading/trailing whitespace

    if error:
        return f"Error: {error.decode('utf-8')}"

    with open('output.txt', 'w+') as output_file:
        output_file.write(f"Command: {command}\n")
        output_file.write(f"Output:\n{output}\n")
        output_file.write('-' * 50 + '\n')

    return output

@api_view(['GET'])
def download_output(request):
    file_path = r'C:\Users\Yashn\Downloads\ezyzip (1)\server\output.txt'

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = Response(file.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=output.txt'
            return response

    else:
        return Response('Output file not found.')