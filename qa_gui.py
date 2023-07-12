import tkinter as tk

def open_cqa_gui():
    cqa_window = tk.Toplevel(qa_window)
    cqa_window.title("Categories/Questions/Answers")

    # Create labels and entry fields for categories
    category_label1 = tk.Label(cqa_window, text="Category 1:")
    category_label1.pack()
    category_entry1 = tk.Entry(cqa_window)
    category_entry1.pack()

    category_label2 = tk.Label(cqa_window, text="Category 2:")
    category_label2.pack()
    category_entry2 = tk.Entry(cqa_window)
    category_entry2.pack()

    category_label3 = tk.Label(cqa_window, text="Category 3:")
    category_label3.pack()
    category_entry3 = tk.Entry(cqa_window)
    category_entry3.pack()

    category_label4 = tk.Label(cqa_window, text="Category 4:")
    category_label4.pack()
    category_entry4 = tk.Entry(cqa_window)
    category_entry4.pack()

    questions_answers = []

    def add_question_answer():
        question = question_entry.get()
        answer = answer_entry.get()
        questions_answers.append((question, answer))
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        question_entry.focus()

    def submit_cqa_details():
        category1 = category_entry1.get()
        category2 = category_entry2.get()
        category3 = category_entry3.get()
        category4 = category_entry4.get()

        # Process the submitted details and start the game
        # ...

        cqa_window.destroy()

    question_label = tk.Label(cqa_window, text="Question:")
    question_label.pack()
    question_entry = tk.Entry(cqa_window)
    question_entry.pack()

    answer_label = tk.Label(cqa_window, text="Answer:")
    answer_label.pack()
    answer_entry = tk.Entry(cqa_window)
    answer_entry.pack()

    add_button = tk.Button(cqa_window, text="Add", command=add_question_answer)
    add_button.pack()

    submit_button = tk.Button(cqa_window, text="Submit", command=submit_cqa_details)
    submit_button.pack(pady=10)

def submit_details():
    player1_name = player_entry1.get()
    player2_name = player_entry2.get()
    player3_name = player_entry3.get()
    player4_name = player_entry4.get()

    player_colors = {
        player1_name: color_var1.get(),
        player2_name: color_var2.get(),
        player3_name: color_var3.get(),
        player4_name: color_var4.get()
    }

    # Process the submitted details and start the game
    # ...

    qa_window.destroy()

# Create a new window for the question/answer GUI
qa_window = tk.Tk()
qa_window.title("QA GUI")

# Create labels and entry fields for player names
player_label1 = tk.Label(qa_window, text="Player 1 Name:")
player_label1.pack()
player_entry1 = tk.Entry(qa_window)
player_entry1.pack()

player_label2 = tk.Label(qa_window, text="Player 2 Name:")
player_label2.pack()
player_entry2 = tk.Entry(qa_window)
player_entry2.pack()

player_label3 = tk.Label(qa_window, text="Player 3 Name:")
player_label3.pack()
player_entry3 = tk.Entry(qa_window)
player_entry3.pack()

player_label4 = tk.Label(qa_window, text="Player 4 Name:")
player_label4.pack()
player_entry4 = tk.Entry(qa_window)
player_entry4.pack()

# Create radio buttons for player colors
color_frame = tk.Frame(qa_window)
color_frame.pack()

color_label1 = tk.Label(color_frame, text="Select Player 1 Color:")
color_label1.grid(row=0, column=0, padx=5, pady=5)
color_var1 = tk.StringVar(value="blue")
color_rb1_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var1, value="blue")
color_rb1_blue.grid(row=0, column=1)

color_rb1_green = tk.Radiobutton(color_frame, text="Green", variable=color_var1, value="green")
color_rb1_green.grid(row=0, column=2)

color_rb1_red = tk.Radiobutton(color_frame, text="Red", variable=color_var1, value="red")
color_rb1_red.grid(row=0, column=3)

color_rb1_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var1, value="yellow")
color_rb1_yellow.grid(row=0, column=4)

color_label2 = tk.Label(color_frame, text="Select Player 2 Color:")
color_label2.grid(row=1, column=0, padx=5, pady=5)
color_var2 = tk.StringVar(value="blue")
color_rb2_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var2, value="blue")
color_rb2_blue.grid(row=1, column=1)

color_rb2_green = tk.Radiobutton(color_frame, text="Green", variable=color_var2, value="green")
color_rb2_green.grid(row=1, column=2)

color_rb2_red = tk.Radiobutton(color_frame, text="Red", variable=color_var2, value="red")
color_rb2_red.grid(row=1, column=3)

color_rb2_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var2, value="yellow")
color_rb2_yellow.grid(row=1, column=4)

color_label3 = tk.Label(color_frame, text="Select Player 3 Color:")
color_label3.grid(row=2, column=0, padx=5, pady=5)
color_var3 = tk.StringVar(value="blue")
color_rb3_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var3, value="blue")
color_rb3_blue.grid(row=2, column=1)

color_rb3_green = tk.Radiobutton(color_frame, text="Green", variable=color_var3, value="green")
color_rb3_green.grid(row=2, column=2)

color_rb3_red = tk.Radiobutton(color_frame, text="Red", variable=color_var3, value="red")
color_rb3_red.grid(row=2, column=3)

color_rb3_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var3, value="yellow")
color_rb3_yellow.grid(row=2, column=4)

color_label4 = tk.Label(color_frame, text="Select Player 4 Color:")
color_label4.grid(row=3, column=0, padx=5, pady=5)
color_var4 = tk.StringVar(value="blue")
color_rb4_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var4, value="blue")
color_rb4_blue.grid(row=3, column=1)

color_rb4_green = tk.Radiobutton(color_frame, text="Green", variable=color_var4, value="green")
color_rb4_green.grid(row=3, column=2)

color_rb4_red = tk.Radiobutton(color_frame, text="Red", variable=color_var4, value="red")
color_rb4_red.grid(row=3, column=3)

color_rb4_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var4, value="yellow")
color_rb4_yellow.grid(row=3, column=4)

cqa_button = tk.Button(qa_window, text="Categories/Questions/Answers", command=open_cqa_gui)
cqa_button.pack(pady=10)

submit_button = tk.Button(qa_window, text="Submit", command=submit_details)
submit_button.pack(pady=10)

# Start the question/answer GUI event loop
qa_window.mainloop()
