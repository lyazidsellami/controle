note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

notes_eleve1 =  [note1[2], note2[2], note3[2], note4[2], note5[2], note6[2]]
print(notes_eleve1)

#Q4.a
somme_1 = sum(notes_eleve1)
moy_eleve1 = somme_1/len(notes_eleve1) 
print("Moyenne générale de l'élève 1 :", moy_eleve1)

#Q4.b

def moyenne_tuples(notes,eleve,matiere):
  s=0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s= s+x[2]
      i = i +1
  moy = s / i
  return moy

print("La moyenne e l'élève 1 en math est ", moyenne_tuples(notes,'eleve1','math'))

#Q4.c

def moyenne_tuples(notes,eleve,matiere):
  s=0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s= s+x[2]
      i = i +1
  moy = s / i
  return moy


  #Q5

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


#Q6

class Note:
def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
self.eleve = eleve
self.matiere = matiere
self.valeur = valeur
def afficherNote(self):
print(self.valeur)
onote = Note('eleve1', 'maths', 13)
onote.afficherNote()







class Demo:
  classattr = 'defaut'
  def __init__(self, a):
    self.a = a


demo1 = Demo(1)
demo2 = Demo(2)

print(demo1.a)
print(demo2.a)
print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 23

print(demo1.classattr)
print(demo2.classattr)

demo1.classattr = -1

print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 14






class Demo:
  classattr = 'defaut'
  def __init__(self, a):
    self.a = a

  @classmethod #attention !
  def default_len(cls):
    return len(cls.classattr)

print(Demo.default_len())






from .main import Note

def test_ajout():
  Note.vider()
  # assert
  Node(eleve = 'eleve1', matiere='math', 12)
  # assert













