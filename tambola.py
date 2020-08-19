#!/usr/bin/python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.graphics import Color
import random
coins = random.sample(range(1,91), 90)
#print(coins)
picked_coins=[]
current_coin=0
#print(picked_coins)
class Housie(FloatLayout):
	def __init__(self,**kwargs):
		super(Housie,self).__init__(**kwargs)
		self.title = Label(text="Housie Coin Picker",font_size = 50,size_hint=(1, .55),pos_hint={'x':0, 'y':.45})
		self.main_label = Label(text = "Click PICK NUMBER", size_hint=(1, .60),pos_hint={'x':0, 'y':.35})
		self.picked_ones = Label(text = "picked_coins", size_hint=(1, .40),pos_hint={'x':0, 'y':.40})
		self.help_button = Button(text = "PICK NUMBER", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1},on_press = self.update)
		self.add_widget(self.title)
		self.add_widget(self.main_label)
		self.add_widget(self.picked_ones)
		self.add_widget(self.help_button)
		self.add_widget(self.userinterface())
	def userinterface(self):
		self.layout = GridLayout(cols = 10,size_hint=(.50, .50))
		for i in range(1,91):
			self.layout.add_widget(Button(background_color=(1,0,0,1),text =str(i)))
		return self.layout
	def update(self,event):
		for coin in coins:
			if coin not in picked_coins:
				current_coin=coin
				picked_coins.append(coin)
				self.main_label.text = str(coin)
				for i in self.layout.children:
					if i.text == str(coin):
						print(i,i.text)
						i.background_normal=''
						i.background_color=(0,0,1,1)
						print(i,i.text)
				break
		self.picked_ones.text = "Picked coins = {}".format(" ".join(str(sorted(picked_coins))))
class app1(App):
	def build(self):
		return Housie()
if __name__=="__main__":
     app1().run()