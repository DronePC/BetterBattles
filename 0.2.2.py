from random import randint
#make equips here
weapons = {'melee':(1,2), 'stick':(1,5), 'sword':(3,8), 'sharpsword':(4,10), 'big axe':(90,100)}
armour = {'none':None, 'leather armor':(2, 10, 50), 'enchanted leather armor':(2, 10, 100), 'halo':(90, 100, 50)}

def getDefence(creature):
    if creature.armor == 'none':
        return 2
    else:
        probdef = armour[creature.armor]
        defence = randint(probdef[0], probdef[1])
        ratio = randint(1,100)
        chance = probdef[2]
        if ratio <= chance:
            return defence / 100
        else:
            return 2
        
    

def getAttack(you, enemy):
    probdmg = weapons[you.weapon]
    dmg = randint(probdmg[0], probdmg[1])
    posdef = getDefence(enemy)
    if posdef == 2:
        return dmg
    else:
        defence = round(enemy.max_health / dmg * posdef)
        if defence > 0:
            if dmg > defence:
                return dmg - defence
            else:
                return 0
        else:
            return dmg
      
#battles
def battle(you,enemy,count):
    if count == 1:
        print('\nNEW BATTLE!\n {0} and {1} are fighting tonight!\n'.format(you.name, enemy.name))

    global enemies
    global player
    yatk = getAttack(you, enemy)
    eatk = getAttack(enemy, you)

    if checkIfFaster(you, enemy):
        deductDamage(enemy, yatk)
        print('{0} has dealt {1} damage to {2}! {2} now has {3} health left!'.format(you.name, yatk, enemy.name, enemy.health))

        if checkDeath(enemy, yatk):
            print('{0} has died! {1} has won the battle!\n'.format(enemy.name, you.name))

            if enemy in enemies:
                enemies.remove(enemy)
                return None
            else:
                print('R.I.P., game over!\n')
                del player
                return None

        deductDamage(you, eatk)
        print('{0} has dealt {1} damage to {2}! {2} now has {3} health left!\n'.format(enemy.name, eatk, you.name, you.health))

        if checkDeath(you, yatk):
            print('{0} has died! {1} has won the battle!'.format(you.name, enemy.name))

            if you in enemies:
                enemies.remove(you)
                return None
            else:
                print('R.I.P., game over!\n')
                del player
                return None
  
    else:
        deductDamage(you, eatk)
        print('{0} has dealt {1} damage to {2}! {2} now has {3} health left!\n'.format(enemy.name, eatk, you.name, you.health))

        if checkDeath(you, yatk):
            print('{0} has died! {1} has won the battle!'.format(you.name, enemy.name))

            if you in enemies:
                enemies.remove(you)
                return None
            else:
                print('R.I.P., game over!\n')
                del player
                return None

        deductDamage(enemy, yatk)
        print('{0} has dealt {1} damage to {2}! {2} now has {3} health left!'.format(you.name, yatk, enemy.name, enemy.health))

        if checkDeath(enemy, yatk):
            print('{0} has died! {1} has won the battle!\n'.format(enemy.name, you.name))

            if enemy in enemies:
                enemies.remove(enemy)
                return None
            else:
                print('R.I.P., game over!\n')
                del player
                return None

    count += 1
    battle(you, enemy, count)

def checkIfFaster(you, enemy):
    if you.speed > enemy.speed:
        return True
    else:
        return False
  
#checks if creature dies after the specified amount of damage is dealt. Death = True
def checkDeath(creature, damage):
    health = creature.health
    health -= damage
    if health <= 0:
        return True
    else:
        return False

def deductDamage(creature, damage):
    creature.health -= damage

class Creature:
    def __init__(self, health, name, weapon, armor, speed):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.max_health = health

class Player(Creature):
    pass

enemies = []

#change equips here
enemies.append(Creature(1000, 'Enemy, level 1', 'sharpsword', 'leather armor', 100))
player = Player(100, 'Broman', 'sword', 'leather armor', 20)

#2 battles
try:
    battle(player, enemies[0], 1)
except NameError:
    print('\nYou have died! You can\'t battle any more!')
except IndexError:
    print('\nYou are trying to fight a dead creature!')

try:
    battle(enemies[0], player, 1)
except NameError:
    print('\nYou have died! You can\'t battle any more!')
except IndexError:
    print('\nYou are trying to fight a dead creature!')