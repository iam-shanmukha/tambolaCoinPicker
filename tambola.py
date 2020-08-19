#!/usr/bin/python
'''

App: TambolCoinPicker
Author: Shanmukha Vishnu
github: @iam-shanmukha
twitter: @iam_shanmukha
website: www.shanmukhavishnu.in

'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.properties  import NumericProperty
import random
coins = random.sample(range(1,91), 90)
picked_coins=[0]
class Housie(FloatLayout):
	def __init__(self,**kwargs):
		super(Housie,self).__init__(**kwargs)

		#Declaration
		self.title = Label(text="Housie Coin Picker",font_size = 50,size_hint=(1, .55),pos_hint={'x':0, 'y':.60})
		#Label to show Picked Number
		self.main_label = Label(text = "",font_size=90, size_hint=(1, .60),pos_hint={'x':0, 'y':.40})
		#Label to show previous number
		self.prev_label = Label(text = "Previous Number",font_size=30, size_hint=(1, .60),pos_hint={'x':0, 'y':.25})
		self.help_button = Button(text = "PICK NUMBER", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1},on_press = self.update)
		self.interval_time = Slider(min = 0, max = 5,size_hint=(0.2, 0.2),pos_hint={'top': 0.8})
		self.interval_value = Label(text ='0',size_hint=(0.4, 0.2),pos_hint={'top': 0.8})


		#Widget Creation
		self.add_widget(self.title)
		self.add_widget(self.main_label)
		self.add_widget(self.prev_label)
		#self.add_widget(self.picked_ones)

		self.add_widget(self.help_button)
		self.add_widget(self.userinterface())

		#Scheduling
		self.add_widget(Label(text ='Interval in seconds',size_hint=(0.2, 0.1),pos_hint={'top': 0.8}))
		self.add_widget(self.interval_time)
		#self.add_widget(Label(text ='Slider Value',size_hint=(1, .55),pos_hint={'top': 0.9})) 
		self.add_widget(self.interval_value)
		self.interval_time.bind(value = self.on_value) 

		#Enabling below lines Picks coin based on Time automatically
		#Clock.schedule_interval(self.update, 2) 
	def on_value(self, instance, slider_val):
		self.interval_value.text = "% d"% slider_val
		print(self.interval_value.text)
		if int(self.interval_value.text) ==0:
			Clock.unschedule(self.update)
		if int(self.interval_value.text) ==1:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 1)
		if int(self.interval_value.text) ==2:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 2)
		if int(self.interval_value.text) ==3:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 3)
		if int(self.interval_value.text) ==4:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 4)

	def userinterface(self):
		self.layout = GridLayout(cols = 10,size_hint=(.50, .50))
		for i in range(1,91):
			self.layout.add_widget(Button(background_color=(1,0,0,1),text =str(i)))
		return self.layout
	def update(self,event):
		for coin in coins:
			if coin not in picked_coins:
				self.prev_label.text = str(f"Previous Number: {picked_coins[-1]}")
				picked_coins.append(coin)
				self.main_label.text = str(coin)
				for i in self.layout.children:
					if i.text == str(coin):
						print(i,i.text)
						#change the color of picked coin
						i.background_normal=''
						i.background_color=(0,0,1,1)
				break
class app1(App):
	def build(self):
		return Housie()
if __name__=="__main__":
     app1().run()