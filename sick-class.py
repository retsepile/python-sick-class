from tkinter import *
from tkinter import messagebox

window = Tk()
window .title("StudentNo:78120734678964")
window.geometry("500x500")


# Parent class of influenza and cancer classes
class Sick:
    def __init__(self):  # Placing the labels
        sickness_code = Label(window, text="Sickness Code:")
        sickness_code.place(x=25, y=150, anchor="w")

        treatment_duration = Label(window, text="Duration of Treatment:")
        treatment_duration.place(x=25, y=200, anchor="w")

        duration_unit = Label(window, text="Weeks/Months")
        duration_unit.place(x=390, y=188)

        doc_prac_num = Label(window, text="Doctor's Practice Number:")
        doc_prac_num.place(x=25, y=250, anchor="w")

        fee = Label(window, text="Scan/Consultation Fee:")
        fee.place(x=25, y=300, anchor="w")

        amount_paid_label = Label(window, text="Amount paid for treatment:")
        amount_paid_label.place(x=25, y=400)

        # Creating the entry boxes
        self.sick_id = Entry(window)
        self.duration = Entry(window, width=10)
        self.doc_id = Entry(window)
        self.scan_or_consult = Entry(window)

        self.sick_id.place(x=300, y=135)
        self.duration.place(x=300, y=185)
        self.doc_id.place(x=300, y=235)
        self.scan_or_consult.place(x=300, y=285)

        # Creating Radiobuttons
        self.v = IntVar()
        cancer_radio = Radiobutton(window, text="Cancer", variable=self.v, value=1)
        influenza_radio = Radiobutton(window, text="Influenza", variable=self.v, value=2)

        cancer_radio.place(x=20, y=330)
        influenza_radio.place(x=20, y=360)

        # calculate, clear and exit buttons

        def calculate():   # This function is to redirect the calculation based on the radio button selected
            radio = self.v.get()
            if radio == 1:
                can = Cancer(self.scan_or_consult.get())
            elif radio == 2:
                flu = Influenza(self.scan_or_consult.get())

        calc_btn = Button(window, text="Calculate", command=calculate)
        calc_btn.place(x=25, y=450)

        def clear():   # This function clears entry fields
            self.sick_id.delete(0, 'end')
            self.duration.delete(0, 'end')
            self.doc_id.delete(0, 'end')
            self.scan_or_consult.delete(0, 'end')

        clear_btn = Button(window, text="Clear", command=clear)
        clear_btn.place(x=225, y=450)

# Child of sick class for cancer calculation and display


class Cancer(Sick):

    def __init__(self, scan):
        amount_paid_display = Label(window, text="")
        amount_paid_display.place(x=225, y=400)
        medication = 400
        self.scan = scan

        if float(scan) > 600:
            messagebox.showinfo("", "Sorry we cannot treat you")
        else:
            amount_paid = float(scan) + medication
            amount_paid_display.config(text="R"+str(round(amount_paid, 4)))

# Child of sick class for influenza calculation and display


class Influenza(Sick):

    def __init__(self, consult):
        x = StringVar()
        amount_paid_display = Label(window, textvariable=x)
        amount_paid_display.place(x=225, y=400)
        medication = 350.50
        self.consult = consult
        consult = float(consult)

        if consult > 600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
        else:
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")


exit_btn = Button(window, text="Exit", command=window .destroy)
exit_btn.place(x=425, y=450)
# tkinter stuff creating window


app = Sick()

window .mainloop()
