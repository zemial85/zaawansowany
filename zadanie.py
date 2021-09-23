#pobaw sie w nauczyciela
# - nauczyciel podaje ocene ze sprawdzianu (pojedynczy int)
  # gdy nauczyciel poda ocene spoza skali podnies błąd SchoolError. SchoolError to twoj customowy wyjątek

class GradeOutOfRange(Exception):
    pass
class LetterIsNotDigit(Exception):
    pass

a = input("Podaj ocenę: ")
if not a.isdigit():
    raise LetterIsNotDigit("Grade must be a digit")
if int(a) not in range(1, 7):
    raise GradeOutOfRange("Grade not in range")
print("Grade in range")

