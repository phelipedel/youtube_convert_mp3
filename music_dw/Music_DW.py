import youtube_dl
from lib.utilidade import cor

while True :
    v_url = input ( 'Link do video: ' )
    video_info = youtube_dl.YoutubeDL ( ).extract_info (
        url = v_url , download = False
    )
    filename = f"{video_info [ 'title' ]}.mp3"
    option = {
        'format' : 'bestaudio/best' ,
        'keepvideo' : False ,
        'outtmpl' : filename ,
    }

    with youtube_dl.YoutubeDL ( option ) as ydl :
        ydl.download ( [ video_info [ 'webpage_url' ] ] )

    print ( f'Download Completo... {filename}' )
    r = str ( input ( 'Quer salvar mais algum? [S/N]' ) ).upper ( ) [ 0 ]
    if r == 'N' :
        break
