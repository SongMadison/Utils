from dataclasses import dataclass, field
from typing import List

@dataclass
class Book:
    '''Object for tracking physical books in a collection.'''
    name: str    
    weight: float = field(default=0.0, repr=False)
    shelf_id: int = field(init=False)
    chapters: List[str] = field(default_factory=list)
    condition: str = field(default="Good", compare=False)

    def __post_init__(self):
        if self.condition == "Discarded":
            self.shelf_id = None
        else:
            self.shelf_id = 0

if __name__=='__main__':
    chapters = ['reason', 'feeling']
    # don't initialize shelf_id, it processed in __post_init__
    b = Book('reason and feeling', 1.0,  chapters, 'good')
    print(b)
    print(b.weight)
    b.weight  = 0.5
    print(b.weight)

    c = Book(name = 'reason and feeling', 
    weight = 1.0,  
    chapters = chapters, 
    condition ='Discarded')
    print(c)

    print(b[0])