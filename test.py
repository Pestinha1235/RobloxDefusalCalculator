from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hexadecimal', methods=["GET", "POST"])
def hexadecimal():
    answer = ""
    if request.method == "POST":
        digits = request.form.get('digits', "")
        try:
            if " " in digits:
                for h in digits.strip().upper().split():
                    answer += chr(int(h, 16))
            else:
                for i in range(0, len(digits), 2):
                    answer += chr(int(digits[i:i+2].upper().strip(), 16))
        except ValueError:
            answer = "Invalid hexadecimal values."
    return render_template('hexadecimal.html', answer=answer)

@app.route('/squares', methods=["GET", "POST"])
def squares():
    num1 = num2 = num3 = num4 = ""
    answer = None
    if request.method == "POST":
        num1 = request.form.get('num1', "").strip()
        num2 = request.form.get('num2', "").strip()
        num3 = request.form.get('num3', "").strip()
        num4 = request.form.get('num4', "").strip()
        if num1 and num2 and num3 and num4: 
            try:
                n1 = int(num1)
                n2 = int(num2)
                n3 = int(num3)
                n4 = int(num4)
                y=(n1+n2+n3+n4)/2
                x=0
                if n1<=10:x=15
                elif n1>10 and n1<=20:x=20
                elif n1>20 and n1<=80:x=30
                else:x=10
                if n2<=10:x+=10
                elif n2>10 and n2<=20:x*=2
                elif n2>20 and n2<=80:x*=3
                else:x-=10
                if n3<=10:x*=2
                elif n3>10 and n3<=20:x*=3
                elif n3>20 and n3<=80:x-=5
                if n4<=10:x*=2
                elif n4>10 and n4<=20:x+=20
                elif n4>20 and n4<=80:x+=50
                else:x*=3
                result=x-y
                if result <= 0:answer = f"num1: {n1}, num2: {n2}, num3: {n3}, num4: {n4}"
                elif result < 20:answer = f" num1: {n1}, num4: {n4}, num3: {n3}, num2: {n2}"
                elif result < 50:answer = f"num2: {n2}, num1: {n1}, num3: {n3}, num4: {n4}"
                elif result < 90:answer = f"num4: {n4}, num2: {n2}, num3: {n3}, num1: {n1}"
                else:answer = f"num3: {n3}, num1: {n1}, num4: {n4}, num2: {n2}"
            except ValueError:
                answer = "Invalid input values."
    return render_template('squares.html', answer=answer)

@app.route('/verticallights', methods=["GET", "POST"])
def verticallights(): 
    number = []
    number0  = 0
    number1 = 0
    answer = ""
    lights = ""
    if request.method == "POST":
        lights = request.form.get('lights', "").strip() #if lights is an empty string for i in lights will not run NEED TO FIX THIS
    if lights:  # Check if lights is not an empty string
        try:
            number = [int(i) for i in lights]
            number0 = number.count(0)
            number1 = number.count(1)
            size = len(number)
            if size == 7:
                if  1 not in number:answer = "Click once"
                elif number[1] == 1 and number[6] == 0:answer = "Click twice"
                elif number[0] == 1 and number[1] == 1:answer = "Click three times"
                elif number[0] == 0 and number[6] == 0:answer = "Click four times"
                elif number[0] == 1 and number[1] == 1 and number[2] == 1:answer = "Click five times"
                elif number0 > 3:answer = "Click seven times"
                elif number1 > 5:answer = "Click eight times"
                elif 0 not in number:answer = "Click nine times"
            else:
                answer = "Invalid input length. Please enter exactly 7 digits."
        except ValueError:
            answer = "Invalid input values. Please use only 0s and 1s."
    return render_template('verticallights.html', answer=answer)
@app.route('/letterstoonumbers', methods=["GET", "POST"])
def letterstoonumbers():
        digitslist=[]
        answer = ""
        if request.method == "POST":
            digits = request.form.get('digits', "").lower()
            replacement ={"a": "1", "b": "3", "c": "7", "d": "2", "e": "4", "f": "5", "g": "6", "h": "0", "i": "8", "j": "9"}
            digits = ''.join(replacement.get(char, char) for char in digits)
            try:
                if " " in digits:
                    digitslist = (digits.split())
                else:
                    digitslist = [(digits[i:i+2]) for i in range(0, len(digits), 2)]
                if len(digitslist) == 2 and all(len(i) == 2 for i in digitslist):
                        ans = int(digitslist[0]) * int(digitslist[1])
                        answer = f"The answer is: {ans}"
                else:
                    answer = "Please enter exactly two pairs of letters."   
            except ValueError:
                answer = "Invalid input. Please enter valid letters corresponding to the digit pairs."
        return render_template('letterstoonumbers.html', answer=answer)
@app.route("/colorsmodule", methods=["GET", "POST"])
def colorsmodule():
    answer = ""
    number=[]
    red = False
    orange = False
    yellow = False
    green = False
    blue = False
    purple = False
    order1 = False
    order2 = False
    order3 = False
    if request.method == "POST":
        x=(request.form.get('numbers', "").strip())
        try:
            if len(x) != 6 or not x.isnumeric():
                raise ValueError("Input must be a 6-digit number.")
            for i in str(x):
                number.append(i)
            red = int(number[0])<6
            orange = not red
            yellow = int(number[1])<6
            green = not yellow
            blue = int(number[2])<6
            purple = not blue
            order1 = int(number[3])<7
            order2 = int(number[4])<7
            order3 = int(number[5])<7
            if red:
                if yellow:
                    if blue:
                        if order1:answer = ("Red Yellow Blue Green Purple Orange")
                        elif order2:answer = ("Red Yellow Blue Purple Green Orange")
                        elif order3:answer = ("Red Yellow Blue Orange Green Purple")
                        else:answer = ("Red Yellow Blue Orange Purple Green")
                    elif purple:
                        if order1:answer = ("Red Yellow Purple Green Blue Orange")
                        elif order2:answer = ("Red Yellow Purple Blue Green Orange")
                        elif order3:answer = ("Red Yellow Purple Orange Green Blue")
                        else:answer = ("Red Yellow Purple Orange Blue Green")
                elif green:
                    if blue:
                        if order1:answer = ("Red Green Blue Yellow Purple Orange")
                        elif order2:answer = ("Red Green Blue Purple Yellow Orange")
                        elif order3:answer = ("Red Green Blue Orange Yellow Purple")
                        else:answer = ("Red Green Blue Orange Purple Yellow")
                    elif purple:
                        if order1:answer = ("Red Green Purple Yellow Blue Orange")
                        elif order2:answer = ("Red Green Purple Blue Yellow Orange")
                        elif order3:answer = ("Red Green Purple Orange Yellow Blue")
                        else:answer = ("Red Green Purple Orange Blue Yellow")
            elif orange:
                if yellow:
                    if blue:
                        if order1:answer = ("Orange Yellow Blue Green Purple Red")
                        elif order2:answer = ("Orange Yellow Blue Purple Red Green")
                        elif order3:answer = ("Orange Yellow Blue Red Green Purple")
                        else:answer = ("Orange Yellow Blue Red Purple Green")
                    elif purple:
                        if order1:answer = ("Orange Yellow Purple Green Blue Red")
                        elif order2:answer = ("Orange Yellow Purple Blue Green Red")
                        elif order3:answer = ("Orange Yellow Purple Red Green Blue")
                        else:answer = ("Orange Yellow Purple Red Blue Green")
                elif green:
                    if blue:
                        if order1:answer = ("Orange Green Blue Yellow Purple Red")
                        elif order2:answer = ("Orange Green Blue Purple Yellow Red")
                        elif order3:answer = ("Orange Green Blue Red Yellow Purple")
                        else:answer = ("Orange Green Blue Yellow Purple Red")
                    elif purple:
                        if order1:answer = ("Orange Green Purple Yellow Blue Red")
                        elif order2:answer = ("Orange Green Purple Blue Yellow Red")
                        elif order3:answer = ("Orange Green Purple Red Yellow Blue")
                        else:answer = ("Orange Green Purple Red Blue Yellow")
        except (ValueError, IndexError):
            answer = "Invalid input. Please enter a 6-digit number."
    return render_template('colorsmodule.html', answer=answer)

@app.route("/colortiming", methods=["GET", "POST"])
def colortiming():
    answer = ""
    number = []
    digitslist=[]
    if request.method == "POST":
        digits=request.form.get('digits', "").strip().lower()
        try:
            if len(digits) != 4:
                answer = "Please enter exactly 4 characters."
                return render_template('colortiming.html', answer=answer)   
            dictionary = {"a": "4", "b": "3", "c": "7", "d": "9"}
            number = [dictionary.get(i, i) for i in digits]
            digitslist.append(int(number[0]) + int(number[1]))
            digitslist.append(int(number[2]) + int(number[3]))
            ans = int(digitslist[0]) * int(digitslist[1])
            if ans<=59:answer = ("white")
            elif ans<=99:answer = ("red")
            elif ans<=199:answer = ("yellow")
            elif ans<=299:answer = ("green")
            elif ans<=399:answer = ("blue")
            elif ans<=499:answer = ("yellow")
            elif ans<=599:answer = ("red")
            else:answer = ("white")
        except ValueError:
            answer = "Invalid input. Please enter valid letters corresponding to the digit pairs."  
    return render_template('colortiming.html', answer=answer)

@app.route('/divisibility', methods=["GET", "POST"])
def divisibility():
    answer = ""
    by2= False
    by3= False
    by5= False
    by7= False
    if request.method == "POST":
        x=request.form.get('digits', "").strip()
        try:
            x=int(x)
            by2 = x%2==0
            by3 = x%3==0
            by5 = x%5==0
            by7 = x%7==0
            if by2:
                if by3:
                    if by5:
                        if by7:answer = "D"
                        else:answer = "C"
                    else:
                        if by7:answer = "C"
                        else:answer = "B"
                else:
                    if by5:
                        if by7:answer = "A"
                        else:answer = "B"
                    else:
                        if by7:answer = "E"
                        else:answer = "A"
            else:
                if by3:
                    if by5:
                        if by7:answer = "A"
                        else:answer = "B"
                    else:
                        if by7:answer = "B"
                        else:answer = "D"
                else:
                    if by5:
                        if by7:answer = "E"
                        else:answer = "F"
                    else:
                        if by7:answer = "C"
                        else:answer = "F"
        except ValueError:
            answer = "Invalid input. Please enter a valid number."
    return render_template('divisibility.html', answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)