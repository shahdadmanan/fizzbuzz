def unique_words(file):
	text_file= open(file, 'r')
	text= text_file.read()

	#now we clean the text

	text=text.lower()
	words=text.split()
	words= [word.strip('.,!()[]"') for word in words]
	words = [word.replace("'s", '') for word in words]
	words = ["".join(c for c in string if c.isalnum()) for string in words]

	#now we find all the unique words

	unique= []
	for word in words:
		if word not in unique:
			unique.append(word)

	#sorting
	unique.sort()

	#print
	return(unique)


def count_the_articles(file):
	text_file=open(file,'r')
	text=text_file.read()
	#cleaning the data
	text= text.lower()
	words= text.split()
	articles= ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	count=0
	for word in words:
		if word in articles:
			count= count + 1
	print("count of articles is : ", count)

def sorted_words(l1):
	print(sorted(l1, key=len))

def character_word_count(words):
	count={}
	for word in words:
		count[word] = len(word)
	return count

def starts_with_vow(words):
	count=0
	for word in words:
		if word != "":
			if word[0] in "aeiou":
				count += 1
	print("total words starting with vowel are: ", count)

def rare_words(words, file):
	text_file = open(file, 'r')
	text= text_file.read()
	text = text.lower()
	ref = text.split()
	ref = [word.strip('.,!;()[]" ') for word in ref]
	ref = [word.replace("'s", '') for word in ref]
	ref = ["".join(c for c in string if c.isalnum()) for string in ref]
	mylist=[]
	for i in words:
		if i not in ref:
			mylist.append(i)
	print(mylist)
	
def unused_words(ref, unique_words1, unique_words2, unique_words3):
	text_file = open(ref, 'r')
        text= text_file.read()
        text = text.lower()
        ref = text.split()
        ref = [word.strip('.,!;()[]" ') for word in ref]
        ref = [word.replace("'s", '') for word in ref]
        ref = ["".join(c for c in string if c.isalnum()) for string in ref]
	mylist=[]
	for i in ref:
		if i not in unique_words1:
			if i not in unique_words2:
				if i not in unique_words3:
					mylist.append(i)
	print(mylist)
	print("total number: ", len(mylist))



file1="/home/madhatter/fizbuzz-Abdul/openbook1-shahdadmanan/Book1.txt"
file2="/home/madhatter/fizbuzz-Abdul/openbook1-shahdadmanan/Book2.txt"
file3="/home/madhatter/fizbuzz-Abdul/openbook1-shahdadmanan/Book3.txt"    
fileref= "/home/madhatter/fizbuzz-Abdul/openbook1-shahdadmanan/20k.txt" 
l1= unique_words(file1)
l2= unique_words(file2)
l3= unique_words(file3)
unused_words(fileref,l1,l2,l3)
#count_the_articles(file)
#sorted_words(l1)
#x= character_word_count(l1)
#print(x)
#starts_with_vow(l1)
#rare_words(l1,fileref)
		
