
import time
import telebot

TOKEN = '1886414390:AAEnQufO4Piz_RsYt0rY9dZzldHI2EdcZqg'

knownUsers = [] 
userStep = {}  

commands = { 
    
    'start'         : 'Iniciar el bot\n\n',
    'help'          : 'Muestra los comandos disponibles\n\n', 
    'macm'          : 'Conversion de Metros a Centimetros\n\n',
    'kam'           : 'Conversion de Kilometros a Metros\n\n',
    'makm'          : 'Conversion de Metros a Kilometros\n\n',
    'pieap'         : 'Conversion de Pie a Pulgadas\n\n'  
}
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuario detectado, pero no ha usado \"/start\" ")
        return 0


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
                    print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener) 


@bot.message_handler(commands=['start'])
def command_start(m):

    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola " +mention+"!" ,parse_mode="Markdown")

    if cid not in knownUsers: 
    
        knownUsers.append(cid)  
        userStep[cid] = 0 
       
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Me causa emocion que me hayas escrito.")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAO0YQ8M52iwda6I38qVWILyuvR1PagAAmILAAIWYGFLr_jq9I0EzgYgBA')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te encuentres muy bien")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Será un gusto ayudarte")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "El objetivo por el cual fui programado es para mostrarte las siguientes conversiones")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Metros a Centímetros. \nKilómetros a Metros. \nMillas a Kilómetros. \nPie a Pulgadas.")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Te las enviare en un momento")
        time.sleep(3)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAOzYQ8MwBVPAx_6d0mUqJA3rnffWh8AAkgCAAJWnb0KHPVy-NwpFNAgBA')

        time.sleep(10)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "La primera conversion que te enviaré es:")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Metros a Centímetros")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('m a cm.png', 'rb'))
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBsGEPVP-wCIiSZ12DDtTkZEq_fOfGAALSAQACFkJrCgpo79h_0FWBIAQ')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te sea de gran ayuda")

        cid = m.chat.id
        user_id = m.from_user.id 
        user_name = m.from_user.first_name 
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid,mention + " si necesitas consultar esta conversion en un futuro solo tienes que usar el comando /macm  ó puedes usar el bot *@Tarea4_Semana6_bot* para realizar mas consultas sobre conversiones de unidades de area", parse_mode="Markdown")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBfGEPUmHxseXzmgp52ZN8U4Hv8NY0AAKmDgACzYEhS1wXZT85bypsIAQ')
        
        time.sleep(10)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "La segunda conversion que te enviaré es:")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Kilómetros a Metros.")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('km a m.png', 'rb'))
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBsGEPVP-wCIiSZ12DDtTkZEq_fOfGAALSAQACFkJrCgpo79h_0FWBIAQ')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te sea de gran ayuda")
        
        cid = m.chat.id
        user_id = m.from_user.id 
        user_name = m.from_user.first_name 
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid,mention + " si necesitas consultar esta conversion en un futuro solo tienes que usar el comando /kam ó puedes usar el bot *@Tarea4_Semana6_bot* para realizar mas consultas sobre conversiones de unidades de area", parse_mode="Markdown")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBfGEPUmHxseXzmgp52ZN8U4Hv8NY0AAKmDgACzYEhS1wXZT85bypsIAQ')

        time.sleep(10)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "La tercera conversion que te enviaré es:")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Millas a Kilómetros.")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('milla km.png', 'rb'))
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBsGEPVP-wCIiSZ12DDtTkZEq_fOfGAALSAQACFkJrCgpo79h_0FWBIAQ')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te sea de gran ayuda")
        
        cid = m.chat.id
        user_id = m.from_user.id 
        user_name = m.from_user.first_name 
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid,mention + " si necesitas consultar esta conversion en un futuro solo tienes que usar el comando /makm ó puedes usar el bot *@Tarea4_Semana6_bot* para realizar mas consultas sobre conversiones de unidades de area", parse_mode="Markdown")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBfGEPUmHxseXzmgp52ZN8U4Hv8NY0AAKmDgACzYEhS1wXZT85bypsIAQ')
        
        time.sleep(10)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "La ultima conversion que te enviaré es:")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pie a Pulgadas.")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('pie a pulg.png', 'rb'))
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBsGEPVP-wCIiSZ12DDtTkZEq_fOfGAALSAQACFkJrCgpo79h_0FWBIAQ')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te sea de gran ayuda")
        
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid,mention + " si necesitas consultar esta conversion en un futuro solo tienes que usar el comando /pieap ó puedes usar el bot *@Tarea4_Semana6_bot* para realizar mas consultas sobre conversiones de unidades de area", parse_mode="Markdown")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBfGEPUmHxseXzmgp52ZN8U4Hv8NY0AAKmDgACzYEhS1wXZT85bypsIAQ')
        bot.send_chat_action(cid, 'typing')  
        time.sleep(3)
        bot.send_message(cid, "Adios " + mention + ", regresa pronto", parse_mode="Markdown")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIB4WEPYh_zqCgxnOe2uNfF_is4LePUAAJlDQACWEEhSXGhWBUqWqCjIAQ')
    else:
        bot.send_chat_action(cid, 'typing')  
        time.sleep(4)
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos")

@bot.message_handler(commands=['macm'])
def command_macm(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola de nuevo " +mention+"!, Está es la conversion de Metros a Centímetros" ,parse_mode="Markdown")
    bot.send_chat_action(cid, 'upload_photo')
    time.sleep(5)   
    bot.send_photo(cid, open('m a cm.png', 'rb'))
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Espero te sea de gran ayuda")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Adios " + mention + ", regresa pronto o puedes usar el comando /help para visualizar todos los comandos disponibles", parse_mode="Markdown")
        
@bot.message_handler(commands=['kam'])
def command_kam(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola de nuevo " +mention+"!, Está es la conversion de Kilómetros a Metros " ,parse_mode="Markdown")
    bot.send_chat_action(cid, 'upload_photo')
    time.sleep(5)   
    bot.send_photo(cid, open('km a m.png', 'rb'))
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Espero te sea de gran ayuda")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Adios " + mention + ", regresa pronto o puedes usar el comando /help para visualizar todos los comandos disponibles", parse_mode="Markdown")

@bot.message_handler(commands=['makm'])
def command_makm(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola de nuevo " +mention+"!, Está es la conversion de Millas a Kilómetros" ,parse_mode="Markdown")
    bot.send_chat_action(cid, 'upload_photo')
    time.sleep(5)   
    bot.send_photo(cid, open('milla km.png', 'rb'))
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Espero te sea de gran ayuda")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Adios " + mention + ", regresa pronto o puedes usar el comando /help para visualizar todos los comandos disponibles", parse_mode="Markdown")

@bot.message_handler(commands=['pieap'])
def command_pieap(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola de nuevo " +mention+"!, Está es la conversion de Pie a Pulgadas" ,parse_mode="Markdown")
    bot.send_chat_action(cid, 'upload_photo')
    time.sleep(5)   
    bot.send_photo(cid, open('pie a pulg.png', 'rb'))
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Espero te sea de gran ayuda")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Adios " + mention + ", regresa pronto o puedes usar el comando /help para visualizar todos los comandos disponibles", parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos están disponibles:\n\n\n"
    bot.send_chat_action(cid, 'typing')  
    time.sleep(5)
    for key in commands: 
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡Y no!")
    bot.send_sticker (m.chat.id, 'CAACAgIAAxkBAAO5YQ8PSGtokwxUBV-qzIUoO2nquboAAp8RAAIIoNBJeY4rQ3fKpYkgBA')
    bot.send_message(m.chat.id, "Yo no entiendo la palabra \"" + m.text + "\"\nUsa /start para usar el bot")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¡Qué esto no se vuelva a repetir!")
    bot.send_sticker (m.chat.id,'CAACAgIAAxkBAAPdYQthbfLBJlfwsYFoFgsH6_ykG3UAAoQAA0QNzxdaythEmzlA7iAE')
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¿Entendido?")

bot.infinity_polling()