#1. The Canvas & Output (Setup aur Save karna):
#plt.figure(figsize=(10, 6)): Graph banane se pehle uski screen/photo ka size tay karna (lambaai aur chaudaai).
#plt.show(): Code complete hone ke baad graph ko screen par pop up karna.
#plt.savefig('file_ka_naam.png'): Us graph ki HD photo apne computer mein save karna.

#2. The "Big 4" Graphs (Tumhare asali 4 hathiyar):
#plt.bar(): Bar Chart - Jab do cheezon ko compare karna ho (Jaise CT aur MRI mein se kahan zyada log aaye).
#plt.pie(): Pie Chart - Jab 100% mein se hissa (percentage) dekhna ho (Jaise total budget kahan kharch hua).
#plt.plot(): Line Chart - Jab time ke hisaab se trend dekhna ho (Jaise patient ka BP ya ICU ke cases pichle 10 din mein kaise upar-neeche hue).
#plt.hist(): Histogram - Bheed ka distribution dekhne ke liye (Bohot zaroori! Jaise hospital mein aaye patients mein se kitne 20-30 
#                                                             saal ke hain, kitne 30-40 ke).

#3. The "Makeup" (Formatting - Report ko professional banane ke liye):
#plt.title("Title Here"): Graph ke sabse upar main heading dalna.
#plt.xlabel("Text") & plt.ylabel("Text"): X (neeche) aur Y (khadi line) par kya likha hai, uska naam dena.
#plt.legend(): Graph ke kone mein wo chhota sa box banana jo batata hai ki "Laal rang ka matlab Emergency hai, aur Neele ka matlab Surgery".
# 3. THE MAGIC TRICK: Har bar ke upar uska exact number print karna
# padding=3 aur fontweight='bold': Yeh thoda sa 'Makeup' hai. padding=3 ka matlab hai number bar ke bilkul
#  upar chipka na ho, thoda sa space (gap) ho. Aur bold se number dark aur clear dikhega.
#plt.bar_label(bars, padding=3, fontweight='bold')
#plt.scatter(X-axis_Data, Y-axis_Data): Scatter Plot - Jab do cheezon ke beech ka relationship dekhna ho (Jaise patient ki age aur uska recovery time).