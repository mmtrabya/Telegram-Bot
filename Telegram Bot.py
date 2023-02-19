import telebot
import logging

bot = telebot.TeleBot("")
bot.set_webhook()
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"""this bot is made by Mariam Alkassaby and Mohamed Tarabay
students in AIE program faculty of engineering mansoura university, to know more about our program press here /Artificial and to start /press here""")
logger = telebot.logger
logging.basicConfig(filename='TeleLog.log', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
@bot.message_handler(commands=["press"])
def reply(message):
    bot.send_message(message.chat.id,"""/students affairs
/credit hours (البرامج النوعيه)""")

@bot.message_handler(commands=["students"])
def students (message):
    bot.send_message(message.chat.id,"""/1-التحويل بعد اعدادي
/2-التقديم للكليه
/3-المنح الخاصه بالبرامج النوعيه
/4-مواعيد عمل شئون الطلبه
/5-الكشف الطبي
/6-سداد الرسوم الدراسيه""")

@bot.message_handler(commands=["1","2","3","4","5","6"])
def STUDENTS(message):
    if message.text == "/1":
            bot.send_message(message.chat.id,u""" من داخل الكلية
بيان حالة بالدرجات و التقديرات و مختوم من الكلية اصل + صورة
عدد ٢ استمارة ثانوية عامة او ما يعادلها
عدد ٢ صورة من بطاقة الرقم القومي للطالب
صورة من بطاقة الرقم القومي للوالد
صورة من شهادة الميلاد للطالب\nمن خارج الكلية
بيان حالة بالدرجات و التقديرات و مختوم من الكلية المقيد بها الطالب اصل + صورة
عدد ٢ استمارة ثانوية عامة او ما يعادلها
عدد ٢ صورة من بطاقة الرقم القومي للطالب
صورة من بطاقة الرقم القومي للوالد
صورة من شهادة الميلاد للطالب
محتوي علمي للمواد معتمدا و مختوم
نموذج ٢ جند للطلاب الذكور فقط مستوفيا البيانات الشخصية
اصل + صورة للبطاقة العسكرية (٦جند او ٧ جند) للطلاب الذكور فقط لمواليد عام ٢٠٠٤ او ما قبله
ايصال كهرباء او مياه او تليفون بإسم ولي الامر لم يمضي عليه ٣ شهور""")

    elif message.text == "/2":
            bot.send_message(message.chat.id,"""للثانوية العامة و ما يعادلها
عدد ٢ استمارة ثانوية عامة او ما يعادلها
عدد ٢ صورة من بطاقة الرقم القومي للطالب
صورة من بطاقة الرقم القومي للوالد
صورة من شهادة الميلاد للطالب
نموذج ٢ جند للطلاب الذكور فقط مستوفيا البيانات الشخصية
اصل + صورة للبطاقة العسكرية (٦جند او ٧ جند) للطلاب الذكور فقط لمواليد عام ٢٠٠٤ او ما قبله""")

    elif message.text == "/3":
            bot.send_photo(message.chat.id,open("scolarship.jpeg","rb"))

    elif message.text == "/4":
            bot.send_message(message.chat.id,"من 9 حتي 1")

    elif message.text == "/5":
            bot.send_message(message.chat.id,"""ازاي تحجز للكشف الطبي:
https://muhtwaplus.com/162722/2021/09/24/%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D8%A8%D9%86-%D8%B3%D9%8A%D9%86%D8%A7-%D8%AC%D8%A7%D9%85%D8%B9%D8%A9-%D8%A7%D9%84%D9%85%D9%86%D8%B5%D9%88%D8%B1%D8%A9-%D8%A7%D9%84%D9%83%D8%B4%D9%81-%D8%A7%D9%84%D8%B7%D8%A8%D9%8A-%D9%84%D9%84%D8%B7%D9%84%D8%A7%D8%A8-%D8%A7%D9%84%D8%AC%D8%AF%D8%AF/
لينك الحجز :
http://sce.mans.edu.eg/mus/studentPortal/""")

    elif message.text == "/6":
            bot.send_photo(message.chat.id,open("money.jpeg","rb"))


@bot.message_handler(commands=["credit"])
def programs (message):
  bot.send_message(message.chat.id,text="""/Artificial Intelligence Engineering (AIE)\n
/Building and Construction Engineering (BCE)\n
/Biomedical Engineering (BME)\n
/Communications and Computer Engineering (CCE)\n
/chemical and enviromental engineering (CEE)\n
/Civil and Environmental Engineering-Sustainable Water Engineering (CEE_SWE)\n
/Infrastructure and Environmental Engineering (IEE)\n
/Mechatronics Engineering (MTE)\n
/materials engineering for advanced technology (MET)\n
/Renewable and Sustainable energy Engineering (RSE)\n
/Sustainable Architecture Engineering (SAE)\n
/Structural Engineering (STE)\n""")



@bot.message_handler(commands=["Artificial"])
def AIE_program(message):
   bot.send_message(message.chat.id,"""/AIE_brochure (program guide)
/AIE_the intro video of the program
/AIE_group link
/AIE_program page
/AIE_courses map
/AIE_Price per credit hour""")
@bot.message_handler(commands=["AIE_brochure","AIE_the","AIE_group","AIE_program","AIE_courses","AIE_Price"])
def AIE (message):
    if message.text == "/AIE_brochure":
        bot.send_message(message.chat.id,"https://drive.google.com/file/d/1SLdlM_0gfcJpib0SEOTLTLiKT_dduT1D/view?usp=sharing")
    elif message.text == "/AIE_the":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=aPTnaP6OA14")
    elif message.text == "/AIE_group":
        bot.send_message(message.chat.id,"https://www.facebook.com/groups/aiefemu/")
    elif message.text == "/AIE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/AIE-Faculty-of-Engineering-MU-102651682175732")
    elif message.text == "/AIE_courses":
        bot.send_photo(message.chat.id,open("aie couses.jpg","rb"))
    elif message.text == "/AIE_Price":
        bot.send_message(message.chat.id,"1100 EP")



@bot.message_handler(commands=["Building"])
def BCE_program(message):
   bot.send_message(message.chat.id,"""/BCE_brochure (program guide)
/BCE_the intro video of the program
/BCE_program page
/BCE_courses map
/BCE_Price per credit hour""")
@bot.message_handler(commands=["BCE_brochure","BCE_the","BCE_program","BCE_courses","BCE_Price"])
def BCE (message):
    if message.text == "/BCE_brochure":
        bot.send_photo(message.chat.id,open("bce bro.jpeg","rb"))
    elif message.text == "/BCE_the":
        bot.send_message(message.chat.id,"https://youtu.be/nWnJc1qQ0kQ")
    #elif message.text == "/BCE_group":
        #bot.send_message(message.chat.id,"https://www.facebook.com/groups/aiefemu/?ref=share_group_link")
    elif message.text == "/BCE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/BCE.MansouraUnvirsty/")
    elif message.text == "/BCE_courses":
        bot.send_photo(message.chat.id,open("bce.jpeg","rb"))
    elif message.text == "/BCE_Price":
        bot.send_message(message.chat.id,"1100 EP")


@bot.message_handler(commands=["Biomedical"])
def BME_program(message):
   bot.send_message(message.chat.id,"""/BME_brochure (program guide)
/BME_the intro video of the program
/BME_group link
/BME_program page
/BME_courses map
/BME_Price per credit hour""")
@bot.message_handler(commands=["BME_brochure","BME_the","BME_group","BME_program","BME_courses","BME_Price"])
def BME (message):
    if message.text == "/BME_brochure":
        bot.send_message(message.chat.id,"http://engpro.mans.edu.eg/bme/news-ar/2302-2020-10-15-07-35-55")
    elif message.text == "/BME_the":
        bot.send_message(message.chat.id,"https://youtu.be/ci-OGC8cmg4")
    elif message.text == "/BME_group":
        bot.send_message(message.chat.id,"https://www.facebook.com/groups/BMEOfficial/?ref=share_group_link")
    elif message.text == "/BME_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/bme.mansourauniversity")
    elif message.text == "/BME_courses":
        bot.send_photo(message.chat.id,open("bme.jpeg","rb"))
    elif message.text == "/BME_Price":
        bot.send_message(message.chat.id,"1100 EP")


@bot.message_handler(commands=["Communications"])
def CCE_program(message):
   bot.send_message(message.chat.id,"""/CCE_brochure (program guide)
/CCE_the intro video of the program
/CCE_group link
/CCE_courses map
/CCE_Price per credit hour""")
@bot.message_handler(commands=["CCE_brochure","CCE_the","CCE_group","CCE_program","CCE_courses","CCE_Price"])
def CCE (message):
    if message.text == "/CCE_brochure":
        bot.send_message(message.chat.id,"http://engfac.mans.edu.eg/images/files/engpdf/main-n/regulations-a.pdf")
    elif message.text == "/CCE_the":
        bot.send_message(message.chat.id,"https://youtu.be/rEzrMIcXrU4")
    elif message.text == "/CCE_group":
        bot.send_message(message.chat.id,"https://www.facebook.com/groups/1413763278865103/?ref=sharehttps://www.facebook.com/groups/1413763278865103/?ref=share&exp=93fa")
    elif message.text == "/CCE_courses":
        bot.send_photo(message.chat.id,open("cce.jpeg","rb"))
    elif message.text == "/CCE_Price":
        bot.send_message(message.chat.id,"1100 EP")

@bot.message_handler(commands=["chemical"])
def CEE(message):
    bot.send_message(message.chat.id,"""/CEE_brochure (program guide)
/CEE_the intro video of the program
/CEE_courses map
/CEE_Price per credit hour""")
@bot.message_handler(commands=["CEE_brochure","CEE_the","CEE_courses","CEE_Price"])
def cee (message):
    if message.text == "/CEE_brochure":
        bot.send_photo(message.chat.id,open("chemical.jpeg","rb"))
    elif message.text == "/CEE_the":
        bot.send_message(message.chat.id,"https://fb.watch/fjqvKqnTkS/")
    #elif message.text == "/CEE_program":
        #bot.send_message(message.chat.id,"")
    elif message.text == "/CEE_courses":
        bot.send_message(message.chat.id,"https://engfac.mans.edu.eg/images/files/engpdf/new-programs/chemical/daleel-chem.pdf")
    elif message.text == "/CEE_Price":
        bot.send_message(message.chat.id,"600 EP")



@bot.message_handler(commands=["Civil"])
def CEE_SWE_program(message):
   bot.send_message(message.chat.id,"""/CEE_SWE_brochure (program guide)
/CEE_SWE_the intro video of the program
/CEE_SWE_program page
/CEE_SWE_courses map
/CEE_SWE_Price per credit hour""")
@bot.message_handler(commands=["CEE_SWE_brochure","CEE_SWE_the","CEE_SWE_group","CEE_SWE_program","CEE_SWE_courses","CEE_SWE_Price"])
def SWE (message):
    if message.text == "/CEE_SWE_brochure":
        bot.send_message(message.chat.id,"https://drive.google.com/file/d/1EVT7zPpue0mUUM7A6HCRLVIDh7kq1CzK/view?usp=sharing")
    elif message.text == "/CEE_SWE_the":
        bot.send_message(message.chat.id,"https://drive.google.com/file/d/1lJXt-IcewPjUcKuqhd64_M2BXnfsnf82/view?usp=sharing")
    elif message.text == "/CEE_SWE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/Civil-Environmental-Engineering-Sustainable-Water-Engineering-Program-233193351954020/")
    elif message.text == "/CEE_SWE_courses":
        bot.send_photo(message.chat.id,open("SWE cor.jpeg","rb"))
    elif message.text == "/CEE_SWE_Price":
        bot.send_message(message.chat.id,"600 EP")





@bot.message_handler(commands=["Infrastructure"])
def IEE_program(message):
   bot.send_message(message.chat.id,"""/IEE_brochure (program guide)
/IEE_the intro video of the program
/IEE_program page
/IEE_courses map
/IEE_Price per credit hour""")
@bot.message_handler(commands=["IEE_brochure","IEE_the","IEE_program","IEE_courses","IEE_Price"])
def IEE (message):
    if message.text == "/IEE_brochure":
        bot.send_message(message.chat.id,"https://engfac.mans.edu.eg/images/files/engpdf/new-programs/Infrastructure/daleel-e-iee.pdf")
    elif message.text == "/IEE_the":
        bot.send_message(message.chat.id,"https://www.facebook.com/106844782122771/posts/114281884712394/?flite=scwspnss")
    #elif message.text == "/IEE_group":
        #bot.send_message(message.chat.id,"https://www.facebook.com/groups/aiefemu/?ref=share_group_link")
    elif message.text == "/IEE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC-%D9%87%D9%86%D8%AF%D8%B3%D8%A9-%D8%A7%D9%84%D8%A8%D9%86%D9%8A%D8%A9-%D8%A7%D9%84%D8%AA%D8%AD%D8%AA%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A8%D9%8A%D8%A6%D9%8A%D8%A9-106844782122771/")
    elif message.text == "/IEE_courses":
        bot.send_photo(message.chat.id,open("iee.jpeg","rb"))
    elif message.text == "/IEE_Price":
        bot.send_message(message.chat.id,"600 EP")



@bot.message_handler(commands=["Mechatronics"])
def MTE_program(message):
   bot.send_message(message.chat.id,"""/MTE_brochure (program guide)
/MTE_the intro video of the program
/MTE_group link
/MTE_courses map
/MTE_Price per credit hour""")
@bot.message_handler(commands=["MTE_brochure","MTE_the","MTE_group","MTE_courses","MTE_Price"])
def MTE (message):
    if message.text == "/MTE_brochure":
        bot.send_message(message.chat.id,"https://m.facebook.com/story.php?story_fbid=pfbid02YxX2qEWf6tyVTfpNLmXuGVQ759HBTNeQ2tLKW4TVXogB5kA5kM4MyakUGa9oxxxol&id=104498195704957")
    elif message.text == "/MTE_the":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=ef_T2b2cfxY&t=4s")
    elif message.text == "/MTE_group":
        bot.send_message(message.chat.id,"https://www.facebook.com/groups/mte.mu/")
    elif message.text == "/MTE_courses":
        bot.send_photo(message.chat.id,open("mte.jpeg","rb"))
    elif message.text == "/MTE_Price":
        bot.send_message(message.chat.id,"1100 EP")

@bot.message_handler(commands=["materials"])
def MET_program(message):
       bot.send_message(message.chat.id,"""/MET_brochure (program guide)
/MET_the intro video of the program
/MET_Price per credit hour""")
@bot.message_handler(commands=["MET_brochure","MET_the","MET_courses","MET_Price"])
def MET (message):
    if message.text == "/MET_brochure":
        bot.send_photo(message.chat.id,open("MET BROCHURE.jpeg","rb"))
    elif message.text == "/MET_the":
        bot.send_message(message.chat.id,"https://fb.watch/fjspvQ18Zt/")
    elif message.text == "/MET_Price":
        bot.send_message(message.chat.id,"600EP")

@bot.message_handler(commands=["Renewable"])
def RSE_program(message):
   bot.send_message(message.chat.id,"""/RSE_brochure (program guide)
/RSE_the intro video of the program
/RSE_program page
/RSE_Price per credit hour""")
@bot.message_handler(commands=["RSE_brochure","RSE_the","RSE_group","RSE_program","RSE_Price"])
def RSE (message):
    if message.text == "/RSE_brochure":
        bot.send_message(message.chat.id,"https://engfac.mans.edu.eg/images/files/energy/guide2021.pdf")
    elif message.text == "/RSE_the":
        bot.send_message(message.chat.id,"https://fb.watch/fcLPR7cDoz/")
    elif message.text == "/RSE_group":
       bot.send_message(message.chat.id,"https://www.facebook.com/groups/RSE.MU/")
    elif message.text == "/RSE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/profile.php?id=100072494407577")
    elif message.text == "/RSE_Price":
        bot.send_message(message.chat.id,"825 EP")





@bot.message_handler(commands=["Sustainable"])
def SAE_program(message):
   bot.send_message(message.chat.id,"""/SAE_brochure (program guide)
/SAE_the intro video of the program
/SAE_program page
/SAE_courses map
/SAE_Price per credit hour""")
@bot.message_handler(commands=["SAE_brochure","SAE_the","SAE_program","SAE_courses","SAE_Price"])
def SAE (message):
    if message.text == "/SAE_brochure":
        bot.send_photo(message.chat.id,open("sae bro.jpeg","rb"))
    elif message.text == "/SAE_the":
        bot.send_message(message.chat.id,"https://m.facebook.com/story.php?story_fbid=946820449514324&id=234250540449950")
    elif message.text == "/SAE_program":
        bot.send_message(message.chat.id,"https://m.facebook.com/Sustainable-Architecture-Programme-248286630422952/")
    elif message.text == "/SAE_courses":
        bot.send_photo(message.chat.id,open("sae co.jpeg","rb"))
    elif message.text == "/SAE_Price":
        bot.send_message(message.chat.id,"1100 EP")




@bot.message_handler(commands=["Structural"])
def STE_program(message):
   bot.send_message(message.chat.id,"""/STE_brochure (program guide)
/STE_the intro video of the program
/STE_group link
/STE_program page
/STE_courses map
/STE_Price per credit hour""")
@bot.message_handler(commands=["STE_brochure","STE_the","STE_program","STE_courses","STE_Price"])
def STE (message):
    if message.text == "/STE_brochure":
        bot.send_photo(message.chat.id,open("ste bro.jpeg","rb"))
    elif message.text == "/STE_the":
        bot.send_message(message.chat.id,"https://fb.watch/eTa63SjR9E/")
    elif message.text == "/STE_program":
        bot.send_message(message.chat.id,"https://www.facebook.com/STE.mans.eg/")
    elif message.text == "/STE_courses":
        bot.send_photo(message.chat.id,open("ste.jpeg","rb"))
    elif message.text == "/STE_Price":
        bot.send_message(message.chat.id,"750")



bot.polling()