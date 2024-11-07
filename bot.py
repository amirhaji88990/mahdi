import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# غیرفعال کردن پروکسی‌ها
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

# توکن ربات خود را وارد کنید
TOKEN = "7870121961:AAGExjTsLbhohXAY6efTNlfKuIlqo_1vL_Q"

# خوش آمد گویی به کاربر
async def start(update: Update, context: CallbackContext) -> None:
    # ارسال دو پیام به صورت جداگانه
    await update.message.reply_text("به ربات ما خوش آمدید!")
    await update.message.reply_text("لطفاً رمز مورد نظر خود را وارد کنید:")

# پردازش پیام‌ها و ارسال پاسخ بر اساس رمز
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    # رمز معتبر
    valid_password = "1"

    # اگر رمز صحیح باشد
    if user_input == valid_password:
        await update.message.reply_text("10.202.10.10")
    else:
        # اگر رمز اشتباه باشد
        await update.message.reply_text("پوزش می‌طلبم، همچین رمزی در سیستم ثبت نشده است.")

    # پس از ارسال پاسخ، دوباره به حالت اولیه باز می‌گردد
    await update.message.reply_text("در خدمت شما هستیم.")

# تعریف تابع اصلی برای راه اندازی ربات
async def main():
    # ایجاد شیء Application
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن دستور start
    application.add_handler(CommandHandler("start", start))

    # اضافه کردن پیام‌ها و پاسخ‌ها
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # راه‌اندازی ربات
    await application.run_polling()

# اجرای ربات
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



