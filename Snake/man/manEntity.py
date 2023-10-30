

import sys
import os

# Obtén la ruta del directorio actual (donde se encuentra manEntity.py)
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agrega la ruta del directorio man/ (el directorio principal) al sys.path
ruta_proyecto = os.path.join(directorio_actual, '..')
sys.path.append(ruta_proyecto)
import man.utils.slotmap as Utils
import cmp.components as Components
class Entity:
    def __init__ (self):
        self.cmpMask = 0
        self.tagMask = 0
        self.keys = list()
        for i in range(0, 10):
            self.keys.append(Utils.key_type())

    def addComponent(self, cmp):
        self.cmpMask = self.cmpMask | cmp.utils.mask
    def addTag(self, tag):
        self.tagMask = self.tagMask | tag
    def eraseTag(self, tag):
        self.tagMask ^= tag
    def hasComponent(self, cmp):
        return self.cmpMask & cmp.utils.mask
    def hasTag(self, tag):
        return self.tagMask & tag
    def getComponentMask(self):
        return self.cmpMask
    def getTagMask(self):
        return self.tagMask

class ComponentStorage:
    def __init__(self):
        self.slotsCmp = list()
        for i in range(0, Components.numberOfComponents):
            self.slotsCmp.append(Utils.Slotmap(10))
    def getStorage(self, cmp):
        return self.slotsCmp[cmp.utils.slot]
    def addCmp(self, cmp):
        return self.slotsCmp[cmp.utils.slot].push_back(cmp)
    def clearComponentStorage(self):
        for element in self.slotsCmp:
            element.clear()


class ManEntity:
    def __init__(self):
        self.entities_ = list()
        self.componentStorage = ComponentStorage()
    def createEntity(self, cmps:list, tags:list):
        entidad = Entity()
        self.addCmpsToEntity(entidad, cmps)
        self.addTagsToEntity(entidad, tags)
        self.entities_.append(entidad)
        return self.entities_[-1]
    def addCmpsToEntity(self, e:Entity, cmpList:list):
        for cmp in cmpList:
            e.addComponent(cmp)
            key = self.componentStorage.addCmp(cmp)
            e.keys[cmp.utils.slot] = key # ? orden ? 
    def addTagsToEntity(self, e:Entity, tagList:list):
        for t in tagList:
            e.addTag(t)
    def getEntityCMP(self, e:Entity, cmp):
        if e.hasComponent(cmp):
            return self.componentStorage.slotsCmp[cmp.utils.slot].get(e.keys[cmp.utils.slot])
    def getEntities(self):
        return self.entities_
    def forallMatching(self, doFunction, cmps:list, tags:list, wn):
        for e in self.entities_:
            cmp_ok = True
            tag_ok = True
            for cmp in cmps:
                if not e.hasComponent(cmp):
                    cmp_ok = False
            for tag in tags:
                if not e.hasTag(tag):
                    tag_ok = False
            if (cmp_ok == True) and (tag_ok == True):
                doFunction(self, e, wn)
    def forall(self, doFunction):
        for e in self.entities_:
            doFunction(e)







        