from random import randint

#equipable item lists
weapons = {'melee':(1,2), 'stick':(1,5), 'sword':(3,8), 'sharpsword':(4,10), 'big axe':(90,100)}
armour = {'none':None, 'leather armor':(2, 10, 50), 'enchanted leather armor':(2, 10, 100), 'halo':(90, 100, 50)}

#gets the defence percentage of a creature, or if it has any defence at all
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
        
    
#gets how much damage You would do to Enemy
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
      
#a full blown battle function that results in a fight to the death
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

'''
checks if You are faster than Enemy;
if speeds are the same the creature with more health is faster;
if health is the same You is faster by default
'''
def checkIfFaster(you, enemy):
    if you.speed > enemy.speed:
        return True
    elif enemy.speed > you.speed:
        return False
    else:
        if you.health > enemy.health:
            return True
        elif enemy.health > you.health:
            return False
        else:
            return True
  
#checks if creature dies after the specified amount of damage is dealt
def checkDeath(creature, damage):
    health = creature.health
    health -= damage
    if health <= 0:
        return True
    else:
        return False

#simple function that deducts hit points from a creature
def deductDamage(creature, damage):
    creature.health -= damage

#the creature class
class Creature:
    def __init__(self, health, name, weapon, armor, speed):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.max_health = health

#the player class
class Player(Creature):
    pass

#possible enemy list
enemies = []

#2 enemies and you, the player as class instances
enemies.append(Creature(60, 'Enemy, level 1', 'stick', 'none', 10))
enemies.append(Creature(80, 'Enemy, level 2', 'stick', 'leather armor', 20))
player = Player(100, 'Broman', 'sword', 'leather armor', 20)

#battle
try:
    battle(player, enemies[0], 1)
except NameError:
    print('\nYou have died! You can\'t battle any more!')
except IndexError:
    print('\nYou are trying to fight a dead creature!')

#another battle, if the player survives
try:
    battle(enemies[0], player, 1)
except NameError:
    print('\nYou have died! You can\'t battle any more!')
except IndexError:
    print('\nYou are trying to fight a dead creature!')