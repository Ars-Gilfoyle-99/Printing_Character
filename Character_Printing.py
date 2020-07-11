string=input("Enter a string");
string=string.lower();
char=[0]*26;
for i in string:
    a=ord(i)-97;
    char[a]+=1;
print(char);
i=0;
while i<26:
    if char[i]>0:
        print(chr(i+97)+'='+str(char[i]));
    i+=1;    
