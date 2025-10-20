#مشروع الأسماء المختصره 
names = input("Inter The names spearated by a comma: ").split(", ")

Final_result = []

for name in names:
  name_parts = name.split()
#الحصول علي الإسم الأول والإسم الثاني من الأسماء المدخلة
  frist_name = name_parts[0]
  last_name = name_parts[1]
#نحصل علي الحروف الأولي من الإسمين
  frist_letter = frist_name[0]
  last_letter = last_name[0]
#نضع الحروف الأولي من كل اسم في قائمه متخزنه عندنا
  final_loop = frist_letter + "." + last_letter + "."
  Final_result.append(final_loop)

#نطبع القائمه التي تحتوي علي الحروف المختصره النهائيه
for x in Final_result:
  print(x)


#المشروع رقم 2

#مشروع عكس الكلمه
sentence = input("Enter a sentence: ").split()
#مخلي الكلمه تتطبع بالعكس
print(sentence[::-1])#المسافه الفاضيه يعني اطبع من اول بدابه الجمله الي أخرها 
#فصل الكلمات التي في القائمه لكي تكتب عادي كجمله
sentence_2 = " ".join(sentence[::-1])
print(f"Reverrsed sentence is: {sentence_2}")



