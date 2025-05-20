

import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader=SoccerNetDownloader(LocalDirectory="C:\Python312\Lib\site-packages")


mySoccerNetDownloader.password = "s0cc3rn3t"
mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train","test","challenge"])
mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test", "challenge"])
#mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv"], split=["train","valid","test","challenge"])
#mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])
#mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2_PCA512.npy", "2_ResNET_TF2_PCA512.npy"], split=["train","valid","test","challenge"])
#mySoccerNetDownloader.downloadGames(files=["1_baidu_soccer_embeddings.npy", "2_baidu_soccer_embeddings.npy"], split=["train","valid","test","challenge"])