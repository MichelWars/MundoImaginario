# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import youtube_link_video
from urllib.parse import urlparse, parse_qs


#Essa signal pega o link de compartilhamento padrão que o usuario salva no banco de dados e corverte para o formato embed para ser visualizado na pagina html
@receiver(pre_save, sender=youtube_link_video)
def convert_youtube_link(sender, instance, **kwargs):
    # Converte o link padrão do YouTube para o formato de embed
    parsed_url = urlparse(instance.link)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"] and parsed_url.path == "/watch":
        video_id = parse_qs(parsed_url.query).get("v")
        if video_id:
            instance.link = f"https://www.youtube.com/embed/{video_id[0]}"
    elif parsed_url.hostname == "youtu.be":
        # Converte links no formato youtu.be/<id> para embed
        video_id = parsed_url.path.lstrip("/")
        instance.link = f"https://www.youtube.com/embed/{video_id}"
