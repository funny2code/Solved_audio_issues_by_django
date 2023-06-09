from django.shortcuts import render

from django.http import HttpResponse, StreamingHttpResponse
import os
from django.conf import settings


def choose_audio(request):
    context = {}
    return render(request, 'choose_audio.html', context)
    

class Button:
    def __init__(self, label, time):
        self.label = label
        self.time = time

def audio_test(request, pk):

    print (pk)

    if pk == 1:
        audio_file = "audio/admiral_mcraven_speech.mp3"
    elif pk == 2:
        audio_file = 'audio/eric_sprott.mp3'
    elif pk == 3:
        audio_file = "audio/david_lin_interview_doomberg.mp3"
    else:
        audio_file = "audio/forward_guidance_micheal_pettis.mp3"

    buttons_list = [
        Button('Skip to 0:00', 0),
        Button('Skip to 1:00', 60),
        Button('Skip to 2:00', 120),
        Button('Skip to 3:00', 180),
        Button('Skip to 4:00', 240)
    ]

    buttons = buttons_list

    # Get 'time' query parameter, default to 0 if not provided
    timestamp = request.GET.get('time', 0)

    context = {
        'audio_file': audio_file,
        'buttons': buttons,
        'timestamp': timestamp
    }
    return render(request, 'audio_test.html', context)

def audio_speed(request, speed):
    audio_speeds = {'1.5': 1.5, '2.0': 2.0}
    audio_speed = audio_speeds.get(speed, 1.0)
    return JsonResponse({'status': 'success', 'audio_speed': audio_speed})

def audio_forward(request):
    print ('Audio forward')
    return JsonResponse({'status': 'success', 'forward_time': 10})

def audio_backward(request):
    print ('Audio backward')
    return JsonResponse({'status': 'success', 'backward_time': 10})
















# ### this works ###
# def audio_test(request, pk):

#     print (pk)

#     if pk == 1:
#         file_path = "staticfiles/audio/admiral_mcraven_speech.mp3"
#     elif pk == 2:
#         file_path = 'staticfiles/audio/eric_sprott.mp3'
#     elif pk == 3:
#         file_path = "staticfiles/audio/david_lin_interview_doomberg.mp3"
#     else:
#         file_path = "staticfiles/audio/forward_guidance_micheal_pettis.mp3"

#     # file_path = "staticfiles/audio/admiral_mcraven_speech.mp3"
#     # file_path = 'staticfiles/audio/eric_sprott.mp3'
#     # file_path = "staticfiles/audio/all_in_rkj_interview.mp3"
#     # file_path = "staticfiles/audio/david_lin_interview_doomberg.mp3"
#     # file_path = "staticfiles/audio/forward_guidance_micheal_pettis.mp3"

#     file_size = os.path.getsize(file_path)
#     range_header = request.headers.get('Range')
#     if range_header:
#         start, end = range_header.split('=')[1].split('-')
#         start = int(start)
#         end = int(end) if end else file_size - 1
#         content_length = end - start + 1
#         with open(file_path, 'rb') as f:
#             f.seek(start)
#             data = f.read(content_length)
#         response = HttpResponse(data, content_type='audio/mpeg', status=206)
#         response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
#     else:
#         response = HttpResponse(content_type='audio/mpeg')
#         response['Content-Disposition'] = 'inline; filename="file.mp3"'
#         response['Content-Length'] = file_size
#         with open(file_path, 'rb') as f:
#             response.write(f.read())

#     return response






# def audio_test(request):
#     file_path = "staticfiles/audio/forward_guidance_micheal_pettis.mp3"
#     file_size = os.path.getsize(file_path)
#     range_header = request.headers.get('Range')
#     if range_header:
#         start, end = range_header.split('=')[1].split('-')
#         start = int(start)
#         end = int(end) if end else file_size - 1
#         content_length = end - start + 1
#         with open(file_path, 'rb') as f:
#             f.seek(start)
#             data = f.read(content_length)
#         response = HttpResponse(data, content_type='audio/mpeg', status=206)
#         response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
#     else:
#         response = HttpResponse(content_type='audio/mpeg')
#         response['Content-Disposition'] = 'inline; filename="file.mp3"'
#         response['Content-Length'] = file_size
#         with open(file_path, 'rb') as f:
#             response.write(f.read())

#     # Pass the response as a context variable to the template
#     context = {'audio_response': response}
#     return render(request, 'audio_test.html', context)





# def audio_test(request):
#     audio_file = "audio/forward_guidance_micheal_pettis.mp3"
#     print (type(audio_file))
#     context = {
#         'audio_file': audio_file,
#     }
#     return render(request, 'audio_test.html', context)



# Create your views here.

# http://127.0.0.1:8000/

# https://github.com/yuong1979/audio_test

# def audio_test(request):

#     audio_file = "/audio/admiral_mcraven_speech.mp3"

#     # audio_file = '/audio/eric_sprott.mp3'
#     # audio_file = "/audio/all_in_rkj_interview.mp3"
#     # audio_file = "/audio/david_lin_interview_doomberg.mp3"
#     # audio_file = "/audio/forward_guidance_micheal_pettis.mp3"
#     context = {
#         'audio_file': audio_file,
#     }
#     return render(request, 'audio_test.html', context)





