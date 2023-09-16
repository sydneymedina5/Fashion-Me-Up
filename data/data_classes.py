from dataclasses import dataclass

@dataclass
class Common:
    color: str
    category: str

@dataclass
class LongPants:
    common: Common

class Shorts:
    common: Common
    
@dataclass
class ShortSleeveShirt:
    common: Common