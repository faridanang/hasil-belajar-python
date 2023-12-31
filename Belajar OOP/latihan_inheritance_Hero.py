# Latihan inheritance 

class Hero:
	def __init__(self,name):
		self.__name = name
		self.health_pool = [0,100,200,300,400,500]
		self.attack_pool = [0,10,20,30,40,50]
		self.armor_pool = [0,20,40,60,80,100]
		self.__level = 0
		self.__exp = 0
		
	def info(self):
		print('''
{} Level {}
 Health: {}
 Attack: {}
 Armor: {}	
		'''.format(
		self.__name,
		self.__level,
		self.__health,
		self.__attack,
		self.__armor
		))
		
	@property
	def health_pool(self):
		pass
	@property
	def attack_pool(self):
		pass
	@property
	def armor_pool(self):
		pass
	@property
	def gainExp(self):
		pass
	@property
	def levelUp(self):
		pass
		
	@health_pool.setter
	def health_pool(self,input):
		self.__health_pool = input
	@attack_pool.setter
	def attack_pool(self,input):
		self.__attack_pool = input
	@armor_pool.setter
	def armor_pool(self,input):
		self.__armor_pool = input
		
	@gainExp.setter
	def gainExp(self,input):
		self.__exp += input
		if self.__exp >= 100:
			self.levelUp = self.__exp // 100
			self.__exp %= 100
			
	@levelUp.setter
	def levelUp(self,input):
		self.__level += input
		self.__health = self.__health_pool[self.__level]
		self.__attack = self.__attack_pool[self.__level]
		self.__armor = self.__armor_pool[self.__level]
		
class Fighter(Hero):
		def __init__(self,name):
			super().__init__(name)
			self.health_pool = [0,100,200,300,400,600]
			self.attack_pool = [0,10,20,30,40,50]
			self.armor_pool = [0,20,40,60,80,100]
			self.levelUp = 1
			
class Tank(Hero):
		def __init__(self,name):
			super().__init__(name)
			self.health_pool = [0,100,200,300,400,600]
			self.attack_pool = [0,10,20,30,40,50]
			self.armor_pool = [0,20,40,60,80,100]
			self.levelUp = 1		