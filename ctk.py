import customtkinter
import tkinterDnD
from AutoNPC import AutoNPC

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x600")
app.title("AutoNPC")
app.resizable(width=False, height=False)

f = open("apiKey.txt", "r", encoding="UTF-8")
apiKey = f.readline()
f.close()

def button_callback():
    if (entry_genre.get() == "") :
        return
    if (entry_ambient.get() == "") :
        return
    if (entry_era.get() == "") :
        return
    if (entry_job.get() == "") :
        return
    if (entry_brood.get() == "") :
        return
    if (entry_bias.get() == "") :
        return
    if (optionmenu_language.get() == "") :
        return
    autoNPC = AutoNPC(apiKey)
    autoNPC.run(entry_genre.get(), entry_ambient.get(), entry_era.get(), entry_job.get(), entry_brood.get(), entry_bias.get(), optionmenu_language.get())
    print(autoNPC.getNPC())

    new = customtkinter.CTkToplevel()
    new.title("AutoNPC")
    new.resizable(width=False, height=False)
    
    txt = str(autoNPC.getNPC())

    txt = txt.replace(",", "\n")
    
    """
    for x in autoNPC.getNPC().keys() :
        if (x == "name") :
            txt += "name : " + autoNPC.getNPC()[x]
        if (x == "story") :
            txt += "story : " + autoNPC.getNPC()[x]
        if (x == "name") :
            txt += "name : " + autoNPC.getNPC()[x]
        if (x == "name") :
            txt += "name : " + autoNPC.getNPC()[x]
    """
    label = customtkinter.CTkLabel(new, text=txt)
    label.pack()

    if (checkbox_1.get() == 1) :
        autoNPC.saveToServer()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="AutoNPC", font=customtkinter.CTkFont(size=30))
label_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="--게임 NPC 생성기--", font=customtkinter.CTkFont(size=15))
label_2.pack(pady=10, padx=10)

entry_genre = customtkinter.CTkEntry(master=frame_1, placeholder_text="게임 장르")
entry_genre.pack(pady=10, padx=10)

entry_ambient = customtkinter.CTkEntry(master=frame_1, placeholder_text="게임 배경 분위기")
entry_ambient.pack(pady=10, padx=10)

entry_era = customtkinter.CTkEntry(master=frame_1, placeholder_text="게임 배경 시대")
entry_era.pack(pady=10, padx=10)

entry_job = customtkinter.CTkEntry(master=frame_1, placeholder_text="NPC 직업")
entry_job.pack(pady=10, padx=10)

entry_brood = customtkinter.CTkEntry(master=frame_1, placeholder_text="NPC 종족")
entry_brood.pack(pady=10, padx=10)

entry_bias = customtkinter.CTkEntry(master=frame_1, placeholder_text="NPC 성향")
entry_bias.pack(pady=10, padx=10)

optionmenu_language = customtkinter.CTkOptionMenu(frame_1, values=["한국어", "영어", "일본어"])
optionmenu_language.pack(pady=10, padx=10)
optionmenu_language.set("언어 선택")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="저장")
checkbox_1.pack(pady=10, padx=10)

button_gen = customtkinter.CTkButton(master=frame_1, command=button_callback, text="생성")
button_gen.pack(pady=10, padx=10)

app.mainloop()