from fatoshist.config import CHANNEL
import logging


def msg_alerta_stars(bot):
    try:
        caption = (
            '🌟 📺 <b>Apoiem o nosso canal reagindo às publicações com estrelas!</b> 📺 🌟\n\n'
            'As estrelas ajudam a incentivar nosso trabalho e a desbloquear novos recursos no canal. '
            'Vocês podem comprar estrelas diretamente pela Play Store e utilizá-las para reagir aos nossos posts. '
            'Cada estrela faz a diferença!\n\n'
            '#historia #ajude_canal #stars #estrelas #doe'
        )

        video_path = r'./fatoshistoricos/assets/stars_video.mp4'
        with open(video_path, 'rb') as video:
            bot.send_video(CHANNEL, video, caption=caption, parse_mode='HTML')

    except Exception as e:
        logging.error(f'Erro ao enviar vídeo com legenda no canal: {e}')
