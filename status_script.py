import vk_api
import datetime
import time
    

while True:
    vk = vk_api.VkApi(token="71d9ffef00a5270a453e4e67b75a7b7f3647ecc21a52beeaf50d33a0fe1a322016f1439d573c9d8b23359")

    delta = datetime.timedelta(hours=3, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)
    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")
    counted = len(on)

    vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})

    vk.method("account.setOnline")

    time.sleep(300)



