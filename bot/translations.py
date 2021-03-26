# © @Kirodewal

class Messages:

    START_MSG = "**Hi there {}**.\n\n**I'm Updated Youtube Uploader Bot.You can use me to upload any telegram video to youtube once you authorise me.** \n\n**HOW TO USE ME:-**\n **Watch On YouTube:** [Click Here](https://youtu.be/dLCXse6HlaE)\n **Watch On Google Drive:** [Click Here](https://drive.google.com/file/d/12qp4VcvBOVwhMIx0O5CtO5VvUbCDeFKs/view). \n\n You can know more from /help.\n\n **Join @HXBots for More Bots...**"

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that youtube processes each and every video uploaded, and its AI is amazing that it flags the video for copyrights if it finds copywrited content as soon as its uploaded, and you will not be able to publish the video.\n\nRead through all the pages to know how I work.",

        "**                          Page 📄 2/5** \n\n **Lets learn how I work.**\n\n**Step 1:** __You authorise me to upload to your youtube channel.More about this in comming pages.__\n\n**Step 2:** __You forward any Telegram video to me.__\n\n**Step 3:** __You reply /upload to the forwarded video file.You can also specify some title in the upload command, but its optional though.Title will follow the /upload {your custom title}.If no title is given, filename will be used as title.__\n\n**Step 4:** __I remotely download the file and uploads to your Youtube channel.__\n\n**Step 5:** __I send you the Youtube link after upload.__",

        "**                          Page 📄 3/5** \n\n **Create your youtube channel**\n\nThere is no point in using me if you dont have a Youtube Channel.So go through the given steps to create one.\n\n**Step 1:** __Sign in to YouTube on a computer or using the mobile.__\n\n**Step 2:** __Try any action that requires a channel, such as uploading a video, posting a comment, or creating a playlist.__\n\n**Step 3:** __If you don't yet have a channel, you'll see a prompt to create a channel.__\n\n**Step 4:** __Check the details and confirm to create your new channel.__",

        "**                          Page 📄 4/5** \n\n **Verify your YouTube account**\n\nYoutube take spam and abuse very seriously. So you are asked to verify your Youtube account. Once you've verified your account, you will be able to upload videos longer than 15 minutes. If you haven't verified your account every video uploaded which are longer than 15 minutes will be removed.\n[Verify your Youtube account here.](http://www.youtube.com/verify)\n\n__Remember to verify your project, else your uploads will be kept private.__",

        "**                          Page 📄 5/5** \n\n **Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that open the given link and allow access and copy the code. Come back here and type /authorise copied-code (eg: 4/4Ewa...) and send it.\n\n**Fear not!**\nI'm not a hacker or someone who wants to creep into people's privacy. I respect one's privacy. I'm here just to help anyone who wants help. If I was a hacker I won't be sitting here writing Telegram Bots.\n\n If you have any problem you can ask for support at [My Support Group](https://t.me/HxSupport)"
    ]

    NOT_A_REPLY_MSG = "**Please reply to some video file.**"

    NOT_A_MEDIA_MSG = "**No media file found.** "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "**This is not a valid media**"
    
    DAILY_QOUTA_REACHED = "**Looks like you are trying to upload more than 6 videos today! By default youtube only allows about 6 uploads daily, so this request might fail!!**"

    PROCESSING = "Processing....."

    NOT_AUTHENTICATED_MSG = "You have not authenticated me to upload video to any account. see /help Page📄 5/5 carefully to authenticate"

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code. **Read /help Page📄 5/5 Msg carefully**"

    AUTH_SUCCESS_MSG = "Congrats, you have successfully authenticated me to upload to Youtube.\nHappy uploading!"

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}"
    
    AUTH_DATA_SAVE_SUCCESS = "**Successfully saved the given auth data!**"
    
