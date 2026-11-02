# import smtplib
# import mimetypes
# from email.message import EmailMessage
# from email.utils import make_msgid


# # ---------------------------------------------------------
# # Function Name : Marvellous_Send_mail
# # Description   : Send HTML Email with Image Signature
# # ---------------------------------------------------------
# def Marvellous_Send_mail(sender, app_password, receiver, subject):

#     try:
#         # Create Email Object
#         msg = EmailMessage()

#         msg["From"] = sender
#         msg["To"] = receiver
#         msg["Subject"] = subject

#         # Plain Text (Fallback)
#         msg.set_content(
#             ""
#         )

#         # Create Image Content ID
#         image_cid = make_msgid()[1:-1]




#         html = f"""
# <html>
# <body style="font-family:Arial,Helvetica,sans-serif;">

# <p>Jay Ganesh,</p>

# <p>Hello Piyush Sir,</p>

# <p>
# As discussed after today’s Python lecture, I’m sending you this email regarding the Python resume format. You had asked me to send you an email, and you would share the format with me.
# </p>

# <p> Please share the <b>Python + Machine Learning resume format</b> when convenient.
#  </p>

# <p>
# Thank you, Sir.
# </p>

# <br>

# <table cellpadding="0" cellspacing="0">
#     <tr>

#         <td style="padding-right:15px;">
#             <img src="cid:{image_cid}" width="120">
#         </td>

#         <td style="border-left:3px solid #2E75B6;padding-left:15px;">

#             <h2 style="margin:0;color:#2E75B6;">
#                 Omkar Nanaso Suryawanshi
#             </h2>

#             <p style="margin:8px 0;">
#                 <b>Profession :</b> Software Developer
#             </p>

#             <p style="margin:5px 0;">
#                 <b style="color:#2E75B6;">P :</b>
#                 8767579124
#             </p>

#             <p style="margin:5px 0;">
#                 <b style="color:#2E75B6;">E :</b>
#                 omkar.suryawanshistc@gmail.com
#             </p>

#             <p style="margin:5px 0;">
#                 <b style="color:#2E75B6;">A :</b>
#                 At Post Charegaon,<br>
#                 Tal - Karad,<br>
#                 Dist - Satara
#             </p>

#         </td>

#     </tr>
# </table>

# <br><br>

# <b>Regards,</b><br>
# <b>Omkar Suryawanshi</b>

# </body>
# </html>
# """
#         msg.add_alternative(html, subtype="html")

#         # Image Path
#         image_path = "omkar.png"

#         # Attach Image
#         with open(image_path, "rb") as img:

#             mime_type, _ = mimetypes.guess_type(image_path)

#             if mime_type is None:
#                 maintype = "image"
#                 subtype = "png"
#             else:
#                 maintype, subtype = mime_type.split("/")

#             msg.get_payload()[1].add_related(
#                 img.read(),
#                 maintype=maintype,
#                 subtype=subtype,
#                 cid=f"<{image_cid}>"
#             )

#         print("Connecting to Gmail Server...")

#         smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

#         print("Login Successful...")

#         smtp.login(sender, app_password)

#         print("Sending Mail...")

#         smtp.send_message(msg)

#         smtp.quit()

#         print("\nMail Sent Successfully.")

#     except FileNotFoundError:
#         print("Image file 'omkar.png' not found.")

#     except smtplib.SMTPAuthenticationError:
#         print("Authentication Failed.")
#         print("Check your Gmail ID or App Password.")

#     except Exception as e:
#         print("Error :", e)


# # ---------------------------------------------------------
# # Main Function
# # ---------------------------------------------------------
# def main():

#     sender_email = "omkarflutter@gmail.com"

#     # Use App Password WITHOUT SPACES
#     app_password = "wnks ottl sldq gsot"

#     #receiver_email = "chavanshubham936@gmail.com"
#     #receiver_email = "dattabagal7507@gmail.com"
#     #receiver_email = "omkar.suryawanshistc@gmail.com"
#     receiver_email = "marvellousinfosystem@gmail.com"


#     subject = "Request for Python Batch Resume Format Sharing"

#     Marvellous_Send_mail(
#         sender_email,
#         app_password,
#         receiver_email,
#         subject
#     )


# # ---------------------------------------------------------
# # Entry Point
# # ---------------------------------------------------------
# if __name__ == "__main__":
#     main()


# ////////////////////////            ///////////////////////////
 #                 Marvellous_Send_mail
# Description   : Send HTML Email with Image Signature
#                 and TXT Report Attachment
#/////////////////////////                     /////////////////////

# import smtplib
# import mimetypes

# from email.message import EmailMessage
# from email.utils import make_msgid


# # ---------------------------------------------------------
# # Function Name : Marvellous_Send_mail
# # Description   : Send HTML Email with Image Signature
# #                 and TXT Report Attachment
# # ---------------------------------------------------------

# def Marvellous_Send_mail(
#     sender,
#     app_password,
#     receiver,
#     subject
# ):

#     try:

#         # -------------------------------------------------
#         # Create Email Object
#         # -------------------------------------------------

#         msg = EmailMessage()

#         msg["From"] = sender
#         msg["To"] = receiver
#         msg["Subject"] = subject

#         # -------------------------------------------------
#         # Plain Text Fallback
#         # -------------------------------------------------

#         msg.set_content(
#             """
# Hello Sir,

# Please find the attached Fraudulent Transaction Detection
# Machine Learning report.

# Thank you.

# Regards,
# Omkar Suryawanshi
# """
#         )

#         # -------------------------------------------------
#         # Create Image Content ID
#         # -------------------------------------------------

#         image_cid = make_msgid()[1:-1]

#         # -------------------------------------------------
#         # HTML Body
#         # -------------------------------------------------

#         html = f"""
# <html>

# <body style="font-family:Arial,Helvetica,sans-serif;">

# <p>Jay Ganesh,</p>

# <p>Hello Sir,</p>

# <p>
# Please find attached my <b>Fraudulent Transaction Detection</b>
# Machine Learning report.
# </p>

# <p>
# The report contains the performance comparison of:
# </p>

# <ul>
#     <li>Decision Tree Classifier</li>
#     <li>AdaBoost Classifier</li>
#     <li>Bagging Classifier</li>
#     <li>Random Forest Classifier</li>
#     <li>Voting Classifier - Soft</li>
#     <li>Voting Classifier - Hard</li>
# </ul>

# <p>
# Based on the F1 Score, the
# <b>Random Forest Classifier</b>
# achieved the best performance on the test dataset.
# </p>

# <p>
# Please check the attached report for complete results.
# </p>

# <p>
# Thank you, Sir.
# </p>

# <br>

# <table cellpadding="0" cellspacing="0">

#     <tr>

#         <td style="padding-right:15px;">

#             <img
#                 src="cid:{image_cid}"
#                 width="120"
#             >

#         </td>

#         <td
#             style="
#                 border-left:3px solid #2E75B6;
#                 padding-left:15px;
#             "
#         >

#             <h2 style="margin:0;color:#2E75B6;">

#                 Omkar Nanaso Suryawanshi

#             </h2>

#             <p style="margin:8px 0;">

#                 <b>Profession :</b>
#                 Software Developer

#             </p>

#             <p style="margin:5px 0;">

#                 <b style="color:#2E75B6;">
#                     P :
#                 </b>

#                 8767579124

#             </p>

#             <p style="margin:5px 0;">

#                 <b style="color:#2E75B6;">
#                     E :
#                 </b>

#                 omkar.suryawanshistc@gmail.com

#             </p>

#             <p style="margin:5px 0;">

#                 <b style="color:#2E75B6;">
#                     A :
#                 </b>

#                 At Post Charegaon,<br>
#                 Tal - Karad,<br>
#                 Dist - Satara

#             </p>

#         </td>

#     </tr>

# </table>

# <br><br>

# <b>Regards,</b><br>

# <b>Omkar Suryawanshi</b>

# </body>
# </html>
# """

#         msg.add_alternative(
#             html,
#             subtype="html"
#         )


#         # -------------------------------------------------
#         # Attach Signature Image
#         # -------------------------------------------------

#         image_path = "omkar.png"

#         with open(image_path, "rb") as img:

#             mime_type, _ = mimetypes.guess_type(
#                 image_path
#             )

#             if mime_type is None:

#                 maintype = "image"
#                 subtype = "png"

#             else:

#                 maintype, subtype = mime_type.split("/")


#             msg.get_payload()[1].add_related(
#                 img.read(),
#                 maintype=maintype,
#                 subtype=subtype,
#                 cid=f"<{image_cid}>"
#             )


#         # -------------------------------------------------
#         # Attach Generated TXT Report
#         # -------------------------------------------------

#         report_path = "Fraudulent_Transaction_Report.txt"

#         with open(report_path, "rb") as report:

#             report_data = report.read()

#             msg.add_attachment(
#                 report_data,
#                 maintype="text",
#                 subtype="plain",
#                 filename="Fraudulent_Transaction_Report.txt"
#             )


#         # -------------------------------------------------
#         # Connect Gmail Server
#         # -------------------------------------------------

#         print("Connecting to Gmail Server...")

#         smtp = smtplib.SMTP_SSL(
#             "smtp.gmail.com",
#             465
#         )


#         # -------------------------------------------------
#         # Login
#         # -------------------------------------------------

#         print("Login Successful...")

#         smtp.login(
#             sender,
#             app_password
#         )


#         # -------------------------------------------------
#         # Send Mail
#         # -------------------------------------------------

#         print("Sending Mail...")

#         smtp.send_message(msg)

#         smtp.quit()

#         print("\nMail Sent Successfully.")


#     except FileNotFoundError as e:

#         print("File not found :", e)

#     except smtplib.SMTPAuthenticationError:

#         print("Authentication Failed.")

#         print(
#             "Check your Gmail ID or App Password."
#         )

#     except Exception as e:

#         print("Error :", e)


# # ---------------------------------------------------------
# # Main Function
# # ---------------------------------------------------------

# def main():

#     sender_email = "omkarflutter@gmail.com"

# #     # Use App Password WITHOUT SPACES
#     app_password = "wnks ottl sldq gsot"

# #     #receiver_email = "chavanshubham936@gmail.com"
# #     #receiver_email = "dattabagal7507@gmail.com"
#     receiver_email = "omkar.suryawanshistc@gmail.com"
# #     receiver_email = "marvellousinfosystem@gmail.com"
#     subject = (
#         "Home Work Assignment 56 - "
#         "Fraudulent Transaction Detection"
#     )


#     Marvellous_Send_mail(
#         sender_email,
#         app_password,
#         receiver_email,
#         subject
#     )


# # ---------------------------------------------------------
# # Entry Point / Starter
# # ---------------------------------------------------------

# if __name__ == "__main__":
#     main()

import smtplib
import mimetypes

from email.message import EmailMessage
from email.utils import make_msgid


# ---------------------------------------------------------
# Function Name : Marvellous_Send_mail
# Description   : Send HTML Email with Image Signature
#                 and Two TXT Report Attachments
# ---------------------------------------------------------

def Marvellous_Send_mail(
    sender,
    app_password,
    receiver,
    subject
):

    try:

        # -------------------------------------------------
        # Step 1 : Create Email Object
        # -------------------------------------------------

        msg = EmailMessage()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject


        # -------------------------------------------------
        # Step 2 : Plain Text Fallback
        # -------------------------------------------------

        msg.set_content(
            """
Hello Sir,

Please find attached the reports for Home Work Assignment 55
and Home Work Assignment 56.

Thank you.

Regards,
Omkar Suryawanshi
"""
        )


        # -------------------------------------------------
        # Step 3 : Create Image Content ID
        # -------------------------------------------------

        image_cid = make_msgid()[1:-1]


        # -------------------------------------------------
        # Step 4 : HTML Body
        # -------------------------------------------------

        html = f"""
<html>

<body style="font-family:Arial,Helvetica,sans-serif;">

<p>Jay Ganesh,</p>

<p>Hello Sir,</p>

<p>
Please find attached my completed reports for
<b>Home Work Assignment 55</b> and
<b>Home Work Assignment 56</b>.
</p>

<p>
<b>Home Work Assignment 55:</b>
Customer Loan Approval using Machine Learning
</p>

<p>
<b>Home Work Assignment 56:</b>
Fraudulent Transaction Detection using Machine Learning
</p>

<p>
The attached reports contain the model evaluation results
and comparison tables.
</p>

<p>
Please check the attached files for the complete output.
</p>

<p>
Thank you, Sir.
</p>

<br>

<table cellpadding="0" cellspacing="0">

    <tr>

        <td style="padding-right:15px;">

            <img
                src="cid:{image_cid}"
                width="120"
            >

        </td>

        <td
            style="
                border-left:3px solid #2E75B6;
                padding-left:15px;
            "
        >

            <h2 style="margin:0;color:#2E75B6;">

                Omkar Nanaso Suryawanshi

            </h2>

            <p style="margin:8px 0;">

                <b>Profession :</b>
                Software Developer

            </p>

            <p style="margin:5px 0;">

                <b style="color:#2E75B6;">
                    P :
                </b>

                8767579124

            </p>

            <p style="margin:5px 0;">

                <b style="color:#2E75B6;">
                    E :
                </b>

                omkar.suryawanshistc@gmail.com

            </p>

            <p style="margin:5px 0;">

                <b style="color:#2E75B6;">
                    A :
                </b>

                At Post Charegaon,<br>
                Tal - Karad,<br>
                Dist - Satara

            </p>

        </td>

    </tr>

</table>

<br><br>

<b>Regards,</b><br>

<b>Omkar Suryawanshi</b>

</body>

</html>
"""


        msg.add_alternative(
            html,
            subtype="html"
        )


        # -------------------------------------------------
        # Step 5 : Attach Signature Image
        # -------------------------------------------------

        image_path = "omkar.png"

        with open(image_path, "rb") as img:

            mime_type, _ = mimetypes.guess_type(
                image_path
            )

            if mime_type is None:

                maintype = "image"
                subtype = "png"

            else:

                maintype, subtype = mime_type.split("/")


            msg.get_payload()[1].add_related(
                img.read(),
                maintype=maintype,
                subtype=subtype,
                cid=f"<{image_cid}>"
            )


        # -------------------------------------------------
        # Step 6 : Attach Assignment 56 Report
        # -------------------------------------------------

        report_56 = "Fraudulent_Transaction_Report.txt"

        with open(report_56, "rb") as file:

            report_56_data = file.read()

            msg.add_attachment(
                report_56_data,
                maintype="text",
                subtype="plain",
                filename="Fraudulent_Transaction_Report.txt"
            )


        # -------------------------------------------------
        # Step 7 : Attach Assignment 55 Report
        # -------------------------------------------------

        report_55 = "Customer_Loan_Approval_Report.txt"

        with open(report_55, "rb") as file:

            report_55_data = file.read()

            msg.add_attachment(
                report_55_data,
                maintype="text",
                subtype="plain",
                filename="Customer_Loan_Approval_Report.txt"
            )


        # -------------------------------------------------
        # Step 8 : Connect Gmail Server
        # -------------------------------------------------

        print("Connecting to Gmail Server...")

        smtp = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        )


        # -------------------------------------------------
        # Step 9 : Login
        # -------------------------------------------------

        print("Login to Gmail Server...")

        smtp.login(
            sender,
            app_password
        )

        print("Login Successful...")


        # -------------------------------------------------
        # Step 10 : Send Mail
        # -------------------------------------------------

        print("Sending Mail...")

        smtp.send_message(msg)

        smtp.quit()


        # -------------------------------------------------
        # Step 11 : Success Message
        # -------------------------------------------------

        print("\nMail Sent Successfully.")

        print(
            "Attachment 1 : "
            "Fraudulent_Transaction_Report.txt"
        )

        print(
            "Attachment 2 : "
            "Customer_Loan_Approval_Report.txt"
        )


    # -----------------------------------------------------
    # Exception Handling
    # -----------------------------------------------------

    except FileNotFoundError as e:

        print("\nFile Not Found :")
        print(e)

        print(
            "\nPlease make sure that "
            "omkar.png and both TXT files "
            "are present in the same folder."
        )


    except smtplib.SMTPAuthenticationError:

        print("\nAuthentication Failed.")

        print(
            "Please check your Gmail ID "
            "and App Password."
        )


    except Exception as e:

        print("\nError :")
        print(e)


# =========================================================
# Main Function
# =========================================================

def main():

        sender_email = "omkarflutter@gmail.com"

# #     # Use App Password WITHOUT SPACES
        app_password = "wnks ottl sldq gsot"

# #     #receiver_email = "chavanshubham936@gmail.com"
# #     #receiver_email = "dattabagal7507@gmail.com"
        #receiver_email = "omkar.suryawanshistc@gmail.com"
        receiver_email = "marvellousinfosystem@gmail.com"



    # -----------------------------------------------------
    # Email Subject
    # -----------------------------------------------------

        subject = (
        "Home Work Assignment 55 & 56 - "
        "Machine Learning Reports"
    )


    # -----------------------------------------------------
    # Call Send Mail Function
    # -----------------------------------------------------

        Marvellous_Send_mail(
        sender_email,
        app_password,
        receiver_email,
        subject
    )


# =========================================================
# Starter / Entry Point
# =========================================================

if __name__ == "__main__":
    main()