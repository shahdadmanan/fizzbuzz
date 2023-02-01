import os
file="sourcefile.txt"
target_file= "destfile.txt"
target_folder= "/home/madhatter/fizbuzz-Abdul"
start_page= input("enter start page: ")
end_page= input ("enter end page: ")
def leet_code(text):
	text=text.replace("a","4")
	text=text.replace("e","3")
	text=text.replace("i","1")
	text=text.replace("o","0")
	text=text.replace("s","5")
	return text

def copy_page(file, start_page,end_page,target_file,target_folder):
	if target_folder:
		if not os.path.exists(target_folder):
			os.makedirs(target_folder)
		target_file= os.path.join(target_folder, target_file)
	
	with open(file, "r") as f:
		lines=f.readlines()
	
	start_line= (start_page-1) *25
	end_line = end_page * 25
	pages=lines[start_line:end_line]
	
	with open(target_file, "w") as f:
		for page in pages:
			f.write(leet_code(page))

copy_page(file,start_page,end_page,target_file,target_folder)
