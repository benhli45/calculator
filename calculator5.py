from tkinter import *
import math

class Calc():
	def __init__(self):
		self.arithmetic_Operator = ''
		self.result = False
		self.check_sum = False
		self.total = 0
		self.current = ''
		self.input_value = True

	def numberEnter(self, num):
		self.result = False
		firstnum = txtDisplay.get()
		secondnum = str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum + secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result = True
		self.current = int(self.current)
		if self.check_sum == True:
			self.valid_function()
		else: 
			self.total = int(txtDisplay.get())

	def valid_function(self):
		if self.op == 'add':
			self.total += self.current
		if self.op == 'sub':
			self.total -= self.current
		if self.op == 'mult':
			self.total *= self.current
		if self.op == 'div':
			self.total /= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)

	def operation(self, op):
		self.current = int(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False

	def display(self, value): 
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def clear_Entry(self):
		self.result = False
		self.current = ''
		self.display('')
		self.input_value = True

	def clear_Screen(self):
		self.clear_Entry()
		self.total = ''

	def backspace(self):
		self.result = False
		text = txtDisplay.get()[:-1]
		if text == '':
			text = ''
		self.current = text
		self.display(text)

	def opPM(self):
		self.result = False
		self.current = -(int(txtDisplay.get()))
		self.display(self.current)

	def sqrt(self):
		self.result = False
		self.current = math.sqrt(int(txtDisplay.get()))
		self.display(self.current)

	def square(self):
		self.result = False
		self.current = math.pow(int(txtDisplay.get()), 2)
		self.display(self.current)

	def divone(self):
		self.result = False
		self.current = 1 / int(txtDisplay.get())
		self.display(self.current)

added_value = Calc()

root = Tk()
root.title('Calculator')
root.iconbitmap(r'C:/Users/benhl/Desktop/Learn_Python/images/calculator.ico')

top_frame = Frame(root, height = 60)
main_calc = Frame(root)

top_frame.grid(row = 0, sticky='n')
main_calc.grid(row = 1, sticky='s')

txtDisplay = Entry(top_frame, font = ('arial', 18), bd = 10, width = 23, justify = RIGHT) 
txtDisplay.grid(row = 0, column = 0, columnspan = 6, pady = 1, sticky='n')

#---------------------------------------------Row 1 Buttons----------------------------------------------------
btnMC = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'MC').grid(row = 1, column = 0, pady = 1)

btnMR = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'MR').grid(row = 1, column = 1, pady = 1)

btnMPlus = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'M+').grid(row = 1, column = 2, pady = 1)

btnMMinus = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'M-').grid(row = 1, column = 3, pady = 1)

btnMS = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'MS').grid(row = 1, column = 4, pady = 1)

btnMTri = Button(top_frame, width = 3, font = ('arial', 18), bd = 2, text = 'M▼').grid(row = 1, column = 5, pady = 1)

#---------------------------------------------Row 2 Buttons----------------------------------------------------
btnPer = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '%').grid(row = 2, column = 0, pady = 1)

btnSqrt = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '√', command = added_value.sqrt).grid(row = 2, column = 1, pady = 1)

btnSquare = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = 'x²', command = added_value.square).grid(row = 2, column = 2, pady = 1)

btnDivOne = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '1/x', command = added_value.divone).grid(row = 2, column = 3, pady = 1)

#---------------------------------------------Row 3 Buttons----------------------------------------------------
btnCE = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = 'CE', command = added_value.clear_Entry).grid(row = 3, column = 0, pady = 1)

btnC = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = 'C', command = added_value.clear_Screen).grid(row = 3, column = 1, pady = 1)

btnBkspc = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '⌫', command = added_value.backspace).grid(row = 3, column = 2, pady = 1)

#---------------------------------------------Calculator Number Pad--------------------------------------------
numberpad = '789456123'
i = 0
btn = []
for j in range(4, 7):
	for k in range(3):
		btn.append(Button(main_calc, width = 5, font = ('arial', 18), bd = 2, bg='white', text = numberpad[i]))
		btn[i].grid(row = j, column = k, pady = 1)
		btn[i]['command'] = lambda x = numberpad [i]: added_value.numberEnter(x)
		i += 1

#---------------------------------------------Operators--------------------------------------------------------
btnDiv = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '/', command = lambda: added_value.operation('div')).grid(row = 3, column = 3, pady = 1)

btnMult = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '*', command = lambda: added_value.operation('mult')).grid(row = 4, column = 3, pady = 1)

btnSub = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '-', command = lambda: added_value.operation('sub')).grid(row = 5, column = 3, pady = 1)

btnAdd = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '+', command = lambda: added_value.operation('add')).grid(row = 6, column = 3, pady = 1)

#---------------------------------------------Row 7 Buttons----------------------------------------------------
btnOpPM = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '±', command = added_value.opPM).grid(row = 7, column = 0, pady = 1)

btn0 = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, bg = 'white', text = '0', command = lambda: added_value.numberEnter(0)).grid(row = 7, column = 1, pady = 1)

btnDec = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '.').grid(row = 7, column = 2, pady = 1)

btnEqu = Button(main_calc, width = 5, font = ('arial', 18), bd = 2, text = '=', command = added_value.sum_of_total).grid(row = 7, column = 3, pady = 1)

root.mainloop()