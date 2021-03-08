from multiprocessing import Process, Pool
import os, time
import googleapiclient.discovery


def main_map(ID):
    
    command = 'youtube-dl -x --audio-format mp3 --audio-quality 160K {}'.format(ID)
    return os.system(command)


if __name__ == '__main__':
    
    playlist_id = "PLsyOSbh5bs16vubvKePAQ1x3PhKavfBIl"    
    
    if not os.path.isdir('audio_dl/'+playlist_id):
        os.mkdir('audio_dl/'+playlist_id)
    os.chdir('audio_dl/'+playlist_id)


    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBXFboGptNM1bS_uDEZ86HRmR5R2s6YOwU")

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    print(f"total: {len(playlist_items)}")
    #print(playlist_items)

    IDs = [playlist_items[c]['snippet']['resourceId']['videoId'] for c in range(len(playlist_items))]

    # 設定處理程序數量
    pool = Pool(20)

      # 運行多處理程序
    pool_outputs = pool.map(main_map, IDs)

      # 輸出執行結果
    print(pool_outputs)