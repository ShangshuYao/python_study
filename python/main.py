import os
import face_train
import face_get
import tkinter as tk


# 建立一个主窗口
def main_window_create():
    # 创建一个窗口
    main_window = tk.Tk()
    # 设置窗口标题、大小、背景颜色
    main_window.title("人脸识别")
    main_window.geometry('800x600')
    main_window.configure(background='white')
    # 添加按钮
    face_recognition_btn = tk.Button(main_window, text='开始识别', bg='blue', fg='white', font=('楷体', 16),
                                     padx=100, pady=20, activebackground='red',
                                     command=face_train.face_recognition).place(x=275, y=300)
    face_train_btn = tk.Button(main_window, text='模型训练', bg='blue', fg='white', font=('楷体', 16),
                               padx=100, pady=20, activebackground='red',
                               command=face_train.face_train).place(x=275, y=200)
    face_get_btn = tk.Button(main_window, text='人脸采集', bg='blue', fg='white', font=('楷体', 16),
                             padx=100, pady=20, activebackground='red',
                             command=face_get.face_get).place(x=275, y=100)
    main_window.mainloop()


# main函数
if __name__ == '__main__':
    main_window_create()
