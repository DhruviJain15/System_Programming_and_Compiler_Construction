#productions=input("Enter the productions").split(",");
#print(productions);
#variables=input("Enter the variables").split(",");
lhs=input("Enter the lhs of grammar: ")
print("Enter | to separate the grammars");
rhs=input("Enter the rhs of grammar: ").split("|");

alpha=[];
beta=[];
newvar=[];
adash=[];
for string in rhs:
	if(string[0]==lhs):
		#print("left recursion");
		alpha.append(string[1:]);
		#print(alpha);
	else:
		beta.append(string);
		#print(beta);


for word in beta:
	newvar.append(word+lhs+"'");
#print(newvar);
for word in alpha:
	adash.append(word+lhs+"'");
#print(adash);

print(lhs, " --> ",end="");
for n in newvar:
	 print(n , end="|");
print();

print(lhs+"'", " --> ",end="");
for a in adash:
	 print(a , end="|");
print("e");


	
		

	


	 