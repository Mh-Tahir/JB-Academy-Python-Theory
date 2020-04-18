# The file animals.txt has a list of animals, each written on a new line. 
# Create a new file, animals_new.txt, where those animals are written on a single line and separated by whitespace.
f = open('animals.txt', 'r')
fn = open('animals_new.txt', 'w')
for i in f.readlines():
    fn.write(i.replace('\n', ' '))
fn.close()
f.close()
