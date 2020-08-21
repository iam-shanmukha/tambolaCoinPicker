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
from kivy.properties import NumericProperty
import random,os,sys
from plyer import tts


class Housie(FloatLayout):
	def __init__(self,**kwargs):
		super(Housie,self).__init__(**kwargs)
		self.coins = random.sample(range(1,91), 90)
		self.picked_coins=[0]

		#Declaration
		self.title = Label(text="Housie Coin Picker",font_size = 50,size_hint=(1, 0.55),pos_hint={'x':0, 'y':.60})
		#Label to show Picked Number
		self.main_label = Label(text = "",font_size=150, size_hint=(1, .70),pos_hint={'x':0, 'y':.35})
		#Label to show previous number
		self.prev_label = Label(text = "Previous Number",font_size=80, size_hint=(1, .60),pos_hint={'x':0, 'y':.25})
		self.click_button = Button(text = "PICK NUMBER", font_size=30,size_hint=(0.2, 0.1),pos_hint={'x':.75, 'y':0.65},on_press = self.update)

		app = App.get_running_app()
		self.reset_button = Button(text = "RESET",background_normal = 'normal.png',background_down ='down.png',size_hint=(0.1, 0.1),pos_hint={'x':0.8, 'y':0.82},on_press=app.reset)

		self.interval_time = Slider(min = 0, max = 5,size_hint=(0.35, 0.2),pos_hint={'top': 0.8})
		self.interval_value = Label(text ='0',size_hint=(0.5, 0.1),pos_hint={'top': 0.8})
		#Widget Creation
		self.add_widget(self.title)
		self.add_widget(self.main_label)
		self.add_widget(self.prev_label)
		#self.add_widget(self.picked_ones)

		self.add_widget(self.click_button)
		self.add_widget(self.reset_button)
		self.add_widget(self.userinterface())

		#Scheduling
		self.add_widget(Label(text ='Time:',size_hint=(0.25, 0.1),pos_hint={'top': 0.8}))
		self.add_widget(self.interval_time)
		#self.add_widget(Label(text ='Slider Value',size_hint=(1, .55),pos_hint={'top': 0.9})) 
		self.add_widget(self.interval_value)
		self.interval_time.bind(value = self.on_value) 

		#Enabling below lines Picks coin based on Time automatically
		#Clock.schedule_interval(self.update, 2) 
	#Scheduling...		
	def on_value(self, instance, slider_val):
		self.interval_value.text = "% d"% slider_val
		siv = int(self.interval_value.text)
		print(self.interval_value.text)
		if int(self.interval_value.text) == 0:
			Clock.unschedule(self.update)
		if siv == 1:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 1)
		if siv ==2:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 2)
		if siv ==3:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 3)
		if siv ==4:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 4)
		if siv ==5:
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 5)

	def userinterface(self):
		self.layout = GridLayout(cols = 10,size_hint=(1, 0.5))
		for i in range(1,91):
			self.layout.add_widget(Button(background_color=(1,0,0,1),text =str(i)))
		return self.layout
	def update(self,event):
		for coin in self.coins:
			if coin not in self.picked_coins:
				self.prev_label.text = str("Previous Number: {}".format(self.picked_coins[-1]))
				self.picked_coins.append(coin)
				self.main_label.text = str(coin)
				#tts.speak(str(coin))			
				for i in self.layout.children:
					if i.text == str(coin):
						print(i,i.text)
						#change the color of picked coin
						i.background_normal=''
						i.background_color=(0,0,1,1)
				break

class app1(App):
	def build(self):
		fl = FloatLayout()
		fl.add_widget(Housie())
		return fl
	def reset(self, *largs):
		self.root.clear_widgets()# Discard previous Housie instance
		self.root.add_widget(Housie())# Replace it with a new instance

if __name__=="__main__":
     app1().run()