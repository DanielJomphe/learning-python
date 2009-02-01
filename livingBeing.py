#!/usr/bin/env python

class person(object):
    
    def __init__(self,speed):
        print "Je suis en train de naitre"
        self.speed = speed
        
    def getSpeed(self):
        if self.speed == 1:
            return "lentement"
        if self.speed == 2:
            return "normalement"
        if self.speed == 3:
            return "vite"
        
    def crawl(self):
        print "Je rampe " + self.getSpeed()
        
    def walk(self):
        print "Je marche " + self.getSpeed()

# >>> eric = person(3)
# Je suis en train de naitre
# >>> eric.crawl()
# Je rampe vite
# >>> eric.walk()
# Je marche vite

class handicap(person):
    
    def __init__(self,speed):
        print "Je suis en train de naitre"
        self.speed = speed
        if speed > 1:
            print "Tu voulais quelqu'un de " + self.getSpeed() + ", mais..."
            self.speed = 1

# >>> roger = handicap(3)
# Je suis en train de naitre
# Tu voulais quelqu'un de vite, mais...
# >>> roger.crawl()
# Je rampe lentement
# >>> roger.walk()
# Je marche lentement

class potential(object):
    
    def __init__(self,speed):
        self.speed = speed
        
    def getSpeed(self):
        if self.speed == 1:
            return "lentement"
        if self.speed == 2:
            return "normalement"
        if self.speed == 3:
            return "vite"


class person(object):
    
    def __init__(self,potential):
        print "Je suis en train de naitre"
        self.potential = potential
        
    def crawl(self):
        print "Je rampe " + self.potential.getSpeed()
        
    def walk(self):
        print "Je marche " + self.potential.getSpeed()

#>>> vite = potential(3)
#>>> moyen = potential(2)
#>>> lent = potential(1)
#>>> 
#>>> eric = person(vite)
#Je suis en train de naitre
#>>> eric.crawl()
#Je rampe vite
#>>> eric = person(lent)
#Je suis en train de naitre
#>>> eric.crawl()
#Je rampe lentement
#>>> eric = person(potential(2))
#Je suis en train de naitre
#>>> eric.crawl()
#Je rampe normalement

class livingBeing(object):
    
    def __init__(self,name):
        self.name = name
        print self.name + " est en train de naitre"
        
    def __str__(self):
        return self.name

#>>> blob = livingBeing("Blobby")
#Blobby est en train de naitre
#>>> blob
#<__main__.livingBeing object at 0x6fbb0>
#>>> print(blob)
#Blobby

class livingBeing(object):
    
    def __init__(self,name,potential):
        self.name = name
        self.potential = potential
        print self.name + " est en train de naitre"
        
    def __str__(self):
        return self.name
        
    def crawl(self):
        print "Je rampe " + self.potential.getSpeed()
        
    def walk(self):
        print "Je marche " + self.potential.getSpeed()
        
    def swim(self):
        print "Je nage " + self.potential.getSpeed()
        


class person(livingBeing):
    
    def __init__(self,name,potential):
        super(person, self).__init__(name,potential)
        

class animal(livingBeing):
    pass

class bird(animal):
    pass


#>>> clone = person("Eric", potential(3))
#Eric est en train de naitre
#>>> clone.swim()
#Je nage vite

#>>> b = bird("Duffy", potential(1))
#Duffy est en train de naitre
#>>> b.walk()
#Je marche lentement
#>>> b.swim()
#Je nage lentement
#>>> b.crawl()
#Je rampe lentement

class bird(animal):
    
    def crawl(self):
        print "HEY, demande-moi pas de ramper, je sais pas comment!!"

#>>> b2 = bird("Duffy", potential(1))
#Duffy est en train de naitre
#>>> b2.walk()
#Je marche lentement
#>>> b2.crawl()
#HEY, demande-moi pas de ramper, je sais pas comment!!

class fish(animal):
    
    def walk(self):
        print "HEY, je peux pas!"
        
    def swim(self):
        normalPotential = self.potential
        self.potential = potential(3)
        super(fish, self).swim()
        self.potential = normalPotential
        print "Et je peux respirer dans l'eau, nanana!"

#>>> f = fish("Nemo", potential(2))
#Nemo est en train de naitre
#>>> f.crawl()
#Je rampe normalement
#>>> f.swim()
#Je nage vite
#Et je peux respirer dans l'eau, nanana!
#>>> f.crawl()
#Je rampe normalement
