import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, filters
from telegram import ReplyKeyboardMarkup, chataction, message
from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext import Updater, CommandHandler, updater
from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext.filters import Filters
from csv import writer
import pandas as pd



# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

total_price = {}
tedad = 0
Wallet = {}
Wallet2 = {}
sabad = {}
prices = {
    "ROG_PHONE5": 2800000,
    "APPLE_14PRO": 3300000,
    "XIOMI_9S": 800000,
    "SAMSUNG_S20": 2700000,
    "huawei_p30": 1000000
}

Rog = 20
Apple = 10
Xio = 20
Sam = 13
Huw = 15

total_price2 = {}
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to our store. Please choose the service you need from the menu below. Kindly select an option from the menu. '/menu' ")
    chat_id = update.message.chat_id
    fullname = update.message.from_user.full_name
    # logging.info("({} - {}) has entered the bot.".format(fullname, chat_id))
    List=[datetime.now(),chat_id,fullname,"Login","Not Available","Not Available","Not Available"]
    with open('commodities.csv', 'a') as f_object:

        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

    sabad[chat_id] = []
    Wallet[chat_id] = 0
    Wallet2[chat_id] = 0
    total_price[chat_id] = 0
    total_price2[chat_id] = 0


def guide(update: Update, context: CallbackContext):
    update.message.reply_text(
        "This bot was created for a university project in Semnan, and the python telegram bot library was used.")


###############################################################################################################################################


def menu(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([['Shopping cart'], ['Products'], ['Account recharge'], ['Discount Codes']],
                                   one_time_keyboard=False, resize_keyboard=True)
    update.message.reply_text(
        "Please select an option from the menu:", reply_markup=keyboard)


# #######################################################################################################################333
def menu2(update: Update, context: CallbackContext):
    if update.message.text == "Products":
        keyboard = ReplyKeyboardMarkup([['SAMSUNG S21'], ['APPLE Iphone 14PRO', 'XIOMI 9S'], ['HUAWEI P30', 'ROG PHONE 5'],
                                        ['Back to main menu']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text("Please select a product. Press 'Back to main menu' to return to the main menu:",
                                  reply_markup=keyboard)

# ######################################################################################################################33333333


def menu21(update: Update, context: CallbackContext):
    if update.message.text == "SAMSUNG S21":
        keyboard = ReplyKeyboardMarkup([['Add SAMSUNG to Cart'], [
                                       'Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"SAMSUNG S21: {Sam} available\nPrice: 2,700,000\nFor more information, visit: https://www.samsung.com/de/smartphones/galaxy-s21-ultra-5g/",
                                  reply_markup=keyboard)

# ##############################################################################################################################


def menu22(update: Update, context: CallbackContext):
    if update.message.text == "APPLE Iphone 14PRO":
        keyboard = ReplyKeyboardMarkup(
            [['Add APPLE to Cart'], ['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"APPLE Iphone 14PRO: {Apple} available\nPrice: 3,300,000\nFor more information, visit: https://www.apple.com/de/iphone-14-pro/",
                                  reply_markup=keyboard)

# ##########################################################################################################################3##


def menu23(update: Update, context: CallbackContext):
    if update.message.text == "XIOMI 9S":
        keyboard = ReplyKeyboardMarkup(
            [['Add Xiaomi to cart'], ['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Xiaomi 9S: {Xio} available\nPrice: 800,000\nFor more information, visit: https://www.mi.com/in/redmi-9/",
                                  reply_markup=keyboard)

# #############################################################################################################################################


def menu24(update: Update, context: CallbackContext):
    if update.message.text == "HUAWEI P30":
        keyboard = ReplyKeyboardMarkup(
            [['Add HUAWEI to Cart'], ['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Huawei P30: {Huw} available\nPrice: 1,000,000\nFor more information, visit: https://consumer.huawei.com/in/phones/p30-pro/",
                                  reply_markup=keyboard)

# #############################################################################################################################################

def menu25(update: Update, context: CallbackContext):
    if update.message.text == "ROG PHONE 5":
        keyboard = ReplyKeyboardMarkup(
            [['Add ROG to Cart'], ['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"ROG Phone 5: {Rog} available\nPrice: 2,800,000\nFor more information, visit: https://rog.asus.com/phones/rog-phone-5-model/",
                                  reply_markup=keyboard)
        
#############################################################################################################################################

def add_sam(update: Update, context: CallbackContext):

    if update.message.text == "Add SAMSUNG to Cart":
        global Sam
        if (Sam != 0):
            Sam = Sam-1
            chat_id = update.message.chat_id
            sabad[chat_id].append("SAMSUNG_S20")
            update.message.reply_text("Item successfully added to your cart")
            total_price[chat_id] += prices["SAMSUNG_S20"]
        else:
            update.message.reply_text("Item not available")


def add_rog(update: Update, context: CallbackContext):

    if update.message.text == "Add ROG to Cart":
        global Rog
        if (Rog != 0):
            Rog = Rog-1
            chat_id = update.message.chat_id
            sabad[chat_id].append("ROG_PHONE5")
            update.message.reply_text("Item successfully added to your cart")
            total_price[chat_id] += prices["ROG_PHONE5"]
        else:
            update.message.reply_text("Item not available")


def add_xiomi(update: Update, context: CallbackContext):

    if update.message.text == "Add Xiaomi to cart":
        global Xio
        if (Xio != 0):
            Xio = Xio-1
            chat_id = update.message.chat_id
            sabad[chat_id].append("XIOMI_9S")
            update.message.reply_text("Item successfully added to your cart")
            total_price[chat_id] += prices["XIOMI_9S"]
        else:
            update.message.reply_text("Item not available")


def add_apple(update: Update, context: CallbackContext):
    if update.message.text == "Add APPLE to Cart":
        global Apple
        if (Apple != 0):
            Apple = Apple-1
            chat_id = update.message.chat_id
            sabad[chat_id].append("APPLE_14PRO")
            update.message.reply_text("Item successfully added to your cart")
            total_price[chat_id] += prices["APPLE_14PRO"]
        else:
            update.message.reply_text("Item not available")


def add_HUAWEI(update: Update, context: CallbackContext):
    if update.message.text == "Add HUAWEI to Cart":
        global Huw
        if (Huw != 0):
            Huw = Huw-1
            chat_id = update.message.chat_id
            sabad[chat_id].append("huawei_p30")
            update.message.reply_text("Item successfully added to your cart")
            total_price[chat_id] += prices["huawei_p30"]
        else:
            update.message.reply_text("Item not available")


def removeall1(update: Update, context: CallbackContext):
    if update.message.text == "Clear Cart":
        sabad.clear()
        update.message.reply_text("Items removed successfully.")
        update.message.reply_text(f"Shopping cart: {sabad}")


######################################################################################################################################

def menu3(update: Update, context: CallbackContext):
    if update.message.text == "Discount Codes":
        Keyboard = ReplyKeyboardMarkup(
            [['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(
            "Discount code 1\nName: 1400\n20% off\nUnlimited usage\n\nDiscount code 2\nName: saman\n30% off\nUnlimited usage\n\nDiscount code 3\nName: bot\n25% off\nUnlimited usage\n\nPlease enter the discount code name 👇:", reply_markup=Keyboard)


def code_1400(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text == '1400':
        total_price[chat_id] = total_price[chat_id] * (80 / 100)
        update.message.reply_text("Discount code applied successfully.")


def code_saman(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text == 'saman':
        total_price[chat_id] = total_price[chat_id] * (70 / 100)
        update.message.reply_text("Discount code applied successfully.")


def code_bot(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text == 'bot':
        total_price[chat_id] = total_price[chat_id] * (75 / 100)
        update.message.reply_text("Discount code applied successfully.")


def menu4(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text == "Account recharge":
        fullname = update.message.from_user.full_name
        Keyboard = ReplyKeyboardMarkup([['Back'], ['5 Million'], ['10 Million'], [
                                       '20 Million'], ['30 Million']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(
            f"Hello {fullname}\nYour account balance is ${Wallet2[chat_id]}.\nYou can recharge your account by selecting the desired amount.", reply_markup=Keyboard)


def menu41(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    amt=None
    if update.message.text == "5 Million":
        amt=5000000
        chat_id = update.message.chat_id
        Wallet2[chat_id] = Wallet2[chat_id] + 5000000
        Keyboard = ReplyKeyboardMarkup([['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Your balance is {Wallet2[chat_id]}", reply_markup=Keyboard)
    elif update.message.text == "10 Million":
        amt=10000000
        chat_id = update.message.chat_id
        Wallet2[chat_id] = Wallet2[chat_id] + 10000000
        Keyboard = ReplyKeyboardMarkup([['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Your balance is {Wallet2[chat_id]}", reply_markup=Keyboard)
    elif update.message.text == "20 Million":
        amt=20000000
        chat_id = update.message.chat_id
        Wallet2[chat_id] = Wallet2[chat_id] + 20000000
        Keyboard = ReplyKeyboardMarkup([['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Your balance is {Wallet2[chat_id]}", reply_markup=Keyboard)
    elif update.message.text == "30 Million":
        amt=30000000
        chat_id = update.message.chat_id
        Wallet2[chat_id] = Wallet2[chat_id] + 30000000
        Keyboard = ReplyKeyboardMarkup([['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(f"Your balance is {Wallet2[chat_id]}", reply_markup=Keyboard)
    fullname = update.message.from_user.full_name
    # logging.info("({} - {} - ${} has been credited to account.)".format(fullname, chat_id, Wallet2[chat_id]))
    List=[datetime.now(),chat_id,fullname,"Credit","Not Available",amt, Wallet2[chat_id]]
    with open('commodities.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()
    read_file = pd.read_csv (r'commodities.csv')
    read_file.to_excel (r'Details.xlsx', index = None, header=True)

####################################################################################################################

def sabadd(update: Update, context: CallbackContext):
    if update.message.text == "Shopping cart":
        chat_id = update.message.chat_id
        keyboard = ReplyKeyboardMarkup([['Finalize Purchase'], ['Clear Cart'], ['Back']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text(
            f"Your shopping cart: {sabad[chat_id]}", reply_markup=keyboard)
        update.message.reply_text(
            f"Total price: {total_price[chat_id]}", reply_markup=keyboard)


def finish(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text == "Finalize Purchase":
        if Wallet2[chat_id] >= total_price[chat_id]:
            fullname = update.message.from_user.full_name
            Wallet2[chat_id] -= total_price[chat_id]
            
            List=[datetime.now(),chat_id,fullname,"Product",sabad[chat_id],total_price[chat_id], Wallet2[chat_id]]
            with open('commodities.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(List)
                f_object.close()
                    
            # logging.info("({} - {} - Product Name: {} - Price: {} - Account Balance: {}).".format(
            #     fullname, chat_id, sabad[chat_id], total_price[chat_id], Wallet2[chat_id]))
            update.message.reply_text(
                f"Receipt:\nProduct names: {sabad[chat_id]}\nQuantity: {len(sabad[chat_id])}\nPaid amount: {total_price[chat_id]} \n Account Balance:{Wallet2[chat_id]}")
            total_price[chat_id] -= total_price[chat_id]
            sabad[chat_id].clear()
            read_file = pd.read_csv (r'commodities.csv')
            read_file.to_excel (r'Details.xlsx', index = None, header=True)
            update.message.reply_text("Your purchase has been completed.")
        else:
            update.message.reply_text("Insufficient funds in your wallet.")


###########################################################################################
def main():
    updater = Updater("6103832657:AAHyMGRhUYV8BXTCj9FEoxCmnUJSevn4Of8")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("guide", guide))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(MessageHandler(Filters.regex("Products"), menu2))
    dp.add_handler(MessageHandler(Filters.regex("Discount Codes"), menu3))
    dp.add_handler(MessageHandler(Filters.regex("Account recharge"), menu4))
    dp.add_handler(MessageHandler(Filters.regex("SAMSUNG S21"), menu21))
    dp.add_handler(MessageHandler(Filters.regex("APPLE Iphone 14PRO"), menu22))
    dp.add_handler(MessageHandler(Filters.regex("XIOMI 9S"), menu23))
    dp.add_handler(MessageHandler(Filters.regex("HUAWEI P30"), menu24))
    dp.add_handler(MessageHandler(Filters.regex("ROG PHONE 5"), menu25))
    dp.add_handler(MessageHandler(Filters.regex("Back to Products"), menu2))
    dp.add_handler(MessageHandler(Filters.regex("Back"), menu))
    dp.add_handler(MessageHandler(Filters.regex("5 Million"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("10 Million"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("20 Million"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("30 Million"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("Add ROG to Cart"), add_rog))
    dp.add_handler(MessageHandler(Filters.regex("Add SAMSUNG to Cart"), add_sam))
    dp.add_handler(MessageHandler(Filters.regex("Add Xiaomi to cart"), add_xiomi))
    dp.add_handler(MessageHandler(Filters.regex("Add APPLE to Cart"), add_apple))
    dp.add_handler(MessageHandler(Filters.regex("Add HUAWEI to Cart"), add_HUAWEI))
    dp.add_handler(MessageHandler(Filters.regex("Clear Cart"), removeall1))
    dp.add_handler(MessageHandler(Filters.regex("1400"), code_1400))
    dp.add_handler(MessageHandler(Filters.regex("Saman"), code_saman))
    dp.add_handler(MessageHandler(Filters.regex("Bot"), code_bot))

    dp.add_handler(MessageHandler(Filters.regex("Shopping cart"), sabadd))
    dp.add_handler(MessageHandler(Filters.regex("Finalize Purchase"), finish))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
