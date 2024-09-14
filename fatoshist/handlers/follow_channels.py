from ..bot.bot import bot
from ..config import CHANNEL
from ..loggers import logger


def msg_inscricao_canais_historia():
    try:
        msg = (
            '🌟 📺 <b>Junte-se ao nosso incrível canal de História</b> 📺 🌟\n\n'
            'Amigos, descubram a magia da história através dos nossos canais envolventes e emocionantes! '
            'Junte-se a nós agora para desfrutar de uma ampla variedade de programas e documentários que levarão você '
            'em uma emocionante jornada pelas profundezas da história.\n\n'
            'Viva aventuras antigas, fatos intrigantes e eventos cruciais que moldaram o nosso mundo. '
            'Junte-se a nós hoje para uma experiência educativa divertida e esclarecedora!\n\n'
            '<blockquote>🌍 Clique no link para acessar a lista de canais de História: [@history_channels]</blockquote>'
        )
        bot.send_message(
            CHANNEL,
            msg,
            parse_mode='HTML',
        )
    except Exception as e:
        logger.error('Erro ao enviar mensagens históricas no canal:', str(e))
