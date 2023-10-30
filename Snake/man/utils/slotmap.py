
class key_type:
    def __init__(self):
        self.id  = 0
        self.gen = 0
        

class Slotmap:    
    def __init__(self, capacity):
        self.size_ = 0
        self.freelist_ = 0
        self.generation_ = 0
        self.capacity_ = capacity
        self.indices_ = list()
        for e in range(0,10):
            self.indices_.append(key_type())
        self.erase_ = [int()] * capacity
        self.data_ = [None] * capacity
        self.clear()
    def is_valid(self, key:key_type):
        if key.id >= self.capacity_ or self.indices_[key.id].gen != key.gen:
            return False
        return True
    def clear(self):
        self.freelistInit()
        self.size_ = 0
    def freelistInit(self):
        i=0
        for element in self.indices_:
            element.id = i+1
            i+=1
        self.freelist_ = 0
    def size(self):
        return self.size_
    def capacity(self):
        return self.capacity_
    def push_back(self, value):
        reservedID = self.allocate()
        slot = self.indices_[reservedID]
        self.data_[slot.id] = value
        self.erase_[slot.id] = reservedID
        
        key = slot
        key.id = reservedID

        return key    
    def allocate(self):
        if (self.size_ >= self.capacity_):
            raise ValueError("No space left in the slotmap")
        assert(self.freelist_ < self.capacity_)
        slotid = self.freelist_
        self.freelist_ = self.indices_[slotid].id
        slot = self.indices_[slotid]
        slot.id = self.size_
        slot.gen = self.generation_
        self.size_ += 1
        self.generation_ += 1
        return slotid
    def erase(self, key:key_type):
        if not self.is_valid(key):
            return False
        self.free(key)
        return True
    def free(self, key:key_type):
        assert(self.is_valid(key))
        slot    = self.indices_[key.id]
        dataid  = slot.id
        slot.id = self.freelist_
        slot.gen= self.generation_
        self.freelist_ = key.id

        if dataid != (self.size_ - 1):
            self.data_[dataid]  = self.data_[self.size_ - 1]
            self.erase_[dataid] = self.erase_[self.size_ - 1]
            self.indices_[self.erase_[dataid]].id = dataid
        
        self.size_ -= 1
        self.generation_ += 1

    def get(self, key:key_type):
        assert(self.is_valid(key))
        dataID = self.indices_[key.id].id
        return self.data_[dataID]
    def getData(self):
        return self.data_
    def getFreelist(self):
        return self.freelist_
