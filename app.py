#   Importing Python responsories
import sys
import csv
def main():
    """
    #   Author :    krigjo25
    #   Date :      30.08-22

    #   Expects the user to provide two command-line arguments
    #   If the user does not provide exactly two command-line arguments
    #   if the first cannot be read, the program should exit via sys.exit with an error message.

    """

    #   Ensure the user provides two command-line arguments
    if len(sys.argv) != 3: sys.exit("Usage : python scourgify.py  [infile] [filepath]")

    #   Ensure the first argument is a CSV file
    if ".csv" not in sys.argv[1]:sys.exit("Not a CSV file")

    #   Time complexity : O(n)(x 1000)  = Log(n) = 2.88s (-0.1s from the original)
    CSVReader(sys.argv[1], sys.argv[2])

def CSVReader(Infile, Outfile):
    """
    #   Author :    krigjo25
    #   Date :      06.09-22
    #   Description :
            Cleans a csv file, by sorting by firstname, lastname.add()
    #   Time complexity : O(n) x 1000 2.88s (-0.1s from the original)

    """
    #   Initializing a list
    student = []
    fieldnames = ["first name", "last name", "house"]

    #   Open the csv file & write to a new CSV file
    with open(f"{Infile}", 'r') as f:

        #   Read the csv file
        cr = csv.DictReader(f)

        #   Parse the CSV file
        for row in cr:

            last, first = row["name"].split(",")
            student.append(
                {
                    "first name":first, 
                    "last name":last, 
                    "house": row["house"]
                })

    with open(f"{Outfile}", 'w') as w:
        
        #   Initialize the csv writer
        cw = csv.DictWriter(w, fieldnames=fieldnames)

        #   Write the rows
        cw.writeheader()
        cw.writerows(student)

if __name__ == '__main__':
    main()
