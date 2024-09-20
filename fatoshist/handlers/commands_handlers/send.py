import logging

from telebot import TeleBot, types

from fatoshist.database.users import UserManager

user_manager = UserManager()


def register(bot: TeleBot):
    @bot.message_handler(commands=['sendon'])
    def cmd_sendon(message: types.Message):
        try:
            if message.chat.type != 'private':
                return
            user_id = message.from_user.id
            user = user_manager.get_user(user_id)

            if user:
                if user.get('msg_private') == 'true':
                    bot.reply_to(
                        message,
                        'Você já ATIVOU a função de receber eventos históricos no chat privado.',
                    )
                else:
                    user_manager.update_msg_private(user_id, 'true')
                    bot.reply_to(
                        message,
                        '<b>Eventos históricos no chat privado ATIVADO</b>. Você receberá fatos históricos todos os dias às 8 horas.',
                    )
            else:
                user_manager.add_user(user_id=message.from_user.id, username=message.from_user.username, first_name=message.from_user.first_name)
                bot.reply_to(message, 'Envie o comando novamente.')

        except Exception as e:
            logging.error(f'Erro ao ativar o recebimento dos eventos históricos: {str(e)}')

    @bot.message_handler(commands=['sendoff'])
    def cmd_sendoff(message):
        try:
            if message.chat.type != 'private':
                return
            user_id = message.from_user.id
            user = user_manager.get_user(user_id)

            if user:
                if user.get('msg_private') == 'false':
                    bot.reply_to(
                        message,
                        'Você já DESATIVOU a função de receber eventos históricos no chat privado.',
                    )
                else:
                    user_manager.update_msg_private(user_id, 'false')
                    bot.reply_to(
                        message,
                        '<b>Eventos históricos no chat privado DESATIVADO</b>. Você não receberá fatos históricos todos os dias às 8 horas.',
                    )
            else:
                user_manager.add_user(user_id=message.from_user.id, username=message.from_user.username, first_name=message.from_user.first_name)
                bot.reply_to(message, 'Envie o comando novamente.')

        except Exception as e:
            logging.error(f'Erro ao desativar o recebimento dos eventos históricos: {e}')
