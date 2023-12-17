from enum import EnumMeta
import json
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from export import *

from vocabulary import *
import tkinter as tk

language = "english"
fileh = ""
version = "2.1.0"

# ts = googletrans.Translator()
# lang_dict = {"Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az",
#              "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg",
#              "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny", "Chinese (Simplified)": "zh-cn", "Chinese (Traditional)": "zh-tw", "Corsican": "co", "Croatian": "hr", "Czech": "cs",
#              "Danish": "da", "Dutch": "nl",
#              "English": "en", "Esperanto": "eo", "Estonian": "et",
#              "Filipino": "tl", "Finnish": "fi", "French": "fr", "Frisian": "fy",
#              "Galician": "gl", "Georgian": "ka", "German": "de", "Greek": "el", "Gujarati": "gu",
#              "Haitian creole": "ht", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu",
#              "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it",
#              "Japanese": "ja", "Javanese": "jw", "Kannada": "kn",
#              "Kazakh": "kk", "Khmer": "km", "Korean": "ko", "Kurdish (Kurmanji)": "ku", "Kyrgyz": "ky",
#              "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb",
#              "Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my",
#              "Nepali": "ne", "Norwegian": "no",
#              "Odia": "or",
#              "Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa",
#              "Romanian": "ro", "Russian": "ru",
#              "Samoan": "sm", "Scots gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv",
#              "Tajik": "tg", "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr",
#              "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz",
#              "Vietnamese": "vi",
#              "Welsh": "cy",
#              "Xhosa": "xh",
#              "Yiddish": "yi", "Yoruba": "yo",
#              "Zulu": "zu"}

dest = "en"

# if language == "english":
#     translate = "translate"
# else:
#     translate = "번역"


def command_for_see():
    if language == "english":
        see_win_title_text = "See word"
        see_win_ascending_text = "Ascending"
        see_win_file_add_text = "Please add a file."
        see_win_file_select_text = "Please select a file."
        see_win_warning_text = "Warning"
        see_win_file_text = "Export file"
    else:
        see_win_title_text = "단어 보기"
        see_win_ascending_text = "정렬"
        see_win_file_add_text = "파일을 추가해주세요."
        see_win_file_select_text = "파일을 선택해주세요"
        see_win_warning_text = "경고"
        see_win_file_text = "내보내기"
    see_win = Tk()
    see_frame = Frame(see_win)
    see_win.iconbitmap(r'icon.ico')
    see_canvas = Canvas(see_frame)
    see_scroll_bar = ttk.Scrollbar(
        see_frame, orient=VERTICAL, command=see_canvas.yview)
    see_canvas.configure(yscrollcommand=see_scroll_bar.set)
    see_canvas.bind('<Configure>', lambda e: see_canvas.configure(
        scrollregion=see_canvas.bbox("all")))
    second_see_frame = Frame(see_canvas)
    see_canvas.create_window((0, 0), window=second_see_frame, anchor="nw")
    see_width = int(see_win.winfo_screenwidth() * 0.0104166666666667)
    see_height = int(see_win.winfo_screenheight() * 0.0046296296296296)
    see_win.option_add("*Font", "Helvetica 20")
    see_frame.pack(fill=BOTH, expand=1)
    see_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    see_scroll_bar.pack(side=RIGHT, fill=Y)
    see_win.resizable(0, 0)
    see_win.title(see_win_title_text)
    see_win.geometry(
        f"{int(see_win.winfo_screenwidth() * (1 / 3))}x{int(see_win.winfo_screenheight() * 0.7)}")

    sortvalue = BooleanVar()
    sortvalue.set(True)
    label_list = list()

    def show(is_sort):
        cvoca = Vocabulary(language)
        if is_sort:
            sort_voca = sorted(cvoca.voca['jvocabulary'].items(),
                               key=lambda x: x[0].lower())  # sort voca 안 쓰고 트롤하지말고 다음에 아래에 꼭 쓸 것
            for label in label_list:
                label.destroy()
            for i, (word, mean) in enumerate(sort_voca):
                word = Label(second_see_frame, text=word,
                             width=see_width, height=see_height)
                mean = Label(second_see_frame, text=mean,
                             width=see_width, height=see_height)
                label_list.append(word)
                label_list.append(mean)
                word.grid(row=i, column=0)
                mean.grid(row=i, column=1)
        else:
            for label in label_list:
                label.destroy()
            for i, (word, mean) in enumerate(cvoca.voca['jvocabulary'].items()):
                word = Label(second_see_frame, text=word,
                             width=see_width, height=see_height)
                mean = Label(second_see_frame, text=mean,
                             width=see_width, height=see_height)
                label_list.append(word)
                label_list.append(mean)
                word.grid(row=i, column=0)
                mean.grid(row=i, column=1)

    show(True)

    def toggle():
        if sortvalue.get() == True:
            show(True)
            sortvalue.set(False)
        else:
            show(False)
            sortvalue.set(True)

    checkVar = IntVar()
    ascending = Checkbutton(see_win, text=see_win_ascending_text,
                            variable=checkVar, command=toggle)

    def file_press():
        fileh = filedialog.askopenfilename(initialdir="/",
                                           title=see_win_file_select_text,
                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if fileh == '':
            messagebox.showwarning(see_win_warning_text, see_win_file_add_text)

        export(fileh)
    file = Button(see_win, text=see_win_file_text, command=file_press)
    ascending.select()
    ascending.pack()
    file.pack()
    see_win.mainloop()


def command_for_modify():
    cvoca = Vocabulary(language)
    if language == "english":
        modify_win_title = "Modify Word"
    else:
        modify_win_title = "단어 수정"

    def modify_win_quit():
        modify_win.destroy()

    modify_win = Tk()
    modify_win.title(modify_win_title)
    modify_win.iconbitmap(r'icon.ico')

    modify_list = list()
    for i, (word, mean) in enumerate(cvoca.voca['jvocabulary'].items()):
        modify_list.append(word + ' ▬ ' + mean)
    modify_win.geometry(
        f"{int(modify_win.winfo_screenwidth() * (2.5 / 3))}x{int(modify_win.winfo_screenheight() * 0.8)}")
    modify_combo = ttk.Combobox(
        modify_win, values=modify_list, width=86, height=5, font="Helvetica 25 bold")

    def callbackFunc(event):
        global modify_combo_get
        modify_combo_get = modify_combo.get()
        modify_combo_get = modify_combo_get.split(' ▬ ')
        word_entry.delete(0, "end")
        mean_entry.delete(0, "end")
        word_entry.insert(0, modify_combo_get[0])
        mean_entry.insert(0, modify_combo_get[1])

    modify_combo.bind("<<ComboboxSelected>>", callbackFunc)

    def command_for_modify_add_btn():
        word, _ = modify_combo_get
        cvoca.delete(word)
        _word = word_entry.get()
        _mean = mean_entry.get()
        cvoca.add(_word, _mean)
        success_label = Label(modify_win,
                              text="\"{}\" {} \"{}\" {}".format(_word, modify_win_and, _mean,
                                                                modify_win_success_text),
                              font="Helvetica 25 bold")
        success_label.place(relx=0.01, rely=0.945)

    if language == "english":
        modify_win_modify_btn_text = "Modify"
        modify_win_success_text = "have successfully been modified"
        modify_win_and = "and"
        # modify_win_trans_btn_text = "Translate"
    else:
        modify_win_modify_btn_text = "수정"
        modify_win_success_text = "단어가 성공적으로 수정되었습니다"
        modify_win_and = "와/과"
        # modify_win_trans_btn_text = "번역"
    if language == "english":
        modify_win_close_btn_text = "Quit"
    else:
        modify_win_close_btn_text = "종료"

    modify_win['bg'] = '#50BCDF'
    modify_win.option_add("*Font", "Helvetica 50")
    word_entry = Entry(modify_win, font="Helvetica 50 bold")
    mean_entry = Entry(modify_win, font="Helvetica 50 bold")
    modify_btn = Button(modify_win, command=command_for_modify_add_btn, text=modify_win_modify_btn_text,
                        font="Helvetica 50 bold")
    cancel_btn = Button(modify_win, command=modify_win_quit, text=modify_win_close_btn_text,
                        font="Helvetica 50 bold")
    word_entry.place(relx=0.01, rely=0.02, relwidth=0.485, relheight=0.47)
    mean_entry.place(relx=0.505, rely=0.02, relwidth=0.485, relheight=0.47)
    modify_btn.place(relx=0.01, rely=0.51, relwidth=0.485, relheight=0.43)
    cancel_btn.place(relx=0.505, rely=0.51, relwidth=0.485, relheight=0.43)
    modify_combo.place(relx=0.01, rely=0.945, relwidth=0.98, relheight=0.05)

    # def translate():
    #     WEG = word_entry.get()
    #     result1 = ts.translate(WEG, dest=dest)
    #     mean_entry.insert(0, result1.text)

    # if ts_btn_select == True:
    #     translate_btn = Button(modify_win, command=translate, text=modify_win_trans_btn_text,
    #                            font="Helvetica 20 bold")
    #     translate_btn.place(relx=0.01, rely=0.01,
    #                         relwidth=0.98, relheight=0.03)
    modify_win.mainloop()


def click_english_btn():
    global language
    language = "english"
    win.destroy()
    main()


def click_korean_btn():
    global language
    language = "korean"
    win.destroy()
    main()


global ts_combo


def command_for_setting():

    if language == "english":
        english_text = "English"
        korean_text = "Korean"
        # translate_text = "Translate Mode"
        dest_text = "Select"
        version_text = "Version"
    else:
        english_text = "영어"
        korean_text = "한국어"
        # translate_text = "번역 모드"
        dest_text = "선택하기"
        version_text = "버전"

    setting_win = Tk()
    setting_win.resizable(0, 0)
    # setting_win.iconbitmap(r'icon.ico')
    setting_win['bg'] = '#50BCDF'
    setting_win.title("Choose Language")
    setting_win.geometry(
        f"{int(setting_win.winfo_screenwidth() * (0.7 / 2))}x{int(setting_win.winfo_screenheight() * 0.4)}")
    english_btn = Button(setting_win, text=english_text,
                         command=click_english_btn, width=20, height=4, font="Helvetica 25 bold")
    e_lb = Label(setting_win, width=20, height=10, bg="#50BCDF")
    korean_btn = Button(setting_win, text=korean_text, command=click_korean_btn,
                        width=20, height=4, font="Helvetica 25 bold")
    k_lb = Label(setting_win, width=20, height=10, bg='#50BCDF')
    e_lb.grid(row=1, column=0)
    english_btn.grid(row=1, column=1)
    k_lb.grid(row=2, column=0)
    korean_btn.grid(row=2, column=1)
    version_tx = Label(setting_win, text=f"{version_text} : {version}")
    version_tx.grid(row=3, column=1)
    # global translate_button
    # global translate
    # ts_combo_list = list(lang_dict.keys())
    # translate = BooleanVar()
    # tsvalue = BooleanVar()
    # tsvalue.set(True)
    # CheckVar = IntVar()
    # ts_combo = ttk.Combobox(setting_win, values=ts_combo_list,
    #                         width=20, height=2, font="Helvetica 25 bold")

    # def command_for_dest_btn():
    #     global dest
    #     dest = ts_combo.get()
    #     if len(dest) == 0:
    #         dest = "en"
    #     else:
    #         dest = lang_dict[dest]

    # dest_btn = Button(setting_win, width=20, height=4,
    #                   command=command_for_dest_btn, text=dest_text, font="Helvetica 10 bold")
    # global ts_btn_select
    # ts_btn_select = False

    # def ts_btn():
    #     global ts_btn_select
    #     all_in_one_ts = [ts_combo, dest_btn]
    #     if tsvalue.get() == True:
    #         ts_combo.grid(row=3, column=2)
    #         dest_btn.grid(row=4, column=2)
    #         tsvalue.set(False)
    #         ts_btn_select = True
    #     else:
    #         for ob in all_in_one_ts:
    #             ob.grid_forget()
    #         tsvalue.set(True)
    #         ts_btn_select = False
    # translate_button = Checkbutton(setting_win, text=translate_text, variable=CheckVar,
    #                                width=20, height=4, font="Helvetica 25 bold", command=ts_btn)
    # translate_button.grid(row=3, column=1)
    setting_win.mainloop()


def command_for_delete():
    delete_win = Tk()
    delete_win.iconbitmap(r'icon.ico')
    cvoca = Vocabulary(language)

    def delete_win_quit():
        delete_win.destroy()

    if language == "english":
        delete_win_title = "Delete Word"
    else:
        delete_win_title = "단어 삭제"

    delete_win['bg'] = '#50BCDF'
    delete_win.title(delete_win_title)
    delete_win.option_add("*Font", "Helvetica")
    delete_win.geometry(
        f"{int(delete_win.winfo_screenwidth() * (2.5 / 3))}x{int(delete_win.winfo_screenheight() * 0.8)}")

    delete_list = list()
    for i, (word, mean) in enumerate(cvoca.voca['jvocabulary'].items()):
        delete_list.append(word + ' ▬ ' + mean)

    def command_for_delete_btn():
        _word, _mean = delete_combo.get().split(' ▬ ')
        cvoca.delete(_word)
        success_label = Label(delete_win,
                              text="\"{}\" {} \"{}\" {}".format(_word, delete_win_and, _mean,
                                                                delete_win_success_text),
                              font="Helvetica 25 bold")
        success_label.place(relx=0.01, rely=0.945)

    if language == "english":
        delete_win_delete_btn_text = "Delete"
        delete_win_success_text = "have been successfully deleted"
        delete_win_and = "and"
    else:
        delete_win_delete_btn_text = "삭제"
        delete_win_success_text = "단어가 성공적으로 삭제되었습니다"
        delete_win_and = "와/과"
    if language == "english":
        delete_win_close_btn_text = "Quit"
    else:
        delete_win_close_btn_text = "종료"

    delete_combo = ttk.Combobox(
        delete_win, values=delete_list, width=96, height=5, font="Helvetica 25 bold")
    delete_combo.place(relx=0, rely=0.2, relheight=0.09, relwidth=1.0)

    delete_btn = Button(delete_win, command=command_for_delete_btn, text=delete_win_delete_btn_text,
                        font="Helvetica 50 bold")
    delete_btn.place(relx=0.01, rely=0.51, relwidth=0.485, relheight=0.43)

    cancel_btn = Button(delete_win, command=delete_win_quit, text=delete_win_close_btn_text,
                        font="Helvetica 50 bold")
    cancel_btn.place(relx=0.505, rely=0.51, relwidth=0.485, relheight=0.43)

    delete_win.mainloop()


def command_for_add():
    cvoca = Vocabulary(language)
    if language == "english":
        add_win_title = "Add Word"
    else:
        add_win_title = "단어 추가"

    add_win = Tk()
    add_win.iconbitmap(r'icon.ico')
    add_win['bg'] = '#50BCDF'
    add_win.title(add_win_title)

    # if language == "english":
    #     add_win_trans_btn_text = "Translate"
    # else:
    #     add_win_trans_btn_text = "번역"

    if language == "english":
        add_win_add_btn_text = "Add"
    else:
        add_win_add_btn_text = "추가"

    if language == "english":
        add_win_success_text = "have successfully been added to the vocabulary"
        add_win_and = "and"
    else:
        add_win_success_text = "단어가 성공적으로 추가되었습니다"
        add_win_and = "와/과"

    if language == "english":
        add_win_close_btn_text = "Quit"
    else:
        add_win_close_btn_text = "종료"

    def command_for_add_btn():
        _word = word_entry.get()
        _mean = mean_entry.get()
        cvoca.add(_word, _mean)
        success_label = Label(add_win, text="\"{}\" {} \"{}\" {}".format(
            _word, add_win_and, _mean, add_win_success_text), font="Helvetica 25 bold")
        success_label.place(relx=0.01, rely=0.945)

    def add_win_quit():
        add_win.destroy()

    # def translate():
    #     WEG = word_entry.get()
    #     result1 = ts.translate(text=WEG, dest=dest)
    #     mean_entry.insert(0, result1.text)

    add_win.geometry(
        f"{int(add_win.winfo_screenwidth() * (2.5 / 3))}x{int(add_win.winfo_screenheight() * 0.8)}")
    add_win.option_add("*Font", "Helvetica 50")
    word_entry = Entry(add_win, font="Helvetica 50 bold")
    mean_entry = Entry(add_win, font="Helvetica 50 bold")
    add_btn = Button(add_win, command=command_for_add_btn,
                     text=add_win_add_btn_text, font="Helvetica 50 bold")
    close_btn = Button(add_win, command=add_win_quit,
                       text=add_win_close_btn_text, font="Helvetica 50 bold")
    # if ts_btn_select == True:
    #     translate_btn = Button(add_win, command=translate,
    #                            text=add_win_trans_btn_text, font="Helvetica 20 bold")
    #     translate_btn.place(relx=0.01, rely=0.01,
    #                         relwidth=0.98, relheight=0.03)
    word_entry.place(relx=0.01, rely=0.05, relwidth=0.485, relheight=0.47)
    mean_entry.place(relx=0.505, rely=0.05, relwidth=0.485, relheight=0.47)
    add_btn.place(relx=0.01, rely=0.55, relwidth=0.485, relheight=0.43)
    close_btn.place(relx=0.505, rely=0.55, relwidth=0.485, relheight=0.43)
    add_win.mainloop()


if language == "english":
    win_title = "Vocabulary"
else:
    win_title = "단어장"


def main():
    global win
    win = Tk()
    win.iconbitmap(r'icon.ico')
    win['bg'] = '#50BCDF'
    win.title(win_title)
    win.geometry("500x600")
    win.option_add("*Font", "Helvetica")

    if language == "english":
        win_see_btn_text = "See"
        win_add_btn_text = "Add"
        win_modify_btn_text = "Modify"
        win_delete_btn_text = "Delete"
        win_close_btn_text = "Quit"
        win_setting_btn_text = "Setting"
    else:
        win_see_btn_text = "보기"
        win_add_btn_text = "추가"
        win_modify_btn_text = "수정"
        win_delete_btn_text = "삭제"
        win_close_btn_text = "종료"
        win_setting_btn_text = "설정"

    see_btn = Button(win, text=win_see_btn_text,
                     command=command_for_see, width=40, height=5)
    add_btn = Button(win, text=win_add_btn_text,
                     command=command_for_add, width=40, height=5)
    modify_btn = Button(win, text=win_modify_btn_text,
                        command=command_for_modify, width=40, height=5)
    delete_btn = Button(win, text=win_delete_btn_text,
                        command=command_for_delete, width=40, height=5)
    setting_btn = Button(win, text=win_setting_btn_text,
                         command=command_for_setting, width=40, height=5)
    quit_btn = Button(win, text=win_close_btn_text,
                      command=win.destroy, width=35, height=5)
    see_btn.pack()
    add_btn.pack()
    modify_btn.pack()
    delete_btn.pack()
    setting_btn.pack()
    quit_btn.pack()
    win.mainloop()


main()
