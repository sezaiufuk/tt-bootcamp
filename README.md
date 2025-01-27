# File Formats

## JSON

Most popular human readable format with schema flexibility.

### Advantages

* Her bir satırın metadatası kendi içinde
  * Schema flexibility
  * Sparse representation.
* Nested/Complex typelara izin var.
* Human readable.
* XML e göre daha az yer tutuyor.
* Satır bazlı sorgularda hızlı

### Disadvantages

* Anahtar/Colon isimleri tekrar ediyor. Depolama verimsiz.
* Attribute/anahtar bazlı gittiğimizde performans kötü.
* Text based olduğu için parsing verimsizlik ?!?
* No type forcing.

## Fix Length

Most popular format in old generation main frame systems.

### Advantages

* Fast offset based parsing
* Prevent memory/disk fragmentation (SLAB allocators)
* Human readable.
* Satır bazlı sorgularda hızlı

### Disadvantages

* Redundant space usage
* No type forcing.
* Text based olduğu için parsing verimsizlik ?!?
* No metadata information.
* Nested/Complex typelara izin yok.
* Colon bazlı sorgularda yavaş
* Schema evaluation (type resizing) çok zor.
* Yeni alan sadece sona eklenebiliyor.


## Delimited File System

### Advantages

* Lots of tool support.
* Relatively compacted compared to Fix Length.
* Human readable.
* Satır bazlı sorgularda hızlı

### Disadvantages

* Less readable compared JSON and fix length.
* No type forcing.
* Text based olduğu için parsing verimsizlik ?!?
* No metadata information.
* Partial support on Nested/Complex typelara.
* Colon bazlı sorgularda yavaş
* Schema evaluation (type resizing) zor.
* Yeni alan sadece sona eklenebiliyor.


## Custom Columnar Format

### Advantages

* Relatively compacted compared to Fix Length.
* Human readable.
* Satır bazlı sorgularda yavaş
* Better compression
* Filter performans ? 

### Disadvantages

* Deletion ? 
* Less readable compared JSON and fix length.
* No type forcing.
* Text based olduğu için parsing verimsizlik ?!?
* No metadata information.
* Partial support on Nested/Complex typelara.
* Muuuuch faster columnar queries
* Schema evaluation (type resizing) zor.
