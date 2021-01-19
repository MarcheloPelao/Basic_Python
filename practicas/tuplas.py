# formatos_audio=('wav','mp3')
# formatos_videos= tuple(['avi','mov','mp4'])
# formatos_imagen=('png','jpg','tiff')
# formatos_documentos=('pdf',)
# print(formatos_audio)
# print(formatos_documentos)
# formatos=[formatos_audio,
#           formatos_imagen,
#           formatos_videos,
#           formatos_documentos]
# print(formatos) #lista de tuplas
#
# #recorrer tuplas con buble for:
#
# for formato in formatos_imagen:
#     print(formato, end=' ')

formatos='avi','mp3','pdf'
video,audio,doc=formatos #unpacking
print(video)
print(audio)
print(doc)
